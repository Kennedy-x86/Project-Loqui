from google.cloud import texttospeech
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "JSON_SECRETS/project-loqui-22510709e628.json"

client = texttospeech.TextToSpeechClient()
input_text = texttospeech.SynthesisInput(text="Hello, Kennedy!")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)
audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

response = client.synthesize_speech(
    input=input_text,
    voice=voice,
    audio_config=audio_config
)

with open("output.mp3", "wb") as out:
    out.write(response.audio_content)