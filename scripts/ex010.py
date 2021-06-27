# -*- coding: UTF-8 -*-
#Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dólares ela pode comprar.

n1 = float(input("Quanto você tem em dinheiro? R$"))
dólar = 6.0 #Valor atual em abril de 2021
print("Você tem R$ {:.2f} que equivale a {:.2f} em dólar!".format(n1, (n1/dólar)))