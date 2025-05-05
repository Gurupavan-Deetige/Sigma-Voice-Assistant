import speech_recognition as sr
from difflib import get_close_matches

def listen_for_commands():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... please wait")
        recognizer.adjust_for_ambient_noise(source, duration=2)  # longer duration
        print("Listening for commands... speak clearly")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"(Raw recognition): {text}")
        return correct_misheard(text.lower())
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return "Sorry, I couldn't connect to the recognition service."

def correct_misheard(text):
    expected = ["exit", "open google", "play", "play music", "youtube", "play youtube"]
    match = get_close_matches(text, expected, n=1, cutoff=0.5)
    return match[0] if match else text
