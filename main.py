from google.cloud import texttospeech
import os

client = texttospeech.TextToSpeechClient()

def synthesize(text, output_path):
    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
    )

    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    with open(output_path, "wb") as out:
        out.write(response.audio_content)

# Example use:
for idx, sentence in enumerate(text_samples[:10]):
    synthesize(sentence, f"tts_outputs/sample_{idx}.wav")