# -*- coding: UTF-8 -*-
#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input("Digite um número inteiro: "))

acumulador = 0
qtd = 0

for cont in range(1, n+1):
    if n % cont == 0:
        print("\033[33m", end=" ")
        qtd += 1
    else: 
        print("\033[31m", end=" ")
    print(f"{cont}\033[m", end=" ")
print(f"\nO número {n} foi divisível {qtd} vezes.")
if qtd == 2:
    print("E por isso ele é PRIMO!")
else:
    print("E por isso ele NÃO é PRIMO!")