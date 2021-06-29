# -*- coding: UTF-8 -*-
#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

#modo1
""" from math import factorial
print("\n============ SISTEMA FATORIAL ============\n")
n = int(input("Insira um número para o cálculo do fatorial: "))
print(factorial(n)) """

#modo2
"""print("\n============ SISTEMA FATORIAL ============\n")
n = int(input("Insira um número para o cálculo do fatorial: "))
cont = n
fatorial = 1
print(f"Calculando {n}! = ", end = "")
while cont > 0:
    print(f"{cont}", end = "")
    if cont > 1:
        print(" X ", end = "")
    else: 
        print(" = ", end="")
    fatorial = fatorial * cont
    cont -= 1
print(fatorial)"""

#modo3
print("\n============ SISTEMA FATORIAL ============\n")
n = int(input("Insira um número para o cálculo do fatorial: "))
print(f"Calculando {n}! = ", end = "")
fatorial = 1

for cont in range(n, 0, -1):
    print(f"{cont}", end = "")
    if cont > 1:
        print(" X ", end = "")
    else: 
        print(" = ", end="")
    fatorial = fatorial * cont
    cont -= 1
print(fatorial)