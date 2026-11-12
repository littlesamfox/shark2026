import pyautogui
import pygetwindow as gw
from time import sleep

largura = int(input("Largura (px): "))
altura  = int(input("Altura (py): "))

pyautogui.FAILSAFE = True
LADO = 200

print("A iniciar em 3 segundos...")
print(">> MINIMIZA o PyCharm agora! <<\n")
sleep(3)

# Passo 1 — Abrir Paint
print("Passo 1: A abrir Paint...")
pyautogui.hotkey('win', 'r')
sleep(0.5)
pyautogui.write('mspaint', interval=0.05)
pyautogui.press('enter')
sleep(2.0) 

# Passo 2 — Maximizar a Janela
print("Passo 2: A forçar o Paint em ecrã inteiro...")
janelas_paint = gw.getWindowsWithTitle('Paint')
if janelas_paint:
    paint_app = janelas_paint[0]
    try:
        if not paint_app.isMaximized:
            paint_app.maximize()
        paint_app.activate()
    except Exception as e:
        pass
sleep(1.0)

# ── A MAGIA ACONTECE AQUI ──────────────────────────────────
print("\n" + "═"*50)
print("🎯 ATENÇÃO: Mexe o teu rato e coloca-o no meio da FOLHA BRANCA!")
print("Não cliques em nada, só deixa o rato lá parado.")
print("Vou capturar a posição em:")

# Contagem decrescente de 5 segundos
for i in range(5, 0, -1):
    print(f"{i}...")
    sleep(1.0)

# O Python vai ler exatamente onde deixaste o ponteiro do rato!
X_INICIO, Y_INICIO = pyautogui.position()
print(f"✓ Posição capturada: X={largura}, Y={altura}")
print("═"*50 + "\n")
# ─────────────────────────────────────────────────────────

# Passo 3 — Desenhar quadrado a partir do ponto que tu escolheste
print("Passo 3: A desenhar o quadrado...")
x, y, l = X_INICIO, Y_INICIO, LADO

# 1. Clique inicial para ativar o pincel nesse sítio
pyautogui.click(x, y)
sleep(0.3)

# 2. Desenhar o quadrado
pyautogui.moveTo(x, y)
pyautogui.dragTo(x + l, y,     duration=0.5, button='left') # Topo
pyautogui.dragTo(x + l, y + l, duration=0.5, button='left') # Lado Direito
pyautogui.dragTo(x, y + l,     duration=0.5, button='left') # Base
pyautogui.dragTo(x, y,         duration=0.5, button='left') # Lado Esquerdo

print("\n✓ Quadrado desenhado no sítio exato que escolheste!")
print("\n✓ Quadrado 200×200px desenhado!")
print("Próximo: ex04b para pintar o quadrado de cor.")

# ── DESAFIO ────────────────────────────────────────────────
# Desenha um rectângulo com dimensões personalizadas:
#   largura = int(input("Largura (px): "))
#   altura  = int(input("Altura (px): "))
