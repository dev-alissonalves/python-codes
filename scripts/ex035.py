# -*- coding: UTF-8 -*-
#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print("-=-=--=-=- |FORMAÇÃO DE TRIÂNGULOS| -=-=--=-=-")
n1 = float(input("INFORME O COMPRIMENTO DA 1° RETA: "))
n2 = float(input("INFORME O COMPRIMENTO DA 2° RETA: "))
n3 = float(input("INFORME O COMPRIMENTO DA 3° RETA: "))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("É POSSÍVEL FORMAR UM TRIÂNGULO A PARTIR DESSAS MEDIDAS!")
else:
    print("NÃO É POSSÍVEL FORMAR UM TRIÂNGULO A PARTIR DESSAS MEDIDAS!")
