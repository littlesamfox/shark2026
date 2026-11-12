
# ── IMPORTAÇÃO DE BIBLIOTECAS ──
import pyautogui
import math
from time import sleep

pyautogui.FAILSAFE = True

# ── CONFIGURAÇÃO ──
LADO = 200
RAIO = 40
PASSOS_EXTENDED = 100

print("=" * 55)
print("VAMOS DESENHAR NO PAINT!")
print("Resolução do ecrã: 1920 x 1080")
print("=" * 55)

sleep(2)

# ── 1. CAPTURA DAS COORDENADAS ──

print("PASSO 1: Coloca o rato no botão do PINCEL.")
for i in range(5, 0, -1):
    print(f"A gravar em {i}...")
    sleep(1)

X_PINCEL, Y_PINCEL = pyautogui.position()

print("PASSO 2: Coloca o rato no canto superior esquerdo do quadrado.")
for i in range(5, 0, -1):
    print(f"A gravar em {i}...")
    sleep(1)

X_INICIO, Y_INICIO = pyautogui.position()

# ── 2. COORDENADAS DAS FIGURAS ──

# Círculo à direita do quadrado
cx = X_INICIO + LADO + 70
cy = Y_INICIO + LADO // 2

# Triângulo abaixo do quadrado
tx = X_INICIO + LADO // 2
ty = Y_INICIO + LADO + 90

# Estrela à direita do círculo
ex = cx + RAIO * 2 + 35
ey = cy

# Verificar se as figuras cabem no ecrã
if (ex + RAIO >= 1920 or
    ty + RAIO >= 1080 or
    X_INICIO < 0 or Y_INICIO < 0):
    print("AVISO: Algumas figuras podem ficar fora do ecrã.")
    print("Reposiciona o quadrado e executa novamente.")
    raise SystemExit

# Selecionar o pincel
pyautogui.click(X_PINCEL, Y_PINCEL)
sleep(0.5)

# ── 3. DESENHAR CÍRCULO ──

print("A desenhar o círculo...")

pyautogui.moveTo(cx + RAIO, cy)
pyautogui.mouseDown()

for i in range(1, PASSOS_EXTENDED + 1):
    angulo = math.radians(360 * i / PASSOS_EXTENDED)
    px = cx + int(RAIO * math.cos(angulo))
    py = cy + int(RAIO * math.sin(angulo))
    pyautogui.moveTo(px, py, duration=0.01)

pyautogui.mouseUp()
sleep(0.3)

# ── 4. DESENHAR TRIÂNGULO ──

print("A desenhar o triângulo...")

v1 = (tx, ty - RAIO)
v2 = (tx - RAIO, ty + RAIO)
v3 = (tx + RAIO, ty + RAIO)

pyautogui.moveTo(*v1)
pyautogui.dragTo(*v2, duration=0.5)
pyautogui.dragTo(*v3, duration=0.5)
pyautogui.dragTo(*v1, duration=0.5)

sleep(0.3)

# ── 5. DESENHAR ESTRELA ──

print("A desenhar a estrela...")

pontos = []

for i in range(10):
    angulo = math.radians(-90 + i * 36)
    r = RAIO if i % 2 == 0 else RAIO * 0.45

    px = ex + int(r * math.cos(angulo))
    py = ey + int(r * math.sin(angulo))
    pontos.append((px, py))

pyautogui.moveTo(*pontos[0])

for ponto in pontos[1:] + [pontos[0]]:
    pyautogui.dragTo(*ponto, duration=0.3)

print("Círculo, triângulo e estrela desenhados!")