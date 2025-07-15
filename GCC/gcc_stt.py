import os
from google.cloud import speech

def run_google_stt(audio_path, output_dir):
    client = speech.SpeechClient()

    with open(audio_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US"
    )

    response = client.recognize(config=config, audio=audio)

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, os.path.splitext(os.path.basename(audio_path))[0] + ".txt")

    with open(output_file, "w") as f:
        for result in response.results:
            f.write(result.alternatives[0].transcript + "\n")

    print(f"Saved: {output_file}")