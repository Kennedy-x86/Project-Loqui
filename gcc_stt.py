from google.cloud import speech

client = speech.SpeechClient()
with open("output.wav", "rb") as audio_file:
    content = audio_file.read()

audio = speech.RecognitionAudio(content=content)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    language_code="en-US",
)

response = client.recognize(config=config, audio=audio)
for result in response.results:
    print("Transcript:", result.alternatives[0].transcript)