import speech_recognition as sr

def listen_for_commands():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        print("Listening for commands...")
        audio = recognizer.listen(source)

    try:
        # Use pocketsphinx for offline recognition
        command = recognizer.recognize_sphinx(audio)
        print(f"Command recognized: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return None
    except sr.RequestError:
        print("Speech recognition service unavailable.")
        return None
