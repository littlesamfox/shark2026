#Aula 03 - Teclado Avancado - demo do professor
import pyautogui
import pyperclip
import os
import time
from datetime import datetime

# 1. Abrir o Bloco de Notas so com o teclado (Win+R e mais fiavel que um icone)
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write('notepad')
pyautogui.press('enter')
time.sleep(1)

# 2. Escrever texto simples (sem acentos, o write() nao os sabe escrever)
pyautogui.press("esc")

time.sleep(5)  # Durante estes 5 segundos, coloca o rato na área de texto
pyautogui.click()
pyautogui.write('Ola, isto e um teste do teclado.', interval=0.1)
pyautogui.press('enter')

# 3. Escrever texto COM acentos usando pyperclip
pyperclip.copy('Parabéns, já sabes usar o teclado avancado!')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

# 4. Calcular a data e hora ANTES do sleep(3), nunca depois
agora = datetime.now()
data_hora = agora.strftime('%d/%m/%Y %H:%M')
pyperclip.copy('Editado em: ' + data_hora)
pyautogui.hotkey('ctrl', 'v')

# 5. Guardar como 
input('Prime ENTER quando estiveres pronto para guardar...')
time.sleep(5)

pyautogui.hotkey('ctrl', 'shift', 's')
time.sleep(3)

pyautogui.hotkey('ctrl', 'a')
pyautogui.write('aula03.txt', interval=0.05)
pyautogui.press('enter')

# Espera pela gravação
time.sleep(2)