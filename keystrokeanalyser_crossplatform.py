
import os
import platform
from datetime import datetime
from pynput import keyboard

try:
    from PIL import ImageGrab
except ImportError:
    ImageGrab = None

# Settings
LOG_DIR = "logs"
SCREENSHOT_DIR = os.path.join(LOG_DIR, "screenshots")
LOG_FILE = os.path.join(LOG_DIR, "keystroke_log.txt")
CORRECT_PASSWORD = "admin123"

typed_chars = []

# Create directories
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def log(text):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")

def take_screenshot(label="attempt"):
    if ImageGrab is None:
        log("[WARNING] PIL.ImageGrab not available – screenshot not taken.")
        return "Screenshot not supported"
    if platform.system() == "Linux":
        log("[WARNING] Screenshot not supported on Linux without X11 – skipped.")
        return "Screenshot not supported on Linux"
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = os.path.join(SCREENSHOT_DIR, f"{label}_{timestamp}.png")
    try:
        ImageGrab.grab().save(path)
        return path
    except Exception as e:
        log(f"[ERROR] Screenshot failed: {e}")
        return "Screenshot failed"

def on_press(key):
    global typed_chars
    try:
        if key == keyboard.Key.enter:
            entered_password = ''.join(typed_chars)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log(f"[{timestamp}] Entered: {entered_password}")

            if entered_password == CORRECT_PASSWORD:
                log(f"[{timestamp}] ✅ Access Granted")
                print("Access Granted ✅")
            else:
                log(f"[{timestamp}] ❌ Wrong Password")
                screenshot_path = take_screenshot(label="wrong_attempt")
                log(f"[{timestamp}] 📸 Screenshot Saved: {screenshot_path}")
                print("Wrong Password ❌ – Screenshot Taken")

            typed_chars = []

        elif key == keyboard.Key.backspace:
            if typed_chars:
                typed_chars.pop()
        elif hasattr(key, 'char') and key.char is not None:
            typed_chars.append(key.char)

    except Exception as e:
        log(f"[ERROR] {str(e)}")

# Start key listener
print("🔐 KeystrokeAnalyser is running (unlimited attempts, cross-platform)...")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
