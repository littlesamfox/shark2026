import pyautogui
import pygetwindow as gw
from time import sleep

pyautogui.FAILSAFE = True

LARG, ALT = pyautogui.size()
MARGEM = 10
ROW_ALT = (ALT - MARGEM * 3 - 80) // 3
ROW_LARG = LARG - MARGEM * 2

APPS = [
    ("notepad", ["Notepad", "Bloco de Notas", "Untitled"]),
    ("mspaint", ["Paint", "Sem título"])
]

print(f"Ecrã: {LARG}×{ALT}px")
print(f"Layout: 2 linhas de {ROW_LARG}×{ROW_ALT}px")
print("A iniciar em 3 segundos...")
print(">> MINIMIZA o PyCharm agora! <<")

sleep(3)

# Passo 1 — Abrir aplicações
for cmd, _ in APPS:
    print(f"A abrir {cmd}...")
    pyautogui.hotkey('win', 'r')
    sleep(0.8)
    pyautogui.write(cmd, interval=0.05)
    pyautogui.press('enter')
    sleep(1.5)

sleep(1)

# Passo 2 — Definir posições (uma em cima da outra)
posicoes = [
    (MARGEM, MARGEM),
    (MARGEM, MARGEM + ROW_ALT + MARGEM)
]

print("\nA organizar janelas...")
posicionadas = []

for i, (cmd, titulos) in enumerate(APPS):

    x, y = posicoes[i]

    janela = None

    for titulo in titulos:
        resultados = gw.getWindowsWithTitle(titulo)
        if resultados:
            janela = resultados[0]
            break

    if janela is None:
        print(f"⚠ {cmd} não encontrado")
        continue

    try:
        janela.restore()
        sleep(0.3)

        janela.activate()
        sleep(0.3)

        janela.moveTo(x, y)
        sleep(0.3)

        janela.resizeTo(ROW_LARG, ROW_ALT)
        sleep(0.3)

        posicionadas.append(cmd)

        print(f"✓ {cmd} → posição ({x},{y})")

    except Exception as e:
        print(f"⚠ Erro com {cmd}: {e}")

print(f"\n✓ {len(posicionadas)}/2 aplicações organizadas!")
print("Layout vertical concluído!")