# 01C - Mover o rato e renomear (resumo da sequencia)
import os
import time
import pyautogui
import pyperclip
import pygetwindow as gw

desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")

time.sleep(3) # tempo obrigatorio para minimizar o editor
pyautogui.hotkey("win", "r")
pyperclip.copy(desktop)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

# Poll for the Explorer window with a timeout to avoid IndexError when
# getWindowsWithTitle returns an empty list (e.g., timing or different monitor)
timeout = 10  # seconds
end_time = time.time() + timeout
janela = None
while time.time() < end_time:
    wins = gw.getWindowsWithTitle("Ambiente de trabalho")
    if wins:
        janela = wins[0]
        break
    time.sleep(0.5)
if janela is None:
    raise RuntimeError(f"No window titled 'Desktop' found within {timeout} seconds. Available titles: {gw.getAllTitles()}")
janela.activate()
pyautogui.write("fich") # type-ahead para selecionar o ficheiro
pyautogui.press("f2")
pyautogui.hotkey("ctrl", "a")
pyperclip.copy("ficheiro_renomeado")

pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
pyautogui.hotkey("alt", "f4")

# 01D - Abrir ficheiro e escrever conteudo
import datetime

caminho_novo = os.path.join(desktop, "ficheiro_renomeado.txt")

if not os.path.exists(caminho_novo):
    print("Completa o 01C primeiro!")
else:
    os.startfile(caminho_novo)
    time.sleep(3)
    pyautogui.hotkey("ctrl", "home")
    linhas = ["Ficheiro criado automaticamente", str(datetime.datetime.now())]
    for linha in linhas:
        pyautogui.write(linha)
        pyautogui.press("enter")
    pyautogui.hotkey("ctrl", "s")
    time.sleep(1)
    os.system("taskkill /f /im notepad.exe")


