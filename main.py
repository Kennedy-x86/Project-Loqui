import os
from GCC.gcc_tts import run_google_tts
from GCC.gcc_stt import run_google_stt
from AWS.aws_tts import run_aws_tts
from AWS.aws_stt import run_aws_stt

# === Directory Setup ===
DIRS = {
    "input_texts": "input_texts",
    "input_speech": "input_speech",
    "generated_speech": "generated_speech",
    "generated_texts": "generated_texts"
}

# Ensure all directories exist
for dir_path in DIRS.values():
    os.makedirs(dir_path, exist_ok=True)

# Set Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "JSON_SECRETS/project-loqui-22510709e628.json"

def main():
    print("Welcome to Project Loqui")
    print("1. Text to Speech")
    print("2. Speech to Text")
    task = input("Select a task (1 or 2): ").strip()

    if task not in ["1", "2"]:
        print("Invalid task selection.")
        return

    print("\nChoose a provider:")
    print("1. Google Cloud")
    print("2. AWS")
    print("3. Azure (coming soon)")
    provider = input("Select a provider (1, 2, or 3): ").strip()

    # File selection
    if task == "1":
        filename = input("Enter the name of the text file (in input_texts/): ").strip()
        full_path = os.path.join(DIRS["input_texts"], filename)
        if not os.path.isfile(full_path):
            print("File not found.")
            return

        if provider == "1":
            run_google_tts(full_path, DIRS["generated_speech"])
        elif provider == "2":
            run_aws_tts(full_path, DIRS["generated_speech"])
        else:
            print("Selected provider is not supported yet for TTS.")

    elif task == "2":
        filename = input("Enter the name of the audio file (in input_speech/): ").strip()
        full_path = os.path.join(DIRS["input_speech"], filename)
        if not os.path.isfile(full_path):
            print("File not found.")
            return

        if provider == "1":
            run_google_stt(full_path, DIRS["generated_texts"])
        elif provider == "2":
            run_aws_stt(full_path, DIRS["generated_texts"])
        else:
            print("Selected provider is not supported yet for STT.")

if __name__ == "__main__":
    main()
