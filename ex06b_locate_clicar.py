import os
import pyautogui
from time import sleep

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
# EXERCÍCIO 06B — Encontrar e Clicar por Imagem
# ═══════════════════════════════════════════════════════════
# OBJETIVO: Usar locateOnScreen() para encontrar a imagem
#   de referência do ex05a no ecrã e clicar nela.
#   PRÉ-REQUISITO: ex06a concluído (referencia_botao.png existe).
#
# PORQUE É MELHOR QUE COORDENADAS FIXAS:
#   Coordenadas fixas → partem se a janela mover
#   locateOnScreen()  → encontra o elemento onde quer que esteja
#
# CONCEITOS NOVOS:
#   locateOnScreen(imagem)        — procura imagem no ecrã
#   locateCenterOnScreen(imagem)  — devolve centro direto
#   confidence=0.9                — tolerância (0.0–1.0)
#   pyautogui.center(localizacao) — calcular centro da área
# ═══════════════════════════════════════════════════════════

pyautogui.FAILSAFE = True

# Verificar que a referência existe
desktop  = get_desktop()
caminho  = os.path.join(desktop, "referencia_botao.png")

if not os.path.exists(caminho):
    print("⚠ referencia_botao.png não encontrado!")
    print("  Completa o ex06a primeiro.")
    exit()

print(f"✓ Referência encontrada: {caminho}")
print("\nA iniciar em 3 segundos...")
print(">> Garante que o elemento está visível no ecrã! <<\n")
sleep(3)

# ── MÉTODO 1 — locateOnScreen (devolve bounding box) ────────
print("Método 1: locateOnScreen()...")
localizacao = pyautogui.locateOnScreen(caminho, confidence=0.9)

if localizacao is None:
    print("⚠ Elemento não encontrado!")
    print("  Verifica se o elemento está visível e tenta com confidence=0.8")
    exit()

print(f"  Encontrado em: {localizacao}")
print(f"  Box: esq={localizacao.left} topo={localizacao.top} "
      f"larg={localizacao.width} alt={localizacao.height}")

# Calcular o centro
centro = pyautogui.center(localizacao)
print(f"  Centro: ({centro.x}, {centro.y})")

# Mover o rato para o elemento (sem clicar ainda)
pyautogui.moveTo(centro.x, centro.y, duration=1.0)
sleep(0.5)

# ── MÉTODO 2 — locateCenterOnScreen (mais direto) ────────────
print("\nMétodo 2: locateCenterOnScreen()...")
centro2 = pyautogui.locateCenterOnScreen(caminho, confidence=0.9)

if centro2:
    print(f"  Centro direto: ({centro2.x}, {centro2.y})")
    pyautogui.click(centro2.x, centro2.y)
    print("  ✓ Clique efetuado!")
else:
    print("  ⚠ Não encontrado com locateCenterOnScreen.")

print("\n✓ locateOnScreen() concluído!")
print("Próximo: ex06c para contar todas as ocorrências com locateAllOnScreen().")

# ── DESAFIO ────────────────────────────────────────────────
# Tenta com diferentes valores de confidence e mostra qual funciona:
#   for conf in [0.95, 0.90, 0.85, 0.80]:
#       loc = pyautogui.locateOnScreen(caminho, confidence=conf)
#       estado = "✓ encontrado" if loc else "✗ não encontrado"
#       print(f"  confidence={conf}: {estado}")
