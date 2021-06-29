#Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
from time import sleep

c = ("\033[m", # 0 - SEM CORES
     "\033[0;30;41m", # 1 - VERMELHO
     "\033[0;30;42m", # 2 - VERDE
     "\033[0;30;43m", # 3 - AMARELO
     "\033[0;30;44m", # 4 - AZUL
     "\033[0;30;45m", # 5 - ROXO
     "\033[7;30m",    # 6 - BRANCO
);


def ajuda(cmd):
    titulo(f"Acessando o manual do comando '{cmd}'", 4)
    print(c[6], end="")
    help(cmd)
    print(c[0], end="")
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end="")
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)
    print(c[0], end="")
    sleep(1)

# Programa Principal
comando = ""
while True:
    titulo("GUIA INTERATIVO DO PYTHON", 2)
    comando = str(input("Função ou Biblioteca: "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)

titulo("ATÉ LOGO", 1)