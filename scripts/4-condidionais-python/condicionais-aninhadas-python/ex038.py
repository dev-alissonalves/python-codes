# -*- coding: UTF-8 -*-
#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

num1 = int(input("DIGITE UM NÚMERO: "))
num2 = int(input("DIGITE UM SEGUNDO NÚMERO: "))

if num1 > num2: 
    print(f"O valor {num1} é maior que {num2}")
elif num2 > num1: 
    print(f"O valor {num2} é maior que {num1}")
else:
    print(f"Os valores {num1} e {num2} são iguais!")