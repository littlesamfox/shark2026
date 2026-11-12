# ── IMPORTAÇÃO DE BIBLIOTECAS (As ferramentas que o nosso script precisa) ──
import os             # Usado para mexer nos ficheiros, pastas e comandos do próprio Windows.
import pyautogui      # O nosso "robô". Simula teclas e cliques do rato.
import pyperclip      # Usado para Copiar (para a memória do PC) e Colar. Evita erros com acentos e barras.
from time import sleep # Importa a função 'sleep' para fazer o robô esperar/pausar entre ações.
from datetime import datetime # Usado para ir buscar a data e a hora exatas do computador.

# ═══════════════════════════════════════════════════════════
# EXERCÍCIO 03D — Ler, Reorganizar e Guardar como Novo Ficheiro
# ═══════════════════════════════════════════════════════════

# Segurança máxima: se o robô enlouquecer, atira o rato para um dos 4 cantos do ecrã para forçar a paragem!
pyautogui.FAILSAFE = True

# ── 1. DETETIVE DE FICHEIROS (Procurar o aula03.txt original) ──
# Vai buscar o caminho base do teu utilizador (ex: C:\Users\almad)
u = os.environ["USERPROFILE"]

# Cria uma lista com todos os sítios onde o ficheiro pode ter ido parar nas aulas anteriores
possiveis_caminhos = [
    os.path.join(u, "aula03.txt"),
    os.path.join(u, "OneDrive - sharkcoders", "Ambiente de Trabalho", "aula03.txt"),
    os.path.join(u, "OneDrive", "Ambiente de Trabalho", "aula03.txt"),
    os.path.join(u, "Desktop", "aula03.txt"),
    os.path.join(u, "Ambiente de Trabalho", "aula03.txt"),
    os.path.join(u, "Documents", "aula03.txt"),
]

# Testa um por um. O primeiro caminho que o Python confirmar que existe, guarda na variável 'caminho_antigo'.
caminho_antigo = next((c for c in possiveis_caminhos if os.path.exists(c)), None)

# Se testou todos e não encontrou, avisa e fecha o programa (exit)
if not caminho_antigo:
    print("\n⚠ aula03.txt original não encontrado! Executa os exercícios anteriores primeiro.")
    exit()

# Descobre em que pasta está o ficheiro antigo para guardar o novo no mesmo sítio
pasta_pai = os.path.dirname(caminho_antigo)
# Cria o nome do novo ficheiro juntando a pasta com "aula3_1.txt"
caminho_novo = os.path.join(pasta_pai, "aula3_1.txt")
# normpath() corrige automaticamente as barras inclinadas (\ e /) para ficarem perfeitas para o Windows
caminho_novo = os.path.normpath(caminho_novo)

print(f"✓ A ler de: {caminho_antigo}")
print(f"✓ Vamos guardar em: {caminho_novo}")


# ── PARTE 1 — Ler e analisar (Python a trabalhar em modo invisível) ──
# Abre o ficheiro antigo no modo de leitura ('r' = read) com suporte para acentos (utf-8)
with open(caminho_antigo, 'r', encoding='utf-8') as f:
    # Lê todas as linhas. O strip() remove os espaços vazios e "enters" extra. Só guarda as linhas que têm texto.
    linhas = [l.strip() for l in f.readlines() if l.strip()]

# Filtra as linhas: guarda só as que NÃO começam por '---' (ignorando assim cabeçalhos velhos)
conteudo = [l for l in linhas if not l.startswith('---')]
# Vai buscar a data e hora do momento exato em que o script corre
agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

# Cria uma lista vazia que vai conter o visual final do nosso novo texto, linha a linha
novo_texto = [
    '╔══════════════════════════════════╗',
    '║   AULA 03 — PyAutoGui            ║',
    '║   Ficheiro reorganizado          ║',
    '╚══════════════════════════════════╝',
    '',  # Linha em branco para dar espaço
    f'Última atualização: {agora}',
    '',  # Linha em branco
    '── CONTEÚDO NUMERADO ──────────────',
]

# Percorre o texto antigo e adiciona-o ao novo_texto, mas numerando cada linha (001., 002., etc.)
for i, linha in enumerate(conteudo, 1):
    novo_texto.append(f'{i:03d}. {linha}')

# Adiciona o rodapé final
novo_texto.append('')
novo_texto.append('── FIM DO FICHEIRO ────────────────')


print("\nA iniciar em 3 segundos... MINIMIZA O PYCHARM!")
sleep(3) # Pausa crucial para teres tempo de tirar as mãos do teclado e minimizar a janela!


# ── PARTE 2 — Automação Visual (O robô entra em ação) ──

