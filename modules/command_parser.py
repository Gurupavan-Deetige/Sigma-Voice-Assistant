def parse_command(text):
    text = text.lower()  # Convert input to lowercase for consistency
    
    # Check for the pattern "action [target]"
    if "play" in text:
        return "play_song"
    elif "open" in text:
        return "open_app_or_website"
    elif "take" in text and "screenshot" in text:
        return "take_screenshot"
    elif "run" in text:
        return "run_program"
    elif "exit" in text:
        return "exit"
    else:
        return "unknown"  # If the command doesn't match any known pattern
