# -*- coding: UTF-8 -*-
#Exercício Python 48: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

print("-=-=--=-=- |AMOSTRAGEM MÚLTIPLOS DE 3| -=-=--=-=-\n")
soma = 0
qtd_valores = 0
for cont in range (1, 501):
    if cont % 3 == 0 and cont % 2 != 0: #só soma números que forem ímpares e múltiplos de 3
        qtd_valores += 1 #acumulador que recebe a quantidade de números somados
        soma += cont #acumulador que recebe a soma total dos valores encontrados
print(f"A soma de todos os {qtd_valores} números ímpares que são múltiplos de 3 entre 1 e 500 é = {soma}\n")
print("-=-=--=-=- |AMOSTRAGEM MÚLTIPLOS DE 3| -=-=--=-=-\n")