# Passo 1: Abrir o ficheiro antigo no Bloco de Notas
print("A abrir o Bloco de Notas...")
pyautogui.hotkey('win', 'r')    # Abre a janela "Executar" do Windows
sleep(0.8)
pyperclip.copy(f'notepad "{caminho_antigo}"')  # Copia o endereço do ficheiro antigo para a memória (clipboard)
pyautogui.hotkey('ctrl', 'v')   # Cola o endereço na caixa
pyautogui.press('enter')        # Confirma para abrir
sleep(2)                      # Espera 2 para garantir que o Bloco de Notas abriu na totalidade

# Passo 2: Limpar o que lá está
print("A limpar o texto antigo...")
pyautogui.hotkey('ctrl', 't')   # Seleciona todo o texto antigo
sleep(0.5)
pyautogui.press('delete')       # Apaga tudo, deixando a folha em branco
sleep(0.5)

# Passo 3: Escrever o texto novo linha a linha
print("A desenhar o novo texto linha a linha...")
for linha in novo_texto:
    pyperclip.copy(linha)         # Copia a frase atual (garante que os ╔═ e os acentos não dão erro)
    pyautogui.hotkey('ctrl', 'v') # Cola a frase no Bloco de Notas
    pyautogui.press('enter')      # Carrega no Enter para mudar de linha
    sleep(0.1)                    # Espera 0.1s. Isto cria aquele efeito visual fixe de estar a ser "desenhado"


# Verificar antes da gravação se será necessário confirmar substituição
destino_ja_existe = os.path.exists(caminho_novo)

# Passo 4: Guardar como Ficheiro Novo
print("A pedir para Guardar Como...")
#pyautogui.click()               # Um clique simples no meio do ecrã só para garantir que o Bloco de Notas não perdeu o foco
#sleep(0.5)
#pyautogui.hotkey('ctrl', 'shift', 'd') # O TEU atalho específico (descoberto na foto) para "Guardar Como..."

# No Windows 10, usar Ctrl+Shift+S
#
#
pyautogui.hotkey('ctrl', 'shift', 's')


sleep(2.0)                      # Pausa longa para garantir que a janela de gravar abriu completamente

print("A colar o caminho e a guardar...")
# Seleccionar o campo "Nome do ficheiro" na janela Guardar Como.
# Alt+N é o atalho habitual desse campo no Windows.
pyautogui.hotkey('alt', 'n')
sleep(0.3)

# Substituir o nome existente pelo caminho completo do novo ficheiro.
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy(caminho_novo)    # Copia o nome/caminho do ficheiro NOVO (aula3_1.txt)
pyautogui.hotkey('ctrl', 'v')   # Cola na barra de nome do ficheiro
sleep(1.0)
pyautogui.press('enter')        # Confirma a gravação
sleep(2.0)                      # Dá 2 segundos para o disco rígido guardar fisicamente o ficheiro

# Se aparecer a confirmação de substituição, confirmar.
# Se não aparecer, estas teclas não gravam o original.
# Só enviar a confirmação quando o destino já existia
if destino_ja_existe:
    pyautogui.hotkey('alt', 'y')  # "Yes"
    sleep(1)

# Fechar o separador depois de guardar
pyautogui.hotkey('ctrl', 'w')
sleep(0.5)

# Proteção extra: se já existir um ficheiro "aula3_1.txt" de testes anteriores, o Windows pergunta se queres substituir.
#pyautogui.press('left')         # Move a seleção do "Não" para o "Sim"
#sleep(0.2)
#pyautogui.press('enter')        # Confirma o "Sim"
#sleep(1.0)

sleep(2)

# Proteção extra: se já existir um ficheiro "aula3_1.txt" de testes anteriores, o Windows pergunta se queres substituir.
# Confirmar a substituição apenas se o ficheiro já existia
if destino_ja_existe:
    pyautogui.press('left') # Move a seleção do "Não" para o "Sim"
    pyautogui.press('enter')# Confirma o "Sim"
    sleep(2)

# Fechar o separador do ficheiro guardado
pyautogui.hotkey('ctrl', 'w')
sleep(1)

# Fechar a janela do Notepad
pyautogui.hotkey('alt', 'f4')

# Passo 5: Fechar a aplicação
print("A encerrar...")
# Envia um comando direto ao sistema operativo para "matar" o processo do Bloco de Notas.
# É muito mais fiável que o Alt+F4 e nunca desliga o computador por acidente.
#os.system("taskkill /f /im notepad.exe")

print(f"\n✓ SUCESSO ABSOLUTO! Ficheiro guardado em:\n👉 {caminho_novo}")
print("Parabéns — completaste todos os exercícios da Aula 03! 🎉")

# ── DESAFIO ────────────────────────────────────────────────
# Guarda também uma cópia de backup com a data no nome:
#   from shutil import copy2
#   backup = os.path.join(desktop, f'aula03_backup_{agora[:10].replace("/","-")}.txt')
#   copy2(caminho, backup)
#   print(f'Backup guardado: {backup}')