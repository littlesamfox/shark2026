import pyautogui
import pygetwindow as gw
from time import sleep

# ═══════════════════════════════════════════════════════════
# EXERCÍCIO 07B — Focar, Mover e Redimensionar Janelas
# ═══════════════════════════════════════════════════════════
# OBJETIVO: Controlar uma janela existente — ativá-la,
#   movê-la para uma posição específica e redimensioná-la.
#   PRÉ-REQUISITO: ex06a concluído. Ter o Bloco de Notas aberto.
#
# CONCEITOS NOVOS:
#   janela.activate()           — trazer para primeiro plano
#   janela.moveTo(x, y)         — mover para posição (x,y)
#   janela.resizeTo(w, h)       — redimensionar para w×h px
#   janela.maximize()           — maximizar
#   janela.minimize()           — minimizar
#   janela.restore()            — restaurar de min/max
#
# ⚠ Abre o Bloco de Notas manualmente antes de correr!
# ═══════════════════════════════════════════════════════════

pyautogui.FAILSAFE = True

# Procurar o Bloco de Notas
print("A procurar Bloco de Notas...")
janelas = gw.getWindowsWithTitle("Notepad") or gw.getWindowsWithTitle("Bloco de Notas")

if not janelas:
    print("⚠ Bloco de Notas não encontrado!")
    print("  Abre o Bloco de Notas manualmente e volta a correr.")
    exit()

janela = janelas[0]
print(f"✓ Encontrado: '{janela.title}'")
print(f"  Posição atual:  ({janela.left}, {janela.top})")
print(f"  Tamanho atual:  {janela.width}×{janela.height}px\n")

print("A iniciar em 3 segundos...")
sleep(3)

# Passo 1 — Ativar (trazer para primeiro plano)
print("Passo 1: A ativar janela...")
janela.activate()
sleep(0.5)

# Passo 2 — Restaurar se estiver minimizada/maximizada
print("Passo 2: A restaurar...")
janela.restore()
sleep(0.5)

# Passo 3 — Mover para canto superior esquerdo
print("Passo 3: A mover para (50, 50)...")
janela.moveTo(50, 50)
sleep(0.8)
print(f"  Nova posição: ({janela.left}, {janela.top})")

# Passo 4 — Redimensionar
print("Passo 4: A redimensionar para 600×400...")
janela.resizeTo(600, 400)
sleep(0.8)
print(f"  Novo tamanho: {janela.width}×{janela.height}px")

# Passo 5 — Minimizar, esperar, restaurar
print("Passo 5: A minimizar...")
janela.minimize()
sleep(1.0)
print("Passo 5: A restaurar...")
janela.restore()
sleep(0.5)

# Passo 6 — Posição final — centro do ecrã
larg_ecra, alt_ecra = pyautogui.size()
x_centro = (larg_ecra - 600) // 2
y_centro = (alt_ecra  - 400) // 2
print(f"Passo 6: A centrar no ecrã ({x_centro}, {y_centro})...")
janela.moveTo(x_centro, y_centro)
sleep(0.5)

print(f"\n✓ Janela controlada com sucesso!")
print(f"  Posição final: ({janela.left}, {janela.top})")
print("Próximo: ex07c para abrir 3 apps e organizá-las lado a lado.")

# ── DESAFIO ────────────────────────────────────────────────
# Move a janela em espiral:
#   posicoes = [(100,100),(700,100),(700,500),(100,500),(400,300)]
#   for x, y in posicoes:
#       janela.moveTo(x, y)
#       sleep(0.5)
