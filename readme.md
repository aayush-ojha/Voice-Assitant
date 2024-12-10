# Voice Assistant

This is a simple voice assistant built using Python. It can recognize voice commands, respond with text-to-speech, and perform various tasks such as telling the time, date, searching the web, and opening files.

## Features

- Recognizes voice commands using `speech_recognition`
- Responds with text-to-speech using `pyttsx3`
- Tells the current time and date
- Performs Google searches
- Opens files and directories on your system
- Prints recognized voice input to the terminal

## Requirements

- Python 3.6+
- `sounddevice`
- `numpy`
- `pyttsx3`
- `speech_recognition`
- `webbrowser`
- `os`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/aayush-ojha/voice-assistant.git
    cd voice-assistant
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install sounddevice numpy pyttsx3 speechrecognition
    ```

4. Install system dependencies:
    ```bash
    sudo apt update
    sudo apt install espeak
    ```

## Usage

1. Run the voice assistant:
    ```bash
    python3 main.py
    ```

2. Speak one of the supported commands:
    - "What time is it?"
    - "What's the date today?"
    - "Search for Python programming"
    - "Open /path/to/your/file"
    - "Exit"

## Example Commands

- "What time is it?"
- "What's the date today?"
- "Search for Python programming"
- "Open /home/user/Documents"
- "Exit"

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [speech_recognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [sounddevice](https://pypi.org/project/sounddevice/)