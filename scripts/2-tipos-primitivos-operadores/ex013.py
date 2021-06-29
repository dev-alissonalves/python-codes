# -*- coding: UTF-8 -*-
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salário = float(input("Qual o seu salário: R$ "))
salário = salário + (salário*15)/100
print("O seu salário com aumento é: R$ {:.2f}".format(salário))