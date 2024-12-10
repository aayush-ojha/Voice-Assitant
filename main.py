import sounddevice as sd
import numpy as np
import pyttsx3
import datetime
import webbrowser
import speech_recognition as sr
import os

def initialize_engine():
    """Initialize the text-to-speech engine"""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)   
    return engine

def speak(engine, text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for voice input"""
    recognizer = sr.Recognizer()
    samplerate = 16000  
    duration = 5

    print("Listening...")
    recording = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()  
    audio_data = np.squeeze(recording)

    
    audio = sr.AudioData(audio_data.tobytes(), samplerate, 2)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return "Sorry, I couldn't reach the recognition service."

def process_command(command):
    """Process voice commands"""
    if "time" in command:
        return datetime.datetime.now().strftime("%I:%M %p")
    elif "date" in command:
        return datetime.datetime.now().strftime("%B %d, %Y")
    elif "search" in command:
        search_term = command.replace("search", "")
        webbrowser.open(f"https://www.google.com/search?q={search_term}")
        return f"Searching for {search_term}"
    elif "open" in command:
        file_path = command.replace("open", "").strip()
        try:
            os.system(f'xdg-open "{file_path}"')
            return f"Opening {file_path}"
        except Exception as e:
            return f"Could not open {file_path}: {e}"
    elif "exit" in command:
        return "goodbye"
    else:
        return "I didn't understand that command"

def main():
    engine = initialize_engine()
    speak(engine, "Hello, I'm your voice assistant. How can I help?")
    
    while True:
        command = listen()
        if command:
            response = process_command(command)
            speak(engine, response)
            if response == "goodbye":
                break

if __name__ == "__main__":
    main()