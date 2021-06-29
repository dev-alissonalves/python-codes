# -*- coding: UTF-8 -*-
#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

print("============ SOMA NÚMEROS PARES ============")
print("-- DIGITE 6 NÚMEROS QUAISQUER --\n")
soma = 0
n = 0
for cont in range (1, 7):
    n = int(input(f"DIGITE O {cont}º NÚMERO INTEIRO: "))
    if n % 2 == 0:
        soma += n
if soma == 0:
    print("\nTodos os números digitados são ímpares!\n")
else:
    print(f"\nA SOMA DOS NÚMEROS PARES DIGITADOS É = {soma}\n")