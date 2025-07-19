import os
import requests

def run_azure_tts(input_path, output_dir):
    subscription_key = os.getenv("AZURE_SPEECH_KEY")
    region = os.getenv("AZURE_REGION", "eastus")

    if not subscription_key:
        print("Missing AZURE_SPEECH_KEY environment variable.")
        return

    with open(input_path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    os.makedirs(output_dir, exist_ok=True)

    for idx, text in enumerate(lines):
        ssml = f"""
        <speak version='1.0' xml:lang='en-US'>
            <voice xml:lang='en-US' xml:gender='Female' name='en-US-JennyNeural'>
                {text}
            </voice>
        </speak>
        """

        headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Content-Type': 'application/ssml+xml',
            'X-Microsoft-OutputFormat': 'riff-16khz-16bit-mono-pcm',
        }

        url = f"https://{region}.tts.speech.microsoft.com/cognitiveservices/v1"
        response = requests.post(url, headers=headers, data=ssml.encode("utf-8"))

        if response.status_code == 200:
            output_path = os.path.join(output_dir, f"azure_tts_{idx}.wav")
            with open(output_path, "wb") as out:
                out.write(response.content)
            print(f"Saved: {output_path}")
        else:
            print(f"Azure TTS failed: {response.status_code} - {response.text}")
