# -*- coding: UTF-8 -*-
#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input("Digite uma frase inspiradora qualquer: ")).strip().upper()
quantidade = frase.count("A")
prim_posicao = frase.find("A")+1 
ult_posicao = frase.rfind("A")+1
print(f"A letra 'A' aparece {quantidade} vezes!")
print(f"A letra 'A' na primeira vez aparece na posição: {prim_posicao}")
print(f"A letra 'A' na última vez aparece na posição: {ult_posicao}")