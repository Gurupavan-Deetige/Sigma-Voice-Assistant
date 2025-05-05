# main.py
from modules.voice_input import listen_for_commands as listen
from modules.text_to_speech import speak
from modules.command_parser import parse_command
import webbrowser
import time
from modules.system_control import take_screenshot  # Import the screenshot function

def main():
    greeting = "Hello Sir, I am Sigma Version 1.0."
    speak(greeting)
    print(f"🎤 Assistant: {greeting}")

    while True:
        text = listen()  # Listen for the user's command
        print(f"🎤 You said: {text}")
        if not text:
            continue

        command = parse_command(text)  # Parse the command from the input text
        print(f"Command parsed: {command}")

        if command == "play_youtube":
            speak("Opening YouTube and playing your song...")
            song_name = text.split("play")[-1].strip()
            search_query = "+".join(song_name.split())
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
            time.sleep(2)
            webbrowser.open(f"https://www.youtube.com/watch?v={get_first_video_id(search_query)}")
        elif command == "open_google":
            speak("Opening Google...")
            webbrowser.open("https://www.google.com")
        elif command == "exit":
            speak("Goodbye!")
            break
        elif command == "take_screenshot":  # Handle screenshot command
            speak("Taking the screenshot now...")
            screenshot_message = take_screenshot()  # Trigger screenshot function
            speak(screenshot_message)  # Speak the result after screenshot is taken
        else:
            speak("Sorry, I didn't understand that.")

def get_first_video_id(query):
    return "dQw4w9WgXcQ"  # Placeholder for the video ID

if __name__ == "__main__":
    main()
