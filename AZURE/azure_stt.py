import os
import azure.cognitiveservices.speech as speechsdk

def run_azure_stt(audio_path, output_dir):
    subscription_key = os.getenv("AZURE_SPEECH_KEY")
    region = os.getenv("AZURE_REGION", "eastus")

    if not subscription_key:
        print("Missing AZURE_SPEECH_KEY environment variable.")
        return

    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
    audio_config = speechsdk.audio.AudioConfig(filename=audio_path)

    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    result = recognizer.recognize_once()

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, os.path.splitext(os.path.basename(audio_path))[0] + "_azure.txt")

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        with open(output_file, "w") as f:
            f.write(result.text)
        print(f"Saved: {output_file}")
    else:
        print(f"Azure STT failed: {result.reason}")
