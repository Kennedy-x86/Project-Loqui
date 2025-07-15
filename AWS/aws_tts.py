import os
import boto3

def run_aws_tts(input_path, output_dir):
    # Load text input
    sentences = []
    if input_path.endswith(".txt"):
        with open(input_path, "r") as f:
            sentences = [f.read().strip()]
    elif input_path.endswith(".csv"):
        with open(input_path, "r") as f:
            sentences = [line.strip() for line in f if line.strip()]
    else:
        print("Unsupported file format.")
        return

    # Set up AWS Polly
    polly = boto3.client("polly")

    os.makedirs(output_dir, exist_ok=True)

    for idx, sentence in enumerate(sentences):
        response = polly.synthesize_speech(
            Text=sentence,
            OutputFormat="mp3",
            VoiceId="Joanna"
        )

        output_file = os.path.join(output_dir, f"sample_{idx}.mp3")
        with open(output_file, "wb") as f:
            f.write(response["AudioStream"].read())
        print(f"Saved: {output_file}")
