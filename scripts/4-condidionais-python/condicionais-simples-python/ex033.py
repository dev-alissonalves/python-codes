# -*- coding: UTF-8 -*-
#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print("-=-=--=-=- |SISTEMA DE COMPARAÇÃO NUMÉRICA| -=-=--=-=-")
n1 = int(input("INFORME O NÚMERO 1: "))
n2 = int(input("INFORME O NÚMERO 2: "))
n3 = int(input("INFORME O NÚMERO 3: "))

if n1 > n2 and n1 > n3:
    maior = n1
    print(f"O maior entre os números é: {maior}")
if n2 > n1 and n2 > n3:
    maior = n2
    print(f"O maior entre os números é: {maior}")
if n3 > n1 and n3 > n2:
    maior = n3
    print(f"O maior entre os números é: {maior}")

if n1 < n2 and n1 < n3:
    menor = n1
    print(f"O menor entre os números é: {menor}")
if n2 < n1 and n2 < n3:
    menor = n2
    print(f"O menor entre os números é: {menor}")
if n3 < n1 and n3 < n2:
    menor = n3
    print(f"O menor entre os números é: {menor}")