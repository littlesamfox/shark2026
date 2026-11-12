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
# EXERCÍCIO 06C — Contar Todas as Ocorrências de um Ícone
# ═══════════════════════════════════════════════════════════
# OBJETIVO: Usar locateAllOnScreen() para encontrar TODAS
#   as ocorrências de uma imagem de referência no ecrã.
#   PRÉ-REQUISITO: ex06a concluído.
#
# CASOS DE USO REAIS:
#   - Contar quantos ficheiros .txt estão no Desktop
#   - Verificar quantas abas estão abertas no browser
#   - Contar ícones de uma aplicação
#
# CONCEITOS NOVOS:
#   locateAllOnScreen()  — devolve TODAS as ocorrências
#   list()               — converter generator em lista
#   enumerate()          — iterar com índice
#   pyautogui.center()   — centro de cada ocorrência
# ═══════════════════════════════════════════════════════════

pyautogui.FAILSAFE = True

desktop  = get_desktop()
caminho  = os.path.join(desktop, "referencia_botao.png")

if not os.path.exists(caminho):
    print("⚠ referencia_botao.png não encontrado! Completa o ex06a primeiro.")
    exit()

print(f"✓ Referência: {caminho}")
print("\nA iniciar em 3 segundos...")
print(">> Garante que o elemento está visível (várias vezes se possível)! <<\n")
sleep(3)

# Encontrar TODAS as ocorrências
print("A procurar todas as ocorrências...")
#todas = list(pyautogui.locateAllOnScreen(caminho, confidence=0.85))
#total = len(todas)

detecoes = list(
    pyautogui.locateAllOnScreen(caminho, confidence=0.85)
)

todas = []

for loc in detecoes:
    centro = pyautogui.center(loc)

    # Considerar repetidas as detecções com centros próximos.
    repetida = any(
        abs(centro.x - pyautogui.center(outra).x) < loc.width / 2
        and
        abs(centro.y - pyautogui.center(outra).y) < loc.height / 2
        for outra in todas
    )

    if not repetida:
        todas.append(loc)

total = len(todas)

if total == 0:
    print("⚠ Nenhuma ocorrência encontrada.")
    print("  Tenta com confidence mais baixo (0.75) ou verifica a referência.")
    exit()

print(f"\n✓ Encontradas {total} ocorrência(s)!\n")

# Mostrar todas as posições
for i, loc in enumerate(todas, 1):
    centro = pyautogui.center(loc)
    print(f"  #{i:02d}  centro=({centro.x}, {centro.y})  "
          f"box=({loc.left},{loc.top},{loc.width}×{loc.height})")

# Mover rato por cada ocorrência com pausa
print(f"\nA percorrer as {total} ocorrências com o rato...")
sleep(1)
for i, loc in enumerate(todas, 1):
    centro = pyautogui.center(loc)
    pyautogui.moveTo(centro.x, centro.y, duration=0.5)
    print(f"  Ocorrência #{i}: ({centro.x}, {centro.y})")
    sleep(0.3)

print(f"\n✓ Total: {total} ocorrência(s) encontrada(s).")
print("Próximo: ex06d para esperar um elemento aparecer com loop robusto.")

# ── DESAFIO ────────────────────────────────────────────────
# Clica em todas as ocorrências com uma pausa entre cliques:
#   for i, loc in enumerate(todas, 1):
#       centro = pyautogui.center(loc)
#       pyautogui.click(centro.x, centro.y)
#       print(f"Clique #{i} em ({centro.x}, {centro.y})")
#       sleep(0.5)
