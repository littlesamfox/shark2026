import os
import pyautogui
import pyperclip
from time import sleep

# ═══════════════════════════════════════════════════════════
# EXERCÍCIO 03B — Escrever com Acentos (Corrigido)
# ═══════════════════════════════════════════════════════════

pyautogui.FAILSAFE = True

# ── 1. DETETIVE DE FICHEIROS ──────────────────────────────
# Vamos procurar o ficheiro em todos os sítios onde ele pode estar!
u = os.environ["USERPROFILE"]
possiveis_caminhos = [
    os.path.join(u, "aula03.txt"), # Onde o ex03a guardou (pasta almad)
    os.path.join(u, "OneDrive - sharkcoders", "Ambiente de Trabalho", "aula03.txt"),
    os.path.join(u, "OneDrive", "Ambiente de Trabalho", "aula03.txt"),
    os.path.join(u, "Desktop", "aula03.txt"),
    os.path.join(u, "Documents", "aula03.txt"),
]

# Procura um por um. O primeiro que existir, ele guarda no 'caminho'
caminho = next((c for c in possiveis_caminhos if os.path.exists(c)), None)

if not caminho:
    print("\n⚠ aula03.txt não encontrado em lado nenhum!")
    print("  Completa o ex03a primeiro.")
    exit()

print(f"✓ Ficheiro encontrado em: {caminho}")
# ─────────────────────────────────────────────────────────

# input() ANTES do sleep(3)!
nome = input("Qual é o teu nome? ")

print("\nA iniciar em 3 segundos...")
print(">> MINIMIZA o PyCharm agora! <<\n")
sleep(3)

# Abrir aula03.txt via Win+R
print("Passo 1: A abrir aula03.txt...")
pyautogui.hotkey('win', 'r')
sleep(0.8)
# pyperclip.copy resolve o problema das barras e espaços no caminho!
pyperclip.copy(caminho)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(1.5) # Tempo extra para o Notepad abrir

# Ir para o fim do texto existente
print("Passo 2: A posicionar cursor no fim...")
pyautogui.hotkey('ctrl', 'end')
sleep(0.3)
pyautogui.press('enter')

# Escrever com acentos usando pyperclip
print("Passo 3: A escrever com acentos...")
pyperclip.copy('--- Acentos com pyperclip ---')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(0.2)

pyperclip.copy('Parabéns a você!')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(0.2)

mensagem = f'Olá, {nome}! Bem-vindo ao PyAutoGui.'
pyperclip.copy(mensagem)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(0.2)

pyperclip.copy('Feito com Python + pyperclip!')
pyautogui.hotkey('ctrl', 'v')
sleep(0.5)

# Guardar e fechar com segurança
print("Passo 4: A guardar e fechar...")
# Como vimos na tua foto, o atalho para Guardar (atualizar um ficheiro existente) é Ctrl+G
#pyautogui.hotkey('ctrl', 'g')

# No Windows 10, usamos Ctrl+S
pyautogui.hotkey('ctrl', 's')

sleep(2.0) # Tempo para o disco gravar

# Confirmar que o texto foi realmente gravado no disco
with open(caminho, "r", encoding="utf-8-sig") as ficheiro:
    texto_guardado = ficheiro.read()

if mensagem in texto_guardado:
    print(f"\n✓ Alterações gravadas em: {caminho}")

    # Fechar apenas o separador actual, sem terminar à força
    pyautogui.hotkey('ctrl', 'w')
else:
    print("\n⚠ As alterações NÃO foram gravadas.")
    print("O Notepad ficará aberto para poderes guardar manualmente.")

# O nosso método à prova de falhas para fechar
#os.system("taskkill /f /im notepad.exe")

print(f"\n✓ Acentos adicionados para {nome}!")
print("Próximo: ex03c para adicionar data e hora automáticas.")

# ── DESAFIO ────────────────────────────────────────────────
# Escreve um poema com acentos usando ciclo for:
#   linhas = [
#       'Era uma vez um programador...',
#       'Que aprendeu PyAutoGui com paixão,',
#       'Controlou o rato e o teclado,',
#       'E automatizou tudo com precisão!'
#   ]
#   for linha in linhas:
#       pyperclip.copy(linha)
#       pyautogui.hotkey('ctrl', 'v')
#       pyautogui.press('enter')
#       sleep(0.2)