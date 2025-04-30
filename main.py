from modules.voice_input import listen
from modules.text_to_speech import speak
from modules.command_parser import parse_command

def main():
    speak("Hello, I am Raagi. How can I help you?")
    
    while True:
        text = listen()
        print(f"🎤 You said: {text}")  # Print what was recognized
        if not text:
            continue

        command = parse_command(text)
        print(f"Command parsed: {command}")  # Print parsed command for debugging

        if command == "open_youtube":
            speak("Opening YouTube...")
        elif command == "open_google":
            speak("Opening Google...")
        elif command == "exit":
            speak("Goodbye!")
            break  # Exit the loop and stop the program
        else:
            speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    main()
