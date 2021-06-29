# -*- coding: UTF-8 -*-
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input("Qual o valor do produto? R$ "))
preco = preco - (preco*10)/100
print("O valor do produto com desconto é: R$ {}".format(preco))