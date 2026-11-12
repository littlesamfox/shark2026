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
# EXERCÍCIO 05A — Capturar Imagem de Referência
# ═══════════════════════════════════════════════════════════
# OBJETIVO: Tirar screenshot de uma região pequena que
#   contém um botão, ícone ou elemento visual.
#   Esta imagem vai ser usada como "molde" nos ex05b e 05c.
#
# COMO FUNCIONA O IMAGE RECOGNITION:
#   O PyAutoGui compara a imagem de referência com o ecrã.
#   Se encontrar uma zona parecida → devolve as coordenadas.
#   É como o "Onde está o Wally?" — mas feito pelo Python!
#
# BOAS PRÁTICAS para a imagem de referência:
#   ✓  Capturar só o elemento (não incluir fundo variável)
#   ✓  Fundo consistente (não clicar em botões hover)
#   ✓  Tamanho mínimo: 20×20px   máximo recomendado: 150×150px
#   ✓  Guardar como PNG (sem compressão com perda)
# ═══════════════════════════════════════════════════════════

# ── CONFIGURAÇÃO ─────────────────────────────────────────────
# Região exacta do elemento a capturar (usa ex01b)
X_ELEM   = 1792    # ← canto esquerdo do elemento
Y_ELEM   = 1396  # ← canto superior do elemento
LARGURA  = 80      # ← largura do elemento em píxeis
ALTURA   = 40      # ← altura do elemento em píxeis
NOME_REF = "referencia_botao"   # nome base do ficheiro
# ────────────────────────────────────────────────────────────

if X_ELEM is None:
    print("⚠ Preenche X_ELEM, Y_ELEM com coordenadas do ex02b!")
    print("  Aponta para o canto sup. esq. do elemento a capturar.")
    exit()

desktop = get_desktop()
caminho = os.path.join(desktop, f"{NOME_REF}.png")

print(f"Região: ({X_ELEM}, {Y_ELEM}) — {LARGURA}×{ALTURA}px")
print(f"A guardar em: {caminho}")
print("\nPosiciona o ecrã com o elemento visível...")
print("A capturar em 3 segundos...\n")
sleep(3)

# Capturar só a região do elemento
regiao = (X_ELEM, Y_ELEM, LARGURA, ALTURA)
imagem = pyautogui.screenshot(region=regiao)
imagem.save(caminho)

if os.path.exists(caminho):
    print(f"✓ Referência guardada: {caminho}")
    print(f"  Dimensões: {imagem.size[0]}×{imagem.size[1]}px")
    print(f"  Tamanho:   {os.path.getsize(caminho):,} bytes")
else:
    print("⚠ Erro ao guardar a imagem de referência.")
    exit()

print("\nPróximo: ex06b para encontrar este elemento no ecrã com locateOnScreen().")

# ── DESAFIO ────────────────────────────────────────────────
# Captura 3 elementos diferentes como referência:
#   elementos = [('botao_ok', x1, y1, 80, 40),
#                ('icone_pasta', x2, y2, 32, 32),
#                ('logo', x3, y3, 120, 60)]
#   for nome, x, y, w, h in elementos:
#       img = pyautogui.screenshot(region=(x, y, w, h))
#       img.save(os.path.join(desktop, f'{nome}.png'))
#       print(f'Referência "{nome}" guardada.')
