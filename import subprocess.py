import subprocess
import sys

print("Python utilizado:", sys.executable)

subprocess.check_call([
    sys.executable, "-m", "pip", "install", "--upgrade",
    "Pillow", "pyscreeze", "pyautogui"
])