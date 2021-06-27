# -*- coding: UTF-8 -*-
#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:– Média abaixo de 5.0: REPROVADO – Média entre 5.0 e 6.9: RECUPERAÇÃO – Média 7.0 ou superior: APROVADO

from time import sleep
print("-=-=--=-=- |SISTEMA EDUCACIONAL| -=-=--=-=-")
nota1 = float(input("Informe a sua nota na unidade 1: "))
nota2 = float(input("Informe a sua nota na unidade 2: "))

media = (nota1 + nota2)/2
print("VERIFICANDO...\n")
sleep(3)
if media < 5:
    print("REPROVADO!")
    print(f"Sua média foi: {media:.1f}\n")
elif media >= 5 and media <= 6.9:
    print("RECUPERAÇÃO!")
    print(f"Sua média foi: {media:.1f}\n")
elif media >= 7:
    print("APROVADO!\nBoas Férias!")
    print(f"Sua média foi: {media:.1f}\n")
