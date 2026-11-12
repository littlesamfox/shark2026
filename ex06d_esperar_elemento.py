import os
import pyautogui
from time import sleep
import time

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
# EXERCÍCIO 06D — Esperar Elemento Aparecer (Bot Robusto)
# ═══════════════════════════════════════════════════════════
# OBJETIVO: Criar um bot que espera pacientemente até um
#   elemento aparecer no ecrã — só age quando o encontra.
#   PRÉ-REQUISITO: ex06a, 06b e 06c concluídos.
#
# PORQUE É IMPORTANTE:
#   Bots frágeis assumem que tudo aparece instantaneamente.
#   Bots robustos esperam e verificam — como um humano paciente.
#   Esta é a diferença entre um bot que falha e um que funciona.
#
# CONCEITOS NOVOS:
#   try/except                    — capturar erros graciosamente
#   time.time()                   — medir tempo real
#   ImageNotFoundException        — erro específico do PyAutoGui
#   Padrão "esperar e verificar"  — base de todo o bot robusto
# ═══════════════════════════════════════════════════════════

pyautogui.FAILSAFE = True

# ── CONFIGURAÇÃO ─────────────────────────────────────────────
desktop     = get_desktop()
caminho     = os.path.join(desktop, "referencia_botao.png")
CONFIDENCE  = 0.85
TIMEOUT_SEG = 60      # desistir após 60 segundos
INTERVALO   = 1.0     # verificar a cada segundo
# ────────────────────────────────────────────────────────────

if not os.path.exists(caminho):
    print("⚠ referencia_botao.png não encontrado! Completa o ex06a primeiro.")
    exit()

# ── FUNÇÃO: esperar_elemento ─────────────────────────────────
def esperar_elemento(caminho_img, timeout=60, intervalo=1.0, confidence=0.85):
    """
    Aguarda até o elemento aparecer no ecrã.
    Devolve as coordenadas do centro ou None se atingir timeout.
    """
    print(f"A aguardar elemento: {os.path.basename(caminho_img)}")
    print(f"Timeout: {timeout}s  |  Intervalo: {intervalo}s  |  Confidence: {confidence}")
    print("(Faz aparecer o elemento no ecrã para o bot o detetar)\n")

    t_inicio   = time.time()
    tentativas = 0

    while True:
        elapsed = time.time() - t_inicio

        if elapsed > timeout:
            print(f"\n⏱ Timeout após {timeout}s ({tentativas} tentativas).")
            return None

        tentativas += 1
        print(f"  [{elapsed:.0f}s] Tentativa #{tentativas}...", end=' ')

        try:
            loc = pyautogui.locateOnScreen(caminho_img, confidence=confidence)
            if loc:
                centro = pyautogui.center(loc)
                print(f"ENCONTRADO! ({centro.x}, {centro.y})")
                return centro
            else:
                print("não encontrado.")
        except pyautogui.ImageNotFoundException:
            print("não encontrado (ImageNotFoundException).")
        except Exception as e:
            print(f"erro: {e}")

        sleep(intervalo)

# ── EXECUÇÃO ─────────────────────────────────────────────────
print("Bot robusto iniciado — a aguardar elemento...\n")
t_total = time.time()

centro = esperar_elemento(
    caminho,
    timeout    = TIMEOUT_SEG,
    intervalo  = INTERVALO,
    confidence = CONFIDENCE
)

if centro:
    tempo_total = time.time() - t_total
    print(f"\n✓ Elemento encontrado em {tempo_total:.1f}s!")
    print(f"  Centro: ({centro.x}, {centro.y})")

    # Ação após encontrar: mover e clicar
    print("  A mover rato para o elemento...")
    pyautogui.moveTo(centro.x, centro.y, duration=1.0)
    sleep(0.5)
    print("  A clicar...")
    pyautogui.click(centro.x, centro.y)
    print("  ✓ Clique efetuado!")
else:
    print("\n✗ Elemento não apareceu dentro do tempo limite.")
    print("  Sugestões:")
    print("  → Aumentar TIMEOUT_SEG")
    print("  → Reduzir CONFIDENCE para 0.75")
    print("  → Verificar se a referência ainda é válida")

print("\nParabéns — completaste todos os exercícios da Aula 06! 🎉")
print("O teu bot é agora robusto e paciente — como um verdadeiro bot profissional!")

# ── DESAFIO ────────────────────────────────────────────────
# Encadeia 3 elementos em sequência — só avança quando encontrar cada um:
#   elementos = ['passo1.png', 'passo2.png', 'passo3.png']
#   for img in elementos:
#       c = esperar_elemento(os.path.join(desktop, img), timeout=30)
#       if c:
#           pyautogui.click(c.x, c.y)
#           sleep(1.0)
#       else:
#           print(f"Falhou em {img} — a parar."); break
