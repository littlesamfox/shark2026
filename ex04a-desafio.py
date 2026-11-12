import pyautogui
import pygetwindow as gw
from time import sleep

largura = int(input("Largura (px): "))
altura = int(input("Altura (px): "))

pyautogui.FAILSAFE = True

print("A iniciar em 3 segundos...")
print(">> MINIMIZA o PyCharm agora! <<\n")
sleep(3)

# Passo 1 — Abrir Paint
print("Passo 1: A abrir Paint...")
pyautogui.hotkey('win', 'r')
sleep(0.5)
pyautogui.write('mspaint', interval=0.05)
pyautogui.press('enter')
sleep(2)

# Passo 2 — Maximizar a janela
print("Passo 2: A maximizar o Paint...")
janelas_paint = gw.getWindowsWithTitle('Paint')

if janelas_paint:
    paint_app = janelas_paint[0]
    try:
        if not paint_app.isMaximized:
            paint_app.maximize()
        paint_app.activate()
    except Exception:
        pass

sleep(1)

# Passo 3 — Escolher o ponto inicial
print("\nColoca o rato dentro da folha branca.")
print("Nao cliques. Tens 5 segundos!")

for i in range(5, 0, -1):
    print(f"{i}...")
    sleep(1)

x, y = pyautogui.position()

print(f"Posicao inicial: X={x}, Y={y}")

# Passo 4 — Desenhar o retangulo
print("A desenhar o quadrado...")

pyautogui.moveTo(x, y)
pyautogui.dragTo(
    x + largura, y,
    duration=0.5,
    button='left'
)
pyautogui.dragTo(
    x + largura, y + altura,
    duration=0.5,
    button='left'
)
pyautogui.dragTo(
    x, y + altura,
    duration=0.5,
    button='left'
)
pyautogui.dragTo(
    x, y,
    duration=0.5,
    button='left'
)

print(f"Retangulo de {largura} x {altura} px desenhado!")