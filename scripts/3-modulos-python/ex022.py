# -*- coding: UTF-8 -*-
#  Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = input("Informe o seu nome completo: ")
print("O nome informado em MAIÚSCULAS é: {}".format(nome.upper()))
print("O nome informado em minúsculas é: {}".format(nome.lower()))
espaços = nome.count(" ")
tamanho = len(nome)-espaços
print(f"A quantidade de letras sem espaços é: {tamanho}")
primeiro_nome = len(nome.split()[0])
#Ou pode usar o nome.find(" ") para encontrar o primeiro espaço
print(f"A quantidade de letras do seu primeiro nome é: {primeiro_nome}")