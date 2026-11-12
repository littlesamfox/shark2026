import os
import pyautogui
import pyperclip
from time import sleep
from datetime import datetime

# ═══════════════════════════════════════════════════════════
# EXERCÍCIO 03C — Adicionar Data e Hora (Corrigido para o teu PC)
# ═══════════════════════════════════════════════════════════

pyautogui.FAILSAFE = True

# ── 1. DETETIVE DE FICHEIROS ──────────────────────────────
u = os.environ["USERPROFILE"]
possiveis_caminhos = [
    os.path.join(u, "aula03.txt"), # Onde o ex03a guardou
    os.path.join(u, "OneDrive - sharkcoders", "Ambiente de Trabalho", "aula03.txt"),
    os.path.join(u, "OneDrive", "Ambiente de Trabalho", "aula03.txt"),
    os.path.join(u, "Desktop", "aula03.txt"),
    os.path.join(u, "Ambiente de Trabalho", "aula03.txt"),
    os.path.join(u, "Documents", "aula03.txt"),
]

caminho = next((c for c in possiveis_caminhos if os.path.exists(c)), None)

if not caminho:
    print("\n⚠ aula03.txt não encontrado em lado nenhum!")
    print("  Completa o ex03a primeiro.")
    exit()

print(f"✓ Ficheiro encontrado em: {caminho}")
# ─────────────────────────────────────────────────────────

# Calcular data e hora ANTES do sleep(3)
agora     = datetime.now()
data_hora = agora.strftime('%d/%m/%Y às %H:%M:%S')
dia_semana = agora.strftime('%A')
traducoes = {
    'Monday':'Segunda-feira','Tuesday':'Terça-feira','Wednesday':'Quarta-feira',
    'Thursday':'Quinta-feira','Friday':'Sexta-feira','Saturday':'Sábado','Sunday':'Domingo'
}
dia_pt = traducoes.get(dia_semana, dia_semana)

print(f"Data/hora calculada: {data_hora} ({dia_pt})")
print("\nA iniciar em 3 segundos...")
print(">> MINIMIZA o PyCharm agora! <<\n")
sleep(3)

# Abrir aula03.txt
print("Passo 1: A abrir aula03.txt...")
pyautogui.hotkey('win', 'r')
sleep(0.8)
pyperclip.copy(caminho)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(1.5) # Um bocadinho mais de tempo para garantir que abre

# Ir para o fim
print("Passo 2: A posicionar cursor no fim...")
pyautogui.hotkey('ctrl', 'end')
sleep(0.3)
pyautogui.press('enter')

# Adicionar linha de separação e data/hora
print("Passo 3: A escrever data e hora...")
pyperclip.copy('--- Data e Hora Automáticas ---')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(0.2)

pyperclip.copy(f'Editado em: {data_hora}')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(0.2)

pyperclip.copy(f'Dia da semana: {dia_pt}')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(0.2)

# O ano atual menos 2026 (assumindo que o exercício começa este ano)
pyperclip.copy(f'Este ficheiro tem {agora.year - 2026} anos de vida.')
pyautogui.hotkey('ctrl', 'v')
sleep(0.5)

# Guardar e fechar COM SEGURANÇA
print("Passo 4: A guardar e fechar...")
# Usamos o Ctrl+G da tua foto para Guardar
#pyautogui.hotkey('ctrl', 'g')

# No Windows 10, Ctrl+S
pyautogui.hotkey('ctrl', 's')

sleep(2.0) # Dá tempo ao disco para guardar

# Usamos o taskkill em vez do Alt+F4
#os.system("taskkill /f /im notepad.exe")

#fecha o separador
pyautogui.hotkey('ctrl', 'w')
sleep(0.5)

print(f"\n✓ Data e hora adicionadas: {data_hora}")
print("Próximo: ex03d para ler, contar e reescrever o ficheiro.")

# ── DESAFIO ────────────────────────────────────────────────
# Adiciona uma contagem decrescente:
#   for i in range(5, 0, -1):
#       pyperclip.copy(f'  {i}...')
#       pyautogui.hotkey('ctrl', 'v')
#       pyautogui.press('enter')
#       sleep(0.1)
#   pyperclip.copy('  🚀 Lançamento!')
#   pyautogui.hotkey('ctrl', 'v')