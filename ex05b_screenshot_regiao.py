import os
import pyautogui
import pygetwindow as gw
from time import sleep
from datetime import datetime

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


# ═══════════════════════════════════════════════════════════
# EXERCÍCIO 05B — Screenshot de Região
# ═══════════════════════════════════════════════════════════

# 🔎 DETETIVE DE PASTAS (Solução OneDrive)
desktop = get_desktop()

# ── MÉTODO INTERATIVO: SELEÇÃO COM O RATO ────────────────────
print("═" * 60)
print("📸 MODO SNIPPING TOOL (FERRAMENTA DE RECORTE)")
print("═" * 60)

print("\n1. Põe o rato no CANTO SUPERIOR ESQUERDO da área e aguarda...")
for i in range(5, 0, -1):
    print(f"{i}...", end=" ", flush=True)
    sleep(1)
x1, y1 = pyautogui.position()
print(f"\n✅ Canto 1 capturado: ({x1}, {y1})")

print("\n2. Põe o rato no CANTO INFERIOR DIREITO da área e aguarda...")
for i in range(5, 0, -1):
    print(f"{i}...", end=" ", flush=True)
    sleep(1)
x2, y2 = pyautogui.position()
print(f"\n✅ Canto 2 capturado: ({x2}, {y2})")

# ── MATEMÁTICA AUTOMÁTICA ──────────────────────────────────
# Calculamos a largura (w) e altura (h) com base nos dois cliques
largura = x2 - x1
altura = y2 - y1

# Prevenção de erro: garantir que a largura/altura não são negativas
if largura <= 0 or altura <= 0:
    print("\n❌ ERRO: Clicaste nos cantos errados! O segundo clique deve ser à direita e abaixo do primeiro.")
    exit()

# ── EXECUÇÃO DA CAPTURA ─────────────────────────────────────
agora = datetime.now().strftime("%H-%M-%S")
caminho = os.path.join(desktop, f"recorte_{agora}.png")

print(f"\nCapturando região: {largura}x{altura} píxeis...")
# region = (x_inicio, y_inicio, largura, altura)
imagem = pyautogui.screenshot(region=(x1, y1, largura, altura))

imagem.save(caminho)
print(f"✅ Screenshot guardado no Desktop: recorte_{agora}.png")

# Abrir automaticamente para ver o resultado
os.startfile(caminho)
print("Próximo: ex05c para ler a cor de um píxel específico.")

# ── DESAFIO ────────────────────────────────────────────────
# Captura 4 cantos do ecrã em simultâneo:
#   largura_ecra, altura_ecra = pyautogui.size()
#   tamanho = 200
#   cantos = {
#       'topo_esq':  (0, 0, tamanho, tamanho),
#       'topo_dir':  (largura_ecra - tamanho, 0, tamanho, tamanho),
#       'baixo_esq': (0, altura_ecra - tamanho, tamanho, tamanho),
#       'baixo_dir': (largura_ecra - tamanho, altura_ecra - tamanho, tamanho, tamanho),
#   }
#   for nome, regiao in cantos.items():
#       img = pyautogui.screenshot(region=regiao)
#       img.save(os.path.join(desktop, f'canto_{nome}.png'))
#       print(f'Canto {nome} guardado!')
