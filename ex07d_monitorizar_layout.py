import pyautogui
import pygetwindow as gw
from time import sleep
import time
import os
from datetime import datetime


# ═══════════════════════════════════════════════════════════
# EXERCÍCIO 07D — Monitorizar e Reorganizar Janelas
# ═══════════════════════════════════════════════════════════
# OBJETIVO: Loop que verifica periodicamente se as janelas
#   saíram das posições esperadas e as reorganiza.
#   PRÉ-REQUISITO: ex07c concluído (3 apps abertas).
#
# ANALOGIA: "Vigilante de layout" — como um segurança que
#   verifica se tudo está no sítio certo e corrige se não.
#
# CONCEITOS NOVOS:
#   Guardar estado esperado      — dicionário de posições
#   Comparar estado atual vs esperado — detetar desvios
#   Reorganizar automaticamente  — corrigir sem intervir
#   CICLOS + TIMEOUT             — parar após N iterações
#
# ⚠ Move uma janela manualmente para ver o bot reorganizar!
# ═══════════════════════════════════════════════════════════

pyautogui.FAILSAFE = True

LARG, ALT  = pyautogui.size()
MARGEM     = 10
COL_LARG   = (LARG - MARGEM * 4) // 3
COL_ALT    = ALT - 80
TOLERANCIA = 30      # píxeis de desvio antes de reorganizar
INTERVALO  = 2.0     # verificar a cada 2 segundos
DURACAO    = 60      # monitorizar durante 60 segundos

# Layout esperado: (titulo_pesquisa, x, y, largura, altura)
LAYOUT = [
    (["Notepad","Bloco de Notas","Untitled"], MARGEM,                        MARGEM, COL_LARG, COL_ALT),
    (["Paint","Sem título"],                  MARGEM + COL_LARG + MARGEM,    MARGEM, COL_LARG, COL_ALT),
    (["Calculadora","Calculator"],            MARGEM + (COL_LARG+MARGEM)*2,  MARGEM, COL_LARG, COL_ALT),
]

def encontrar_janela(titulos):
    for t in titulos:
        js = gw.getWindowsWithTitle(t)
        if js: return js[0]
    return None

def fora_do_lugar(janela, x_esp, y_esp, w_esp, h_esp, tol):
    return (abs(janela.left - x_esp) > tol or
            abs(janela.top  - y_esp) > tol or
            abs(janela.width  - w_esp) > tol or
            abs(janela.height - h_esp) > tol)

def reorganizar(janela, x, y, w, h, nome):
    try:
        janela.restore()
        sleep(0.2)
        janela.activate()
        sleep(0.2)
        janela.moveTo(x, y)
        sleep(0.2)
        janela.resizeTo(w, h)
        sleep(0.2)
        print(f"  ↩  {nome} → reorganizada em ({x},{y})")
        return True
    except Exception as e:
        print(f"  ⚠  Erro com {nome}: {e}")
        return False

# ── MONITORIZAÇÃO ────────────────────────────────────────────
print("Bot de monitorização de layout iniciado.")
print(f"Duração: {DURACAO}s  |  Intervalo: {INTERVALO}s  |  Tolerância: {TOLERANCIA}px")
print("Move uma janela para ver o bot reagir!\n")
print("(Mover rato para (0,0) para parar)\n")

t_inicio     = time.time()
verificacoes = 0
correcoes    = 0

try:
    while time.time() - t_inicio < DURACAO:
        verificacoes += 1
        elapsed = time.time() - t_inicio
        alguma_corrigida = False

        for titulos, x_esp, y_esp, w_esp, h_esp in LAYOUT:
            janela = encontrar_janela(titulos)
            if janela is None:
                continue
            if janela.isMinimized:
                continue
            if fora_do_lugar(janela, x_esp, y_esp, w_esp, h_esp, TOLERANCIA):
                nome = janela.title[:30]
                print(f"[{elapsed:.0f}s] Desvio detetado: '{nome}'")
                if reorganizar(janela, x_esp, y_esp, w_esp, h_esp, nome):
                    correcoes += 1
                    alguma_corrigida = True

        if not alguma_corrigida:
            print(f"[{elapsed:.0f}s] Layout OK — {verificacoes} verificações, {correcoes} correções", end='\r')

        sleep(INTERVALO)

except KeyboardInterrupt:
    print("\n\nInterrompido pelo utilizador.")

print(f"\n\n✓ Monitorização concluída!")
print(f"  Verificações: {verificacoes}")
print(f"  Correções:    {correcoes}")
print("\nParabéns — completaste todos os exercícios da Aula 07! 🎉")

desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
with open(os.path.join(desktop, "janelas.txt"), "w", encoding="utf-8") as f:
    for j in janela:
        with open("layout_log.txt","a") as f:
          f.write(f"{datetime.now():%H:%M:%S} | {nome} reorganizada\n")

# ── DESAFIO ────────────────────────────────────────────────
# Guarda um log das correções em ficheiro:
#   from datetime import datetime
#   with open("layout_log.txt","a") as f:
#       f.write(f"{datetime.now():%H:%M:%S} | {nome} reorganizada\n")
