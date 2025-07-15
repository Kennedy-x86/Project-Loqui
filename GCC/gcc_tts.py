import os
from google.cloud import texttospeech

def run_google_tts(input_path, output_dir):
    client = texttospeech.TextToSpeechClient()

    # Determine input type (.txt or .csv)
    sentences = []
    if input_path.endswith(".txt"):
        with open(input_path, "r") as f:
            sentences = [f.read().strip()]
    elif input_path.endswith(".csv"):
        with open(input_path, "r") as f:
            sentences = [line.strip() for line in f if line.strip()]
    else:
        print("Unsupported text file format.")
        return

    os.makedirs(output_dir, exist_ok=True)

    for idx, sentence in enumerate(sentences):
        synthesis_input = texttospeech.SynthesisInput(text=sentence)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16
        )

        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        out_file = os.path.join(output_dir, f"sample_{idx}.wav")
        with open(out_file, "wb") as out:
            out.write(response.audio_content)
        print(f"Saved: {out_file}")
