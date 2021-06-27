# -*- coding: UTF-8 -*-
#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:– EQUILÁTERO: todos os lados iguais – ISÓSCELES: dois lados iguais, um diferente – ESCALENO: todos os lados diferentes


print("-=-=--=-=- |FORMAÇÃO DE TRIÂNGULOS| -=-=--=-=-")
n1 = float(input("INFORME O COMPRIMENTO DA 1° RETA: "))
n2 = float(input("INFORME O COMPRIMENTO DA 2° RETA: "))
n3 = float(input("INFORME O COMPRIMENTO DA 3° RETA: "))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("\nÉ POSSÍVEL FORMAR UM TRIÂNGULO A PARTIR DESSAS MEDIDAS!\n")
    print("[Digite (1) para saber qual tipo de triângulo será criado]")
    print("[Digite (2) para sair do programa]\n")
    operação = int(input("OPÇÃO: "))
    if operação == 1:
        if n1 == n2 and n1 == n3:
            print("\nO TRIÂNGULO CRIADO SERÁ EQUILÁTERO.\n")
        elif n1 == n2 or n1 == n3:
            print("\nO TRIÂNGULO CRIADO SERÁ ISÓSCELES.\n")
        else:
            print("\nO TRIÂNGULO CRIADO SERÁ ESCALENO.\n")
    else:
        exit()
else:
    print("\nNÃO É POSSÍVEL FORMAR UM TRIÂNGULO A PARTIR DESSAS MEDIDAS!\n")