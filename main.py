from modules.voice_input import listen_for_commands as listen
from modules.text_to_speech import speak
from modules.command_parser import parse_command
import webbrowser
import time

def main():
    speak("Hello, I am Raagi. How can I help you?")
    
    while True:
        text = listen()
        print(f"🎤 You said: {text}")
        if not text:
            continue

        command = parse_command(text)
        print(f"Command parsed: {command}")

        if command == "play_youtube":
            speak("Opening YouTube and playing your song...")
            # Extract song name after 'play'
            song_name = text.split("play")[-1].strip()  # Everything after 'play'
            search_query = "+".join(song_name.split())  # Join with '+' for the URL
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
        elif command == "open_google":
            speak("Opening Google...")
            webbrowser.open("https://www.google.com")
        elif command == "exit":
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    main()
