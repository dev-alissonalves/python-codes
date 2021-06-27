# -*- coding: UTF-8 -*-
#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
pensamento = randint(0,10)
palpites = 0
print("\n---> JOGO DA ADIVINHAÇÃO - VERSÃO ATUALIZADA <---\n")
print("Meu nome é ENIAC 2021... sou seu computador!\nAcabei de processar um número entre 0 e 10, será que você consegue adivinhar qual foi?\n")
print("[INFORME UM NÚMERO ENTRE 0-10]")
numero = int(input("Qual o seu palpite? "))
print("PROCESSANDO...\n")
palpites += 1
while pensamento != numero:
    palpites += 1
    if  pensamento > numero: 
        print("É um número maior...\nTente novamente!\n")
        numero = int(input("Qual o seu novo palpite? "))
        print("\n")
    else: 
        print("É um número menor...\nTente novamente!\n")
        numero = int(input("Qual o seu novo palpite? "))
        print("\n")
print(f"VOCÊ ACERTOU!\nForam necessários {palpites} Palpites.")
print("\n---> FIM JOGO <---\n")
