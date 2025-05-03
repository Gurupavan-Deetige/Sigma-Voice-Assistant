def parse_command(text):
    text = text.lower()
    
    # Define command keywords and map them to actions
    if "youtube" in text and "play" in text:
        return "play_youtube"
    elif "google" in text:
        return "open_google"
    elif "exit" in text or "quit" in text:
        return "exit"
    else:
        return "unknown"
