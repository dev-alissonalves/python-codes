# -*- coding: UTF-8 -*-
#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input("Informe o nome de sua cidade: ")).lstrip().upper()
#retira espaços a esquerda e deixa tudo em maiúsculo
print(cidade)
resultado = "SANTO" in cidade[:5]
print(resultado)