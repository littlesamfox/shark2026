import pyautogui
from time import sleep
from datetime import datetime

# Coordenadas dos píxeis a monitorizar
pontos = [(100, 100), (500, 300), (960, 540)]

INTERVALO = 0.2
TOLERANCIA = 25
CONFIRMACOES = 2

def diferenca_cor(cor1, cor2):
    return max(abs(a - b) for a, b in zip(cor1, cor2))

# Guardar as cores iniciais e os candidatos a alteração
cores_estaveis = {
    ponto: pyautogui.pixel(*ponto)
    for ponto in pontos
}

contagens = {ponto: 0 for ponto in pontos}

for ponto, cor in cores_estaveis.items():
    print(f"Píxel {ponto}: cor inicial {cor}")

print("\nA monitorizar... Pressiona Ctrl+C para parar.\n")


# ── DESAFIO ────────────────────────────────────────────────
# Monitoriza 3 píxeis em simultâneo:
#   pontos = [(x1,y1), (x2,y2), (x3,y3)]
#   while True:
#       for px, py in pontos:
#           if <mudou>:
#               print(f"Mudança em ({px},{py})!")
#       sleep(0.5)