# modules/command_parser.py
from modules.system_control import take_screenshot

def parse_command(text):
    text = text.lower()
    
    # Define command keywords and map them to actions
    if "youtube" in text and "play" in text:
        return "play_youtube"
    elif "google" in text:
        return "open_google"
    elif "exit" in text or "quit" in text:
        return "exit"
    elif "take screenshot" in text:
        return take_screenshot()  # Call the screenshot function from system_control
    else:
        return "unknown"
