import os
import pyautogui
from time import sleep

# ═══════════════════════════════════════════════════════════
# EXERCÍCIO 03A — Desafio
# ═══════════════════════════════════════════════════════════

pyautogui.FAILSAFE = True

print(">> Tem 15 segundos para escrever <<\n")

# Desafio — pedir as 3 frases antes do sleep(3)
f1 = input("Frase 1: ")
f2 = input("Frase 2: ")
f3 = input("Frase 3: ")

print("\nA iniciar em 3 segundos...")
sleep(3)

# Passo 1 — Abrir Bloco de Notas com Win+R
print("Passo 1: A abrir Bloco de Notas...")
pyautogui.hotkey('win', 'r')
sleep(0.8)
pyautogui.write('notepad', interval=0.05)
pyautogui.press('enter')
sleep(1.5)

# Passo 2 — Escrever as 3 linhas
print("Passo 2: A escrever texto...")

linhas = [f1, f2, f3]

for linha in linhas:
    pyautogui.write(linha, interval=0.05)
    pyautogui.press('enter')
    sleep(0.2)

# Passo 3 — Guardar como aula03.txt
print("Passo 3: A pedir para Guardar Como...")

# WINDOWS 11
pyautogui.press('right')
sleep(0.2)
pyautogui.hotkey('ctrl', 'shift', 'd')

# WINDOWS 10
# pyautogui.hotkey('ctrl', 'shift', 's')

sleep(2.0)

print("A escrever o nome aula03.txt...")
pyautogui.write('aula03.txt', interval=0.05)
sleep(0.5)
pyautogui.press('enter')
sleep(1.0)

# Proteção "Ficheiro já existe"
pyautogui.press('right')
sleep(0.2)
pyautogui.press('enter')
sleep(1.5)

# Passo 4 — Fechar
print("Passo 4: A fechar...")
os.system("taskkill /f /im notepad.exe")

print("\n✓ SUCESSO! O ficheiro aula03.txt foi guardado!")
print("Próximo: ex03b para adicionar texto com acentos.")

# ── DESAFIO ────────────────────────────────────────────────
# Pede 3 frases ao utilizador ANTES do sleep(3):
#   f1 = input("Frase 1: ")
#   f2 = input("Frase 2: ")
#   f3 = input("Frase 3: ")
# Depois escreve-as no Bloco de Notas.