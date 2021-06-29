# -*- coding: UTF-8 -*-
#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
pesoAtual = 0
pesoMenor = 0
pesoMaior = 0

for cont in range (1, 6):
    pesoAtual = float(input(f"PESO DA [{cont}º] PESSOA: ")) 
    if cont == 1:
        pesoMaior = pesoAtual
        pesoMenor = pesoAtual
    else: 
        if pesoAtual > pesoMaior:
            pesoMaior = pesoAtual
        elif pesoAtual < pesoMenor:
            pesoMenor = pesoAtual
print(f"\nO menor peso lido foi: \033[42m{pesoMenor} (KG)\033[m\nO maior peso lido foi: \033[7;41m{pesoMaior} (KG)\033[m\n\n")