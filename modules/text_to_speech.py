import pyttsx3

def speak(text):
    try:
        engine = pyttsx3.init()
        print(f"Speaking: {text}")
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error with text-to-speech: {e}")
        print(f"Fallback output: {text}")
