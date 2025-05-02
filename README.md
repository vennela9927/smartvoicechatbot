# Mistral AI Voice Assistant

Welcome to the **Mistral AI Voice Assistant** project! This is a conversational voice assistant built using the **Mistral 7B Instruct** model that allows users to interact with the system via voice. The assistant listens to user commands, processes them, and responds in both text and speech.

## 📝 Project Overview

The Mistral AI Voice Assistant combines **Natural Language Processing (NLP)** and **Speech Processing** to create an intelligent voice assistant capable of real-time conversations. By integrating the **Mistral 7B Instruct** language model with speech recognition and text-to-speech (TTS) synthesis, the assistant provides a seamless voice-interactive experience.

## 🎯 Key Features

- **Speech-to-Text (STT)**: Converts speech into text using the `speech_recognition` library.
- **Text Generation**: Generates responses based on user input using the **Mistral 7B Instruct** model.
- **Text-to-Speech (TTS)**: Converts generated text responses into speech using `pyttsx3`.
- **Real-Time Interaction**: Interacts with users in real-time, processing voice commands and responding promptly.
- **Offline Functionality**: The system works offline, ensuring data privacy while providing a consistent user experience.

## ⚙️ Tech Stack

The Mistral AI Voice Assistant uses the following technologies:

- **Programming Language**: Python 3.12
- **Speech Recognition**: `speech_recognition` library for converting speech to text.
- **Text-to-Speech**: `pyttsx3` for converting text to speech.
- **Language Model**: **Mistral 7B Instruct** model loaded via `llama_cpp` for natural language generation.
- **Microphone Access**: `PyAudio` library for capturing microphone input.
- **Backend**: `llama-cpp-python` for interfacing with the Mistral model.

## 🚀 Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone <repository_url>
cd <repository_name>
```
### 2.Install Dependencies
Create a virtual environment to manage the project's dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
.\venv\Scripts\activate   # For Windows
```

### Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### Alternatively, you can install the libraries individually:
```bash
pip install llama-cpp-python speechrecognition pyttsx3 pyaudio
```

### 3. Run the Assistant
Once all dependencies are installed, you're ready to run the assistant. The Mistral 7B Instruct model file is already included in the repository, so you can skip the step of downloading it.

To start the assistant, run the following command:
```bash
python assistant.py
```

The assistant will begin listening to your voice input and provide responses through text and speech.


