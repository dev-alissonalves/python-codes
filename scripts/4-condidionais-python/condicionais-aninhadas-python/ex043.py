# -*- coding: UTF-8 -*-
#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:– IMC abaixo de 18,5: Abaixo do Peso – Entre 18,5 e 25: Peso Ideal – 25 até 30: Sobrepeso – 30 até 40: Obesidade – Acima de 40: Obesidade Mórbida

from time import sleep
print("-=-=--=-=- |HEALTH EDUCATION| -=-=--=-=-\n")

peso = float(input("Informe o seu peso atual: (KG) "))
altura = float(input("Informe a sua altura atual: (M) "))
imc = peso / (altura**2)

print("CLASSIFICANDO...")
sleep(3)
print("\n-=-=--=-=- |STATUS| -=-=--=-=-\n")

if imc < 18.5:
    print(f"IMC = {imc:.1f}")
    print("CLASSIFICAÇÃO: \033[;;41m[ABAIXO DO PESO IDEAL]\033[m")
    print("OBESIDADE (GRAU) [0]\n")
elif 18.5 <= imc < 25:
    print(f"IMC = {imc:.1f}")
    print("CLASSIFICAÇÃO: \033[;;42m[PESO IDEAL]\033[m")
    print("OBESIDADE (GRAU) [0]\n")
elif 25 <= imc < 30:
    print(f"IMC = {imc:.1f}")
    print("CLASSIFICAÇÃO: \033[7;31;43m[SOBREPESO]\033[m")
    print("OBESIDADE (GRAU) [1]\n")
elif 30 <= imc < 40: 
    print(f"IMC = {imc:.1f}")
    print("CLASSIFICAÇÃO: \033[;;41m[OBESIDADE]\033[m")
    print("OBESIDADE (GRAU) [2]\n")
elif imc > 40:
    print(f"IMC = {imc:.1f}")
    print("CLASSIFICAÇÃO: \033[;;41m[OBESIDADE GRAVE]\033[m")
    print("OBESIDADE (GRAU) [3]\n")


