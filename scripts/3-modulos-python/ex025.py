# -*- coding: UTF-8 -*-
# Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input("Informe seu nome completo: ")).strip().upper()
procura_nome = "SILVA" in nome
print(f"Seu nome tem Silva? {procura_nome}")