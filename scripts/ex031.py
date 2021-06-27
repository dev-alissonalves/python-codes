# -*- coding: UTF-8 -*-
#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
from time import sleep

print("-=-=--=-=- SISTEMA DE VERIFICAÇÃO DE VIAGEM -=-=--=-=-\n")
km = int(input("Informe a distância de sua viagem em KM: "))
if km > 200:
    valor = km*0.45
    print("Calculando viagem...\n")
    sleep(3)
    print(f"Sua viagem tem {km} KM de distância.")
    print(f"O valor de sua passagem será: R$ {valor:.2f}\n")
else:
    print("Calculando viagem...\n")
    sleep(3)
    print(f"Sua viagem tem {km} KM de distância.")
    print(f"O valor de sua passagem será: R$ {(km*0.50):.2f}\n")

print("-=-=--=-=- SISTEMA DE VERIFICAÇÃO DE VIAGEM -=-=--=-=-\n")