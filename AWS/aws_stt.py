import os
import boto3
import time
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context #added to get by ssl certificate isses

def run_aws_stt(audio_path, output_dir):
    s3 = boto3.client("s3")
    transcribe = boto3.client("transcribe")

    # Configuration
    bucket_name = "project-loqui-audio"  # Replace with your actual bucket name
    job_name = os.path.splitext(os.path.basename(audio_path))[0]
    s3_key = os.path.basename(audio_path)
    job_uri = f"s3://{bucket_name}/{s3_key}"

    # Upload audio to S3
    print(f"Uploading {audio_path} to S3 bucket: {bucket_name}")
    s3.upload_file(audio_path, bucket_name, s3_key)
    print("Upload complete.")

    # Start transcription job
    print("Starting AWS Transcribe job...")
    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={"MediaFileUri": job_uri},
        MediaFormat="wav",
        LanguageCode="en-US"
    )

    # Wait for job to complete
    print("Waiting for job to complete...")
    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        if status["TranscriptionJob"]["TranscriptionJobStatus"] in ["COMPLETED", "FAILED"]:
            break
        time.sleep(5)

    # Fetch and save transcription
    if status["TranscriptionJob"]["TranscriptionJobStatus"] == "COMPLETED":
        transcript_url = status["TranscriptionJob"]["Transcript"]["TranscriptFileUri"]
        transcript_data = boto3.client("s3").get_object(Bucket=bucket_name, Key=s3_key)
        os.makedirs(output_dir, exist_ok=True)

        output_file = os.path.join(output_dir, f"{job_name}.txt")
        import urllib.request
        with urllib.request.urlopen(transcript_url) as response:
            result = json.loads(response.read().decode("utf-8"))
            transcript_text = result["results"]["transcripts"][0]["transcript"]

        with open(output_file, "w") as f:
            f.write(transcript_text)

        print(f"Transcription saved to {output_file}")
    else:
        print("Transcription job failed.")
