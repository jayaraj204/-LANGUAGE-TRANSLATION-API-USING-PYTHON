# 🌍 Language Translation API Using Python with Integrated Speech Recognition

## 📌 Overview
This project is a Python-based **Language Translation API** that integrates **speech recognition** and **text-to-speech (TTS)** technologies.  
Developed in 2023 by **Jayaraj**, the system enables **real-time translation** of spoken language into multiple target languages, offering both **textual and auditory outputs**.

The pipeline:
1. Capture voice input via microphone 🎙️  
2. Recognize and transcribe speech into text 📝  
3. Translate text into the selected target language 🌐  
4. Convert translated text into natural-sounding audio 🔊  

This makes it a **responsive multilingual communication tool** useful for accessibility, education, and cross-cultural communication.

---

## 🎯 Objectives
- Capture real-time spoken input via microphone  
- Translate speech into multiple languages accurately  
- Provide synthesized audio output for translated speech  
- Enhance accessibility and cross-lingual communication  

---

## 🛠️ Technologies Used
- **Python**
- **SpeechRecognition** – for capturing and transcribing voice input  
- **Googletrans / Deep-translator** – for translation  
- **gTTS (Google Text-to-Speech)** – for speech synthesis  
- **PyAudio** – for real-time microphone input  

---

## 🚀 Features
- 🎙️ Real-time speech recognition  
- 🌐 Translation into multiple target languages  
- 🔊 Audio output in a synthesized female voice  
- ⚡ Lightweight, modular, and scalable design  
- 🛡️ Built-in error handling for noisy inputs  

---

## 📂 Project Structure
```bash
📦 language-translation-api/
├── 📂 audio/
│   └── recorded_input.wav          # Captured speech input
├── 📂 scripts/
│   └── translator.py               # Main translation script
├── 📂 output/
│   └── translated_speech.mp3       # Generated translated audio
└── 📄 README.md                    # Project documentation
