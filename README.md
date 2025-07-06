# Project-Loqui

**Project-Loqui** is a research and testing framework designed for evaluating the round-trip fidelity between Text-to-Speech (TTS) and Speech-to-Text (STT) tools using real-world input samples. This project was developed for CSCE 4460 (Software Testing and Empirical Methodologies) at the University of North Texas.

## 📌 Objective

To empirically test how accurately cloud-based TTS and STT services preserve original meaning, formatting, and named entities when combined in a round-trip (text → speech → text) pipeline.

## 🧰 Technologies Used

- **Google Cloud Text-to-Speech (TTS)**
- **Google Cloud Speech-to-Text (STT)**
- Python 3.11+
- BERTScore and error metrics (WER, CER)

## 📁 Repository Structure

```
.
├── JSON_SECRETS/               # Google Cloud service account key
│   └── project-loqui-xxxx.json
├── gcc_tts.py                  # Sends text to Google TTS and saves audio
├── gcc_stt.py                  # Sends audio to Google STT and gets transcript
├── main.py                     # End-to-end round-trip testing logic
├── README.md
└── LICENSE
```

## 🚀 How to Use

1. Clone the repository:
```bash
git clone https://github.com/Kennedy-x86/Project-Loqui.git
cd Project-Loqui
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set your Google credentials in code or via environment variable:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="JSON_SECRETS/project-loqui-xxxx.json"
```

4. Run the test script:
```bash
python main.py
```

## 📊 Evaluation Metrics

- **Word Error Rate (WER)**
- **Character Error Rate (CER)**
- **Semantic Similarity (BERTScore)**
- **Punctuation and Named Entity Consistency**

## 👥 Team Members

- Kennedy Onyema-Willys
- Harshita Koppaka
- Jolly Thomas
- Ore Akinbola

## 📄 License

This project is licensed under the MIT License.
