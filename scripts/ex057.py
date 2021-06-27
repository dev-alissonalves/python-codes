# -*- coding: UTF-8 -*-
#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
c = 1
while c != 0:
    sexo = str(input("INFORME SEU SEXO [M/F]: ")).strip().upper()[0]
    if sexo != "F" and sexo != "M":
        print("Dados inválidos - Tente novamente!\n")
        c = 1
    elif sexo == "F" or sexo == "M":
        print(f"\nSexo [{sexo}] cadastrado com sucesso!\n")
        c = 0

#Outra maneira de se fazer
#sexo = str(input("INFORME SEU SEXO [M/F]: ")).strip().upper()[0]
'''while sexo not in "MmFf":
    print("Dados inválidos - Tente novamente!\n")
    sexo = str(input("INFORME SEU SEXO [M/F]: ")).strip().upper()[0]
print(f"\nSexo [{sexo}] cadastrado com sucesso!\n")'''