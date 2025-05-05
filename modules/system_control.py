# modules/system_control.py
import pyautogui
import datetime
import os

def take_screenshot():
    # Get the current date and time to create a unique file name
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"screenshot_{timestamp}.png"

    # Specify the custom path for the "Screenshots" folder
    screenshots_path = r"C:\Users\DELL\Pictures\Screenshots"
    
    # Ensure the folder exists
    if not os.path.exists(screenshots_path):
        os.makedirs(screenshots_path)

    # Take the screenshot and save it to the specified folder
    screenshot = pyautogui.screenshot()
    screenshot.save(os.path.join(screenshots_path, file_name))
    
    # Return a response message for the assistant to speak
    return "Your screenshot is saved, sir."
