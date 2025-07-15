# Project-Loqui

**Project-Loqui** is a testing framework that evaluates the round-trip fidelity between Text-to-Speech (TTS) and Speech-to-Text (STT) services using various cloud providers. It supports real input from `.txt`, `.csv`, and `.wav` files and returns generated speech or transcripts through automated pipelines.

## ✅ Features

- Text-to-Speech (TTS) and Speech-to-Text (STT) support
- Google Cloud, AWS (Amazon Polly & Transcribe) support
- Batch `.txt`, `.csv`, and `.wav` file processing
- Outputs saved in organized directories
- Interactive CLI workflow

## 📁 Directory Structure

```
.
├── input_texts/           # Text inputs (.txt or .csv)
├── input_speech/          # Audio inputs (.wav)
├── generated_speech/      # Output audio (.wav or .mp3)
├── generated_texts/       # Output text (.txt)
├── GCC/                   # Google Cloud handlers
├── AWS/                   # AWS Polly and Transcribe handlers
├── JSON_SECRETS/          # GCP credentials file
├── main.py                # CLI runner
├── requirements.txt
└── README.md
```

## 🚀 Usage

1. Clone this repository:
```bash
git clone https://github.com/your-username/project-loqui.git
cd project-loqui
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure Google Cloud:
- Download your `project-loqui-xxxx.json` key from GCP
- Place it in `JSON_SECRETS/`
- `main.py` will pick it up automatically

4. Configure AWS:
```bash
aws configure
```
Enter:
- Access Key ID
- Secret Access Key
- Region: `us-east-1`
- Output format: `json`

5. Place your inputs:
- Text files into `input_texts/`
- Audio files into `input_speech/`

6. Run the app:
```bash
python main.py
```

Then follow the prompt to select:
- Task (TTS or STT)
- Provider (Google Cloud or AWS)
- Input file name

## 🌐 Supported Providers

| Provider      | TTS Support | STT Support |
|---------------|-------------|-------------|
| Google Cloud  | ✅           | ✅           |
| Amazon AWS    | ✅ (Polly)   | ✅ (Transcribe) |
| Microsoft Azure | coming soon | coming soon |

## 🔐 Notes

- Your `.gitignore` ensures no credentials or generated content is committed.
- You must create and configure your own IAM user and credentials for AWS access.

## 👥 Contributors

- Kennedy Onyema-Willys
- Harshita Koppaka
- Jolly Thomas
- Ore Akinbola

## 📄 License

MIT License
