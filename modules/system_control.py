# modules/system_control.py

import pyautogui
import datetime
import os

def take_screenshot():
    # Get the current date and time to create a unique file name
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"screenshot_{timestamp}.png"
    
    # Create a directory to store screenshots if it doesn't exist
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    
    # Take the screenshot and save it in the screenshots directory
    screenshot = pyautogui.screenshot()
    screenshot.save(f"screenshots/{file_name}")
    
    return f"Screenshot saved as {file_name}"

# You can now call this function from anywhere in the project (like from the command_parser.py or main.py)
