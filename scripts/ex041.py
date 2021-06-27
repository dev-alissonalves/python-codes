# -*- coding: UTF-8 -*-
#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: – Até 9 anos: MIRIM – Até 14 anos: INFANTIL – Até 19 anos: JÚNIOR – Até 25 anos: SÊNIOR – Acima de 25 anos: MASTER
from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input("Informe os quatro dígitos do seu ano de nascimento: "))

idade = ano_atual - ano_nascimento
print("-=-=--=-=- |SISTEMA ESPORTIVO| -=-=--=-=-\n")
if idade <= 9:
    print(f"\nIDADE = {idade}\nATLETA DA CATEGORIA [MIRIM]\n")
elif idade <= 14:
    print(f"\nIDADE = {idade}\nATLETA DA CATEGORIA [INFANTIL]\n")
elif idade <= 19:
    print(f"\nIDADE = {idade}\nATLETA DA CATEGORIA [JÚNIOR]\n")
elif idade <=25:
    print(f"\nIDADE = {idade}\nATLETA DA CATEGORIA [SÊNIOR]\n")
elif idade > 25:
    print(f"\nIDADE = {idade}\nATLETA DA CATEGORIA [MASTER]\n")
