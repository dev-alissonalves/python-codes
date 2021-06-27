# -*- coding: UTF-8 -*-
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Quantos KM você percorreu durante o aluguel? "))
dias = int(input("Quantos dias de aluguel? "))
valor1 = km*0.15
valor2 = dias*60
soma = valor1+valor2

print("O valor a ser pago é: R$ {:.2f}".format(soma))
