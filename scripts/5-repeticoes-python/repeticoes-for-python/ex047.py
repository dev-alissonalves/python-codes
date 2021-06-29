# -*- coding: UTF-8 -*-
#Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
from time import sleep

print("-=-=--=-=- |AMOSTRAGEM DE NÚMEROS PARES| -=-=--=-=-\n")
for cont in range (1, 51):
    if cont % 2 == 0:
        print(cont, end=" ")
print("\nFINALIZANDO...\n")
sleep(1)
print("-=-=--=-=- |AMOSTRAGEM DE NÚMEROS PARES| -=-=--=-=-\n\n")