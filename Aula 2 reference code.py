# 01 - Criar ficheiro no Desktop com Python puro
import os


desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
caminho = os.path.join(desktop, "ficheiro.txt")

print(desktop)

with open(caminho, "w") as f:
    pass # cria o ficheiro vazio



# 01A - O ecra como grelha de coordenadas
import pyautogui

pyautogui.FAILSAFE = True # nunca desativar
largura, altura = pyautogui.size()
print(largura, altura)
print(pyautogui.position())



# 01B - Localizador de coordenadas em tempo real
while True:
    input("Prime ENTER para ver a posicao do rato (CTRL+C para sair)")
    x, y = pyautogui.position()
    print(f"Posicao atual: X={x} Y={y}")

