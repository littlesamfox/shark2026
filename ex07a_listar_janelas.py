import pygetwindow as gw
import os

# ═══════════════════════════════════════════════════════════
# EXERCÍCIO 07A — Listar e Inspecionar Janelas Abertas
# ═══════════════════════════════════════════════════════════
# OBJETIVO: Usar pygetwindow para descobrir todas as janelas
#   abertas no Windows, mostrar as suas propriedades e
#   filtrar por título.
#   pip install pygetwindow
#
# CONCEITOS NOVOS:
#   gw.getAllWindows()           — lista todas as janelas
#   gw.getAllTitles()            — lista só os títulos
#   gw.getWindowsWithTitle(txt) — filtrar por título parcial
#   janela.title                — título da janela
#   janela.left/top/width/height— posição e dimensões
#   janela.isActive             — está em foco?
#   janela.isMinimized          — está minimizada?
#
# NOTA: Não precisa de sleep(3) nem minimizar — só leitura!
# ═══════════════════════════════════════════════════════════

print("═" * 55)
print("  INSPETOR DE JANELAS — pygetwindow")
print("═" * 55)

# ── PARTE 1 — Listar todas as janelas com título ─────────────
todas = [j for j in gw.getAllWindows() if j.title.strip()]
print(f"\n✓ Total de janelas com título: {len(todas)}\n")

print(f"{'#':>3}  {'Título':40} {'Pos':15} {'Dim':15} {'Estado'}")
print("-" * 90)

for i, j in enumerate(todas, 1):
    pos   = f"({j.left},{j.top})"
    dim   = f"{j.width}×{j.height}"
    estado = []
    if j.isActive:    estado.append("ATIVO")
    if j.isMinimized: estado.append("min")
    if j.isMaximized: estado.append("max")
    print(f"{i:>3}  {j.title[:40]:40} {pos:15} {dim:15} {', '.join(estado)}")

# ── PARTE 2 — Filtrar por palavra-chave ─────────────────────
print("\n─── Filtro por título ───")
for kw in ["Notepad", "Paint", "Chrome", "Firefox", "Edge", "Calculadora", "PyCharm"]:
    resultados = gw.getWindowsWithTitle(kw)
    if resultados:
        for j in resultados:
            print(f"  [{kw}] → '{j.title}' em ({j.left},{j.top}) {j.width}×{j.height}px")

# ── PARTE 3 — Janela ativa ───────────────────────────────────
print("\n─── Janela ativa agora ───")
ativas = [j for j in todas if j.isActive]
if ativas:
    j = ativas[0]
    print(f"  Título:   {j.title}")
    print(f"  Posição:  ({j.left}, {j.top})")
    print(f"  Tamanho:  {j.width}×{j.height}px")

print("\n✓ Inspeção concluída!")
print("Próximo: ex06b para focar, mover e redimensionar janelas.")

desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
with open(os.path.join(desktop, "janelas.txt"), "w", encoding="utf-8") as f:
    for j in todas:
        f.write(f"{j.title} | ({j.left},{j.top}) | {j.width}×{j.height}\n")
    print("Lista exportada para janelas.txt!")

# ── DESAFIO ────────────────────────────────────────────────
# Exporta a lista para um ficheiro de texto:
#   import os
#   desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
#   with open(os.path.join(desktop, "janelas.txt"), "w", encoding="utf-8") as f:
#       for j in todas:
#           f.write(f"{j.title} | ({j.left},{j.top}) | {j.width}×{j.height}\n")
#   print("Lista exportada para janelas.txt!")
