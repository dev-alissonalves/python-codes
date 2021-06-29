# -*- coding: UTF-8 -*-
#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
from time import sleep

print("-=-=--=-=- SISTEMA DE VERIFICAÇÃO DE TRÂNSITO -=-=--=-=-\n")
km = int(input("Informe a sua velocidade (KM) atual? "))

if km > 80:
    print("PROCESSANDO...\n")
    sleep(3)
    multa = float((km-80)*7)
    print(f"!!!! MULTADO !!!!\nVocê ultrapassou o limite de velocidade permitido!\nVocê pagará R$ {multa:.2f} de multa!\n")
else:
    print("PROCESSANDO...")
    sleep(3)
    print("O sistema não encontrou nenhuma irregularidade.\nTenha uma ótima viagem!\n")

print("-=-=--=-=- VERIFICAÇÃO FINALIZADA! -=-=--=-=-\n")