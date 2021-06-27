# -*- coding: UTF-8 -*-
#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

from time import sleep
numero = int(input("DIGITE UM NÚMERO INTEIRO: "))
print("[DIGITE (1) PARA CONVERTER PARA BINÁRIO]\n[DIGITE (2) PARA CONVERTER PARA OCTAL]\n[DIGITE (3) PARA CONVERTER PARA HEXADECIMAL]")
operacao = int(input("\nFAÇA SUA ESCOLHA: "))

if operacao == 1: 
    print(f"Convertendo {numero} para BINÁRIO...")
    sleep(3)
    print(f"[DECIMAL - {numero}] <---> [BINÁRIO - {bin(numero)[2:]}]")
elif operacao == 2:
    print(f"Convertendo {numero} para OCTAL...")
    sleep(3)
    print(f"[DECIMAL - {numero}] <---> [OCTAL - {oct(numero)[2:]}]")
elif operacao == 3:
    print(f"Convertendo {numero} para HEXADECIMAL...")
    sleep(3)
    print(f"[DECIMAL - {numero}] <---> [hexadecimal - {hex(numero)[2:]}]")
else: 
    print("Algo deu errado...")
    print("Execute novamente o programa!")
    exit()