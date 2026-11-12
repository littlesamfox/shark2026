import os
import pyautogui
from time import sleep

def get_desktop():
    u = os.environ["USERPROFILE"]

    candidatos = [
        os.path.join(u, "OneDrive - sharkcoders", "Ambiente de Trabalho"),
        os.path.join(u, "OneDrive", "Ambiente de Trabalho"),
        os.path.join(u, "OneDrive - sharkcoders", "Desktop"),
        os.path.join(u, "OneDrive", "Desktop"),
        os.path.join(u, "Desktop"),
        os.path.join(u, "Ambiente de Trabalho"),
    ]

    return next((c for c in candidatos if os.path.exists(c)), u)


desktop = get_desktop()

print("═" * 60)
print(f"🖥️ Resolução do ecrã: {pyautogui.size()}")
print(f"📂 Pasta de destino: {desktop}")
print("═" * 60)

print("\nPrepara o ecrã que queres capturar...")
print("A primeira captura será feita em 2 segundos.\n")

for i in range(1, 4):
    sleep(2)
    imagem = pyautogui.screenshot()
    nome = f"screenshot_{i:02d}.png"
    caminho = os.path.join(desktop, nome)
    imagem.save(caminho)
    tamanho = os.path.getsize(caminho)

print("\n" + "═" * 60)
print("3 prints feitas")
print(f"Localização: {desktop}")
print("═" * 60)

os.startfile(desktop)

# ── DESAFIO ────────────────────────────────────────────────
# Tira 3 screenshots com 2 segundos de intervalo:
#   for i in range(1, 4):
#       sleep(2)
#       img = pyautogui.screenshot()
#       img.save(os.path.join(desktop, f"screenshot_{i:02d}.png"))
#       print(f"Screenshot {i} tirado!")
