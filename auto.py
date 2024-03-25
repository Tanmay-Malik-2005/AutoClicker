import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# Define initial default values
default_settings = {'hotkey': 'z', 'clicks': 1, 'interval': 0.01}

def read_settings():
    """Reads the settings from the file."""
    settings = default_settings.copy()  # Start with default values
    try:
        with open('settings.txt', 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                settings[key] = value  # Store settings as string
    except FileNotFoundError:
        print("Settings file not found, using default settings.")
    # Convert settings to appropriate types
    settings['clicks'] = int(settings['clicks'])
    settings['interval'] = float(settings['interval'])
    return settings

# Read initial settings
settings = read_settings()
mouse = Controller()
activated = False

def do_click(mouse_controller, clicks, interval):
    """Perform the actual click action."""
    for _ in range(clicks):
        mouse_controller.click(Button.left)
        time.sleep(interval)

def click_worker():
    """Background thread function to handle clicks."""
    while True:
        if activated:
            local_settings = read_settings()  # Read settings in case they have been updated
            do_click(mouse, local_settings['clicks'], local_settings['interval'])

threading.Thread(target=click_worker, daemon=True).start()

def on_press(key):
    """Handle key press to toggle clicking."""
    global activated
    local_settings = read_settings()  # Read settings for the latest hotkey
    try:
        if key == KeyCode(char=local_settings['hotkey']):
            activated = not activated
    except AttributeError:
        pass  # In case of special keys that do not have a char attribute

listener = Listener(on_press=on_press)
listener.start()

# Keep the script running
input("Press Enter to stop...\n")
