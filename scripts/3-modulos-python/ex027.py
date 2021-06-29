# -*- coding: UTF-8 -*-
#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("Digite seu nome completo: ")).upper().strip()
separado = nome.split() #Separa a frase em partes
tamanho = len(separado)-1
primeiro_nome = nome.split()[0] #Descobre o primeiro nome
ultimo_nome = nome.split()[tamanho] #O último nome é na posição do tamanho da string
print(f"O primeiro nome digitado foi: {primeiro_nome}")
print(f"O último nome digitado foi: {ultimo_nome}")