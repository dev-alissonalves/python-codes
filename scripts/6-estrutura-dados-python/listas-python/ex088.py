#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep


print("-"*10,     "     JOGO DA MEGA SENA     "     ,"-" *10)
partida = []
jogos = []
palpites = int(input("Quantos jogos deseja realizar: "))
for p in range(0, palpites):
    for num in range(1, 7):
        valor = randint(1,60)
        while valor in partida:
            valor = randint(1,60)       
        partida.append(valor)
    
    partida.sort()
    jogos.append(partida[:])
    partida.clear()
print()
for i,p in enumerate(jogos):
    print(f"Jogo {i+1}: {p}")

print("-=" * 30)
print("-="*10,     "JOGO DA MEGA SENA"     ,"-=" *10)
print("-=" * 30)