def parse_command(text):
    # Convert text to lowercase to handle case-insensitive matching
    text = text.lower()
    
    # Define command keywords and map them to actions
    if "youtube" in text:
        return "open_youtube"
    elif "google" in text:
        return "open_google"
    elif "exit" in text or "quit" in text:
        return "exit"
    else:
        return "unknown"
