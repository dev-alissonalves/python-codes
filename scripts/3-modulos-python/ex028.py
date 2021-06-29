# -*- coding: UTF-8 -*-
#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

pensamento = randint(0,5)
print("---> JOGO DA ADIVINHAÇÃO <---\n")
print("[INFORME UM NÚMERO ENTRE 0-5]")
numero = int(input("Qual o seu palpite? "))
print("PROCESSANDO...")
sleep(3)
if numero == pensamento:
    print(f"\nVocê acertou!!\nO computador pensou em {pensamento} e você digitou {numero}")
else:
    print("\nTENTE OUTRA VEZ - VOCÊ ERROU!!!")

print("---> FIM JOGO <---\n")