# -*- coding: UTF-8 -*-
#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

print("-=-=--=-=- |GAME - JOKENPÔ| -=-=--=-=-\n")
from random import choice
from time import sleep

#configurando as respostas adversário
escolhas = ["PEDRA", "PAPEL", "TESOURA"]
jogada_adversario = choice(escolhas)

print("SUAS OPÇÕES: ")
print("[ 1 ] PEDRA\n[ 2 ] PAPEL\n[ 3 ] TESOURA\n")
jogada = int(input("Qual será sua jogada? "))

if jogada == 1 and jogada_adversario == "PEDRA":
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!\n")
    print("-=-=--=-=- |RESULTADO| -=-=--=-=-\n")
    print(f"COMPUTADOR JOGOU: {jogada_adversario}")
    print(f"VOCÊ JOGOU: PEDRA\n")
    print("-=-=--=-=- \033[;;45m|EMPATE TÉCNICO!|\033[m -=-=--=-=-\n")

elif jogada == 1 and jogada_adversario == "PAPEL":
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!\n")
    print("-=-=--=-=- |RESULTADO| -=-=--=-=-\n")
    print(f"COMPUTADOR JOGOU: {jogada_adversario}")
    print(f"VOCÊ JOGOU: PEDRA\n")
    print("-=-=--=-=- \033[;;41m|COMPUTADOR VENCEU!!|\033[m -=-=--=-=-\n")

elif jogada == 1 and jogada_adversario == "TESOURA":
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!\n")
    print("-=-=--=-=- |RESULTADO| -=-=--=-=-\n")
    print(f"COMPUTADOR JOGOU: {jogada_adversario}")
    print(f"VOCÊ JOGOU: PEDRA\n")
    print("-=-=--=-=- \033[;;42m|JOGADOR VENCEU!!|\033[m -=-=--=-=-\n")

elif jogada == 2 and jogada_adversario == "PEDRA":
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!\n")
    print("-=-=--=-=- |RESULTADO| -=-=--=-=-\n")
    print(f"COMPUTADOR JOGOU: {jogada_adversario}")
    print(f"VOCÊ JOGOU: PAPEL\n")
    print("-=-=--=-=- \033[;;42m|JOGADOR VENCEU!!|\033[m -=-=--=-=-\n")

elif jogada == 2 and jogada_adversario == "PAPEL":
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!\n")
    print("-=-=--=-=- |RESULTADO| -=-=--=-=-\n")
    print(f"COMPUTADOR JOGOU: {jogada_adversario}")
    print(f"VOCÊ JOGOU: PAPEL\n")
    print("-=-=--=-=- \033[;;45m|EMPATE TÉCNICO!|\033[m -=-=--=-=-\n")

elif jogada == 2 and jogada_adversario == "TESOURA":
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!\n")
    print("-=-=--=-=- |RESULTADO| -=-=--=-=-\n")
    print(f"COMPUTADOR JOGOU: {jogada_adversario}")
    print(f"VOCÊ JOGOU: PAPEL\n")
    print("-=-=--=-=- \033[;;41m|COMPUTADOR VENCEU!!|\033[m -=-=--=-=-\n")

elif jogada == 3 and jogada_adversario == "PEDRA":
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!\n")
    print("-=-=--=-=- |RESULTADO| -=-=--=-=-\n")
    print(f"COMPUTADOR JOGOU: {jogada_adversario}")
    print(f"VOCÊ JOGOU: TESOURA\n")
    print("-=-=--=-=- \033[;;41m|COMPUTADOR VENCEU!!|\033[m -=-=--=-=-\n")

elif jogada == 3 and jogada_adversario == "PAPEL":
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!\n")
    print("-=-=--=-=- |RESULTADO| -=-=--=-=-\n")
    print(f"COMPUTADOR JOGOU: {jogada_adversario}")
    print(f"VOCÊ JOGOU: TESOURA\n")
    print("-=-=--=-=- \033[;;42m|JOGADOR VENCEU!!|\033[m -=-=--=-=-\n")

elif jogada == 3 and jogada_adversario == "TESOURA":
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!\n")
    print("-=-=--=-=- |RESULTADO| -=-=--=-=-\n")
    print(f"COMPUTADOR JOGOU: {jogada_adversario}")
    print(f"VOCÊ JOGOU: TESOURA\n")
    print("-=-=--=-=- \033[;;45m|EMPATE TÉCNICO!|\033[m -=-=--=-=-\n")
else:
    print("algo deu errado...\nTente novamente!")
    exit()