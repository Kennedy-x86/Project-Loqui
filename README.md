# Project-Loqui

**Project-Loqui** is a testing framework that evaluates the round-trip fidelity between Text-to-Speech (TTS) and Speech-to-Text (STT) services using various cloud providers. It supports real input from `.txt`, `.csv`, and `.wav` files and returns generated speech or transcripts through automated pipelines.

## ✅ Features

- Text-to-Speech (TTS) and Speech-to-Text (STT) support
- Google Cloud, AWS (Amazon Polly & Transcribe), and Azure Cognitive Services
- Batch `.txt`, `.csv`, and `.wav` file processing
- Outputs saved in organized directories
- Interactive CLI workflow
- Uses `.env` for secure environment variable management

## 📁 Directory Structure

```
.
├── input_texts/           # Text inputs (.txt or .csv)
├── input_speech/          # Audio inputs (.wav)
├── generated_speech/      # Output audio (.wav or .mp3)
├── generated_texts/       # Output text (.txt)
├── GCC/                   # Google Cloud handlers
├── AWS/                   # AWS Polly and Transcribe handlers
├── AZURE/                 # Azure TTS and STT handlers
├── JSON_SECRETS/          # GCP credentials file
├── main.py                # CLI runner
├── .env                   # Environment variables for Azure
├── requirements.txt
└── README.md
```

## 🚀 Usage

1. Clone this repository:
```bash
git clone https://github.com/Kennedy-x86/Project-Loqui.git
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

5. Configure Azure:
- Create a Speech resource in the Azure Portal
- In the root directory, create a file named `.env`:
```env
AZURE_SPEECH_KEY=your-azure-key
AZURE_REGION=eastus
```

6. Place your inputs:
- Text files into `input_texts/`
- Audio files into `input_speech/`

7. Run the app:
```bash
python main.py
```

Then follow the prompt to select:
- Task (TTS or STT)
- Provider (Google Cloud, AWS, or Azure)
- Input file name

## 🌐 Supported Providers

| Provider         | TTS Support     | STT Support     |
|------------------|------------------|------------------|
| Google Cloud     | ✅               | ✅               |
| Amazon AWS       | ✅ (Polly)       | ✅ (Transcribe)  |
| Microsoft Azure  | ✅ (Neural TTS)  | ✅ (Speech SDK)  |

## 🔐 Notes

- `.gitignore` protects sensitive directories like credentials and output.
- Azure uses a `.env` file. Google uses JSON credentials. AWS uses `aws configure`.

## 👥 Contributors

- Kennedy Onyema-Willys
- Harshita Koppaka
- Jolly Thomas
- Ore Akinbola

## 📄 License

MIT License
