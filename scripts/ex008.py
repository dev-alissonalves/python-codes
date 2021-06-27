# -*- coding: UTF-8 -*-
#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n1 = float(input("Informe o tamanho do material em metros: "))
cent = (n1*100)
milim = (n1*1000)
print("O valor informado convertido em centímetros é: {:.2f}cm\nE em milímetros é: {:.2f}mm".format(cent,milim))