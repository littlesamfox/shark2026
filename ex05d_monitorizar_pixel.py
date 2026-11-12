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
# EXERCÍCIO 05D — Monitorizar Píxel em Loop
# ═══════════════════════════════════════════════════════════
# OBJETIVO: Criar um bot que monitoriza continuamente a cor
#   de um píxel e age automaticamente quando ela muda.
#   PRÉ-REQUISITO: ex05c concluído.
#
# CASO DE USO REAL:
#   - Esperar que um botão fique verde (disponível)
#   - Detetar quando uma notificação aparece
#   - Reagir a mudanças visuais sem coordenadas fixas
#
# CONCEITOS NOVOS:
#   while True + break       — loop até condição ser cumprida
#   pixelMatchesColor()      — comparação com tolerância
#   tolerance=               — margem de erro na comparação
#   time.time()              — medir tempo decorrido (timeout)
# ═══════════════════════════════════════════════════════════

import time

pyautogui.FAILSAFE = True

# ── CONFIGURAÇÃO ─────────────────────────────────────────────
X_PIXEL     = None   # ← ponto a monitorizar (ex01b)
Y_PIXEL     = None
COR_INICIAL = None    # ← cor que ESPERAS antes da mudança ex: (200, 200, 200)
COR_ALVO    = None    # ← cor que ACIONA o bot            ex: (0, 180, 0)
TOLERANCIA  = 30      # margem de erro na comparação de cor
TIMEOUT_SEG = 60      # desistir após 60 segundos
INTERVALO   = 0.5     # verificar a cada 0.5 segundos
# ────────────────────────────────────────────────────────────

if X_PIXEL is None:
    # Modo demonstração — monitoriza o píxel atual e espera mudança manual
    print("ℹ Modo DEMO — sem coordenadas configuradas.")
    print("  O bot vai monitorizar o píxel sob o cursor durante 30 segundos.")
    print("  Move o rato para uma área colorida para ver a deteção.\n")
    sleep(2)
    pos  = pyautogui.position()
    X_PIXEL, Y_PIXEL = pos.x, pos.y
    COR_INICIAL = pyautogui.pixel(X_PIXEL, Y_PIXEL)
    COR_ALVO    = None      # qualquer mudança dispara
    TIMEOUT_SEG = 30

print(f"A monitorizar ({X_PIXEL}, {Y_PIXEL})")
cor_atual = pyautogui.pixel(X_PIXEL, Y_PIXEL)
print(f"Cor atual: RGB{cor_atual} = #{cor_atual[0]:02X}{cor_atual[1]:02X}{cor_atual[2]:02X}")
print(f"Timeout: {TIMEOUT_SEG}s  |  Intervalo: {INTERVALO}s\n")
print("A monitorizar... (move o rato para (0,0) para parar)\n")

desktop    = get_desktop()
t_inicio   = time.time()
iteracoes  = 0
cor_base   = cor_atual

try:
    while True:
        elapsed = time.time() - t_inicio

        # Timeout — desistir se demorar demasiado
        if elapsed > TIMEOUT_SEG:
            print(f"\n⏱ Timeout após {TIMEOUT_SEG}s sem mudança detetada.")
            break

        cor_agora = pyautogui.pixel(X_PIXEL, Y_PIXEL)
        iteracoes += 1

        # Verificar se a cor mudou
        if COR_ALVO is not None:
            mudou = pyautogui.pixelMatchesColor(X_PIXEL, Y_PIXEL, COR_ALVO, tolerance=TOLERANCIA)
        else:
            # Qualquer mudança significativa
            diff = max(abs(cor_agora[i] - cor_base[i]) for i in range(3))
            mudou = diff > TOLERANCIA

        if mudou:
            agora = datetime.now().strftime("%H:%M:%S")
            print(f"\n🎯 MUDANÇA DETETADA às {agora}!")
            print(f"   Cor anterior: RGB{cor_base}")
            print(f"   Cor atual:    RGB{cor_agora}")
            print(f"   Após {elapsed:.1f}s e {iteracoes} verificações")

            # Ação automática: tirar screenshot como registo
            caminho = os.path.join(desktop, f"evento_{datetime.now().strftime('%H-%M-%S')}.png")
            pyautogui.screenshot().save(caminho)
            print(f"   Screenshot guardado: {caminho}")
            break

        # Progresso visual a cada 5 segundos
        if iteracoes % (5 / INTERVALO) == 0:
            print(f"  [{elapsed:.0f}s] A monitorizar... cor atual: RGB{cor_agora}", end='\r')

        sleep(INTERVALO)

except KeyboardInterrupt:
    print("\n\nInterrompido pelo utilizador (CTRL+C).")

print(f"\n✓ Bot terminou após {iteracoes} verificações.")
print("Parabéns — completaste todos os exercícios da Aula 05! 🎉")

# ── DESAFIO ────────────────────────────────────────────────
# Monitoriza 3 píxeis em simultâneo:
#   pontos = [(x1,y1), (x2,y2), (x3,y3)]
#   while True:
#       for px, py in pontos:
#           if <mudou>:
#               print(f"Mudança em ({px},{py})!")
#       sleep(0.5)
