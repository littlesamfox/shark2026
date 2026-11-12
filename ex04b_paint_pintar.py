import pyautogui
from time import sleep

# ═══════════════════════════════════════════════════════════
# EXERCÍCIO 04B — Pintar o Quadrado (Problema do Foco Resolvido)
# ═══════════════════════════════════════════════════════════

pyautogui.FAILSAFE = True

print("═════════════════════════════════════════════════════")
print("🪄 O ASSISTENTE DE COORDENADAS VAI COMEÇAR!")
print("Abre o Paint (com o quadrado desenhado) e põe-no à vista.")
print("═════════════════════════════════════════════════════\n")
sleep(3)

# ── 1. FASE DE CAPTURA ─────────────────────────────────────
# Capturar a COR
print("🎨 PASSO 1: Põe o rato em cima da COR que queres (não cliques!)")
for i in range(10, 0, -1):
    print(f"  A gravar em {i}...")
    sleep(1.0)
X_COR, Y_COR = pyautogui.position()
print(f"✓ Cor guardada!\n")

# Capturar o BALDE DE TINTA
print("🪣 PASSO 2: Põe o rato no botão do BALDE DE TINTA (não cliques!)")
for i in range(10, 0, -1):
    print(f"  A gravar em {i}...")
    sleep(1.0)
X_BALDE, Y_BALDE = pyautogui.position()
print(f"✓ Balde guardado!\n")

# Capturar o CENTRO DO QUADRADO
print("🔲 PASSO 3: Põe o rato no MEIO do teu quadrado vazio (não cliques!)")
for i in range(10, 0, -1):
    print(f"  A gravar em {i}...")
    sleep(1.0)
cx, cy = pyautogui.position()
print(f"✓ Centro guardado!\n")

print("Tudo pronto! Podes largar o rato. A automação vai começar...\n")
sleep(1)


# ── 2. FASE DE AUTOMAÇÃO ───────────────────────────────────

# # Clicamos primeiro no centro do quadrado só para chamar o foco para o Paint.
# print("A focar o Paint...")
# pyautogui.click(cx, cy)
# sleep(2) # Dá meio segundo para o Windows perceber que o Paint é a janela principal

# Passo 1 — Selecionar a cor
print("A clicar na cor...")
pyautogui.click(X_COR, Y_COR)
sleep(2)

# Passo 2 — Selecionar balde de tinta
print("A selecionar balde de tinta...")
pyautogui.click(X_BALDE, Y_BALDE)
sleep(2)

# Passo 3 — Clicar dentro do quadrado para pintar
print("A pintar o quadrado!")
pyautogui.click(cx, cy)
pyautogui.click()
sleep(2)

print("\n✓ SUCESSO! O teu quadrado deve estar pintado agora!")
print("Próximo: ex04c para desenhar círculo e triângulo.")


# ── DESAFIO ────────────────────────────────────────────────
# Pinta com uma cor personalizada usando o seletor de cor:
#   pyautogui.doubleClick(X_COR, Y_COR)  # abre seletor
#   sleep(0.5)
#   # descobre coordenadas do campo R, G, B com ex01b
#   # e preenche os valores com write()
