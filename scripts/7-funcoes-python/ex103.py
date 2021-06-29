#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jog="<Desconhecido>", gol=0): 
    print(f"O jogador {jog} fez {gol} gol(s).")

jogador = str(input("NOME DO JOGADOR: "))
gols = str(input("QUANTIDADE DE GOLS: "))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == "":
    ficha(gol=gols)
else:
    ficha(jogador, gols)

