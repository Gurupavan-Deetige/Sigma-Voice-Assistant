import webbrowser
import os
import subprocess
from modules.voice_input import listen_for_commands as listen
from modules.text_to_speech import speak
from modules.command_parser import parse_command
from modules.system_control import take_screenshot

def main():
    greeting = "Hello Sir, I am Sigma Version 1.0, ready to assist with your tasks."
    speak(greeting)
    print(f"🎤 Assistant: {greeting}")

    while True:
        text = listen()  # Listen for the user's command
        print(f"🎤 You said: {text}")
        if not text:
            continue

        command = parse_command(text)  # Parse the command from the input text
        print(f"Command parsed: {command}")

        if command == "play_song":
            song_name = text.split("play")[-1].strip()
            speak(f"Playing {song_name}...")
            search_query = "+".join(song_name.split())
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
        elif command == "open_app_or_website":
            app_or_website = text.split("open")[-1].strip()
            speak(f"Opening {app_or_website}...")
            webbrowser.open(f"https://{app_or_website}.com")
        elif command == "take_screenshot":
            speak("Taking the screenshot now...")
            screenshot_message = take_screenshot()  # Trigger screenshot function
            speak(screenshot_message)  # Feedback after screenshot
        elif command == "run_program":
            filename = text.split("run")[-1].strip()
            speak(f"Running {filename}...")
            result = run_program(filename)  # Trigger function to run program
            speak(result)
        elif command == "exit":
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that.")

def run_program(filename):
    try:
        executable = filename.split(".")[0]
        if os.path.exists(executable):
            subprocess.run(f"./{executable}", shell=True)
            return f"{filename} ran successfully!"
        else:
            return "Executable not found. Please compile the file first."
    except subprocess.CalledProcessError:
        return "Error running the program."

if __name__ == "__main__":
    main()
