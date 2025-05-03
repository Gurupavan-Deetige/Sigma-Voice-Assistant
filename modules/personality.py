import pyttsx3

def greet_user():
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech (words per minute)
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

    # Set voice (optional)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # 0 for male, 1 for female

    # The greeting message
    greeting = "Hello Sir, I am Sigma Version 1.0."

    # Speak the greeting
    engine.say(greeting)
    engine.runAndWait()
