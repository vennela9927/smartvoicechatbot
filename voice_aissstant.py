import speech_recognition as sr
import pyttsx3
from llama_cpp import Llama

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set voice properties (Optional)
engine.setProperty('rate', 150)  # Speed of the speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

# Initialize the Llama model
llm = Llama(
    model_path="models/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    n_ctx=512,
    n_threads=4,  # Adjust based on your CPU
)

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            print(f"You: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            print("Sorry, there was an issue with the speech service.")
            return None

def speak(text):
    print(f"Bot: {text}")
    engine.say(text)
    engine.runAndWait()

print("🤖 Smart Voice Chatbot Ready! Say 'exit', 'quit', or 'bye' to quit.\n")

while True:
    prompt = listen()
    if prompt is None:
        continue
    elif prompt.lower() in ["exit", "quit", "bye"]:
        speak("Goodbye!")
        break
    full_prompt = f"[INST] {prompt} [/INST]"
    output = llm(full_prompt, max_tokens=100, stop=["</s>"])
    response = output["choices"][0]["text"].strip()
    speak(response)
