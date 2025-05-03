from modules.voice_input import listen_for_commands as listen
from modules.text_to_speech import speak
from modules.command_parser import parse_command
import webbrowser
import time

def main():
    # Initialize greeting
    greeting = "Hello Sir, I am Sigma Version 1.0."
    speak(greeting)
    print(f"🎤 Assistant: {greeting}")
    
    while True:
        # Listen for user input
        text = listen()
        print(f"🎤 You said: {text}")
        if not text:
            continue

        # Parse the command
        command = parse_command(text)
        print(f"Command parsed: {command}")

        # Execute command
        if command == "play_youtube":
            speak("Opening YouTube and playing your song...")
            song_name = text.split("play")[-1].strip()
            search_query = "+".join(song_name.split())
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
            time.sleep(2)  # Wait for the page to load
            webbrowser.open(f"https://www.youtube.com/watch?v={get_first_video_id(search_query)}")
        elif command == "open_google":
            speak("Opening Google...")
            webbrowser.open("https://www.google.com")
        elif command == "exit":
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that.")

def get_first_video_id(query):
    """Fetches the video ID of the first YouTube search result."""
    # This function should implement logic to extract the first video ID
    # from the YouTube search results. For now, it returns a placeholder.
    return "dQw4w9WgXcQ"  # Replace with actual logic

if __name__ == "__main__":
    main()
