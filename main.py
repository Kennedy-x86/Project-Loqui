import os
import glob
from dotenv import load_dotenv
from jiwer import wer, cer
import matplotlib.pyplot as plt

from GCC.gcc_tts import run_google_tts
from GCC.gcc_stt import run_google_stt
from AWS.aws_tts import run_aws_tts
from AWS.aws_stt import run_aws_stt
from AZURE.azure_tts import run_azure_tts
from AZURE.azure_stt import run_azure_stt

# Load environment variables
load_dotenv()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "JSON_SECRETS/project-loqui-22510709e628.json"

# Directory structure
DIRS = {
    "input_texts": "input_texts",
    "input_speech": "input_speech",
    "generated_speech": "generated_speech",
    "generated_texts": "generated_texts",
    "auto_audio": "automated_speech_dataset",
    "auto_text": "automated_text_dataset",
    "auto_results": "automated_results"
}

for path in DIRS.values():
    os.makedirs(path, exist_ok=True)


def run_automated_stt_test():
    reference_path = "passage.txt"
    if not os.path.exists(reference_path):
        print("Reference passage.txt not found.")
        return

    with open(reference_path, "r") as f:
        reference = f.read().strip().lower()

    audio_files = [f for f in os.listdir(DIRS["auto_audio"]) if f.endswith(".wav")]
    if not audio_files:
        print("No .wav files found in automated_speech_dataset/")
        return

    tools = {
        "Google Cloud": run_google_stt,
        "AWS": run_aws_stt,
        "Azure": run_azure_stt
    }

    scores = {tool: [] for tool in tools}
    failures = []

    for filename in audio_files:
        filepath = os.path.join(DIRS["auto_audio"], filename)
        name_only = os.path.splitext(filename)[0]

        for tool_name, func in tools.items():
            try:
                func(filepath, DIRS["auto_results"])

                if tool_name == "Google Cloud":
                    pattern = os.path.join(DIRS["auto_results"], f"{name_only}.txt")
                elif tool_name == "Azure":
                    pattern = os.path.join(DIRS["auto_results"], f"{name_only}_azure.txt")
                elif tool_name == "AWS":
                    pattern = os.path.join(DIRS["auto_results"], f"{name_only}-*.txt")

                matches = glob.glob(pattern)
                if not matches:
                    raise Exception("No output generated.")

                with open(matches[0], "r") as out:
                    prediction = out.read().strip().lower()
                    scores[tool_name].append((wer(reference, prediction), cer(reference, prediction)))
            except Exception as e:
                print(f"❌ {tool_name} failed on {filename}: {e}")
                failures.append((tool_name, filename))

    scores = {k: v for k, v in scores.items() if v}
    if not scores:
        print("No successful results to evaluate.")
        return

    wer_avg = {k: sum(w for w, _ in v)/len(v) for k, v in scores.items()}
    cer_avg = {k: sum(c for _, c in v)/len(v) for k, v in scores.items()}

    with open(os.path.join(DIRS["auto_results"], "st_results.txt"), "w") as f:
        f.write("STT Evaluation Results\n\n")
        for tool in scores:
            f.write(f"{tool} - WER: {wer_avg[tool]:.2f}, CER: {cer_avg[tool]:.2f}\n")
        if failures:
            f.write("\nFailures:\n")
            for tool, fname in failures:
                f.write(f"{tool} on {fname}\n")

    labels = list(wer_avg.keys())
    wer_vals = [wer_avg[k] for k in labels]
    cer_vals = [cer_avg[k] for k in labels]
    x = range(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    ax.bar([i - width/2 for i in x], wer_vals, width, label='WER')
    ax.bar([i + width/2 for i in x], cer_vals, width, label='CER')
    ax.set_ylabel('Error Rate')
    ax.set_title('STT Tool Performance')
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels)
    ax.legend()
    plt.savefig(os.path.join(DIRS["auto_results"], "st_comparison.png"))
    print("✅ Results saved in automated_results/")


def manual_test():
    print("1. Text to Speech")
    print("2. Speech to Text")
    task = input("Select a task (1 or 2): ").strip()

    if task not in ["1", "2"]:
        print("Invalid task selection.")
        return

    print("\nChoose a provider:")
    print("1. Google Cloud")
    print("2. AWS")
    print("3. Azure")
    provider = input("Select a provider (1, 2, or 3): ").strip()

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
        elif provider == "3":
            run_azure_tts(full_path, DIRS["generated_speech"])
        else:
            print("Selected provider is not supported.")

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
        elif provider == "3":
            run_azure_stt(full_path, DIRS["generated_texts"])
        else:
            print("Selected provider is not supported.")


def main():
    print("Welcome to Project Loqui")
    print("1. Run Automated Test")
    print("2. Manual Test")
    mode = input("Choose mode (1 or 2): ").strip()

    if mode == "1":
        print("1. Text to Speech")
        print("2. Speech to Text")
        task = input("Choose automated task (1 or 2): ").strip()
        if task == "2":
            run_automated_stt_test()
        else:
            print("Automated TTS not implemented yet.")
    elif mode == "2":
        manual_test()
    else:
        print("Invalid mode selected.")


if __name__ == "__main__":
    main()