# -*- coding: UTF-8 -*-
#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

print("-=-=--=-=- ANO BISSEXTO OU NÃO? -=-=--=-=-")
ano = int(input("INFORME QUAL ANO DESEJA TESTAR: [INFORME 0 PARA ANALISAR O ANO ATUAL] --> "))
if ano == 0:
    ano = date.today().year

if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ANO DE {ano} informado é BISSEXTO")
else:
    print(f"O ANO DE {ano} informado NÃO é BISSEXTO")

print("-=-=--=-=- FIM DO PROGRAMA -=-=--=-=-\n")