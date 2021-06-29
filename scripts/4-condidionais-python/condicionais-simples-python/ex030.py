# -*- coding: UTF-8 -*-
#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input("Digite um número inteiro: "))
print("===| TESTE MATEMÁTICO |===\n")

if num % 2 == 0:
    print(f"O número {num} digitado é par!")
else:
    print(f"O número {num} digitado é ímpar!")

print("\n===| FIM DO TESTE |===\n")