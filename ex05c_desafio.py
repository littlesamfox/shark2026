import os
import pyautogui
from time import sleep
from datetime import datetime

# ── Encontrar o Desktop real (funciona com e sem OneDrive) ──
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
# EXERCÍCIO 05C — Ler Cor de um Píxel e Reagir
# ═══════════════════════════════════════════════════════════

# 🔎 DETETIVE DE PASTAS (Garante que o screenshot do Azul funciona!)
desktop = get_desktop()

# ── ASSISTENTE INTERATIVO ───────────────────────────────────
print("═" * 60)
print("🎨 MONITOR DE CORES INTELIGENTE")
print("═" * 60)

print("\nAponta o rato para o pixel que queres monitorizar.")
for i in range(5, 0, -1):
    print(f"A capturar em {i}...", end=" ", flush=True)
    sleep(1)


pontos = [(100,100), (500,300), (960,540), (200,600), (800,200)]
for px, py in pontos:
    r,g,b = pyautogui.pixel(px, py)
    print(f"({px},{py}) → #{r:02X}{g:02X}{b:02X}, RGB: ({r}, {g}, {b})")

cor = pyautogui.pixel(px, py)
r, g, b = cor

print(f"\n🎨 COR DETETADA:")
print(f"   RGB: ({r}, {g}, {b})")
print(f"   Hex: #{r:02X}{g:02X}{b:02X}")

# Classificar a cor dominante (Lógica de decisão)
componente_maior = max(r, g, b)
if componente_maior == r and r > 150:
    dominante = "🔴 Vermelho dominante"
elif componente_maior == g and g > 150:
    dominante = "🟢 Verde dominante"
elif componente_maior == b and b > 150:
    dominante = "🔵 Azul dominante"
elif r > 200 and g > 200 and b > 200:
    dominante = "⬜ Cor clara (Branco/Cinza claro)"
elif r < 50 and g < 50 and b < 50:
    dominante = "⬛ Cor escura (Preto/Cinza escuro)"
else:
    dominante = "🟫 Cor mista / Neutra"

print(f"🔍 Análise: {dominante}")

cor_alvo = (255, 0, 0)
corresponde = pyautogui.pixelMatchesColor(px, py, cor, tolerance=10)
print(f"🎯 Cor corresponde ao esperado? {corresponde}")

# ── PARTE 3 — Reagir com if/else ────────────────────────────
print("\n🚀 EXECUTANDO REAÇÃO...")

if r > g and r > b:
    print("→ AÇÃO: Perigo! Mover para canto de segurança.")
    pyautogui.moveTo(10, 10, duration=0.5)

elif b > r and b > g:
    print("→ AÇÃO: Detetado Azul! A registar prova visual...")
    agora = datetime.now().strftime("%H-%M-%S")
    nome_foto = f"registo_azul_{agora}.png"
    pyautogui.screenshot().save(os.path.join(desktop, nome_foto))
    print(f"   Screenshot guardado: {nome_foto}")

else:
    print("→ AÇÃO: Cor segura. Nenhuma medida necessária.")

print("\n✓ Processo concluído!")

print("\n✓ Leitura de píxel completa!")
print("Próximo: ex05d para monitorizar píxel em loop contínuo.")

# ── DESAFIO ────────────────────────────────────────────────
# Lê 5 pontos diferentes e cria um "mapa de cores":
#   pontos = [(100,100), (500,300), (960,540), (200,600), (800,200)]
#   for px, py in pontos:
#       r,g,b = pyautogui.pixel(px, py)
#       print(f"({px},{py}) → #{r:02X}{g:02X}{b:02X}")