from PIL import Image
import pyscreeze
import pyautogui

captura = pyautogui.screenshot()
print("Funcionou! Tamanho da captura:", captura.size)