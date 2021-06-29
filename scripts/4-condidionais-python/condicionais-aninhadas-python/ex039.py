# -*- coding: UTF-8 -*-
#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
from time import sleep

print("-=-=--=-=- |SISTEMA DE VERIFICAÇÃO DA FORÇA AÉREA BRASILEIRA| -=-=--=-=-")
ano_atual = date.today().year
ano_nascimento = int(input("INFORME OS 4 DÍGITOS DO SEU ANO DE NASCIMENTO: "))
verificarAlistamento = ano_atual-ano_nascimento
if verificarAlistamento == 18:
    print("VERIFICANDO...")
    sleep(3)
    print(f"O CIDADÃO ESTÁ COM {verificarAlistamento} ANOS DE IDADE E ESTÁ APTO PARA ALISTAMENTO MILITAR!\n")
    print("Dirija-se até a Junta de Serviço Militar de sua cidade.\n")
    print("-=-=--=-=- |FAB - ASAS QUE PROTEGEM O PAÍS| -=-=--=-=-\n")
elif verificarAlistamento > 18:
    print("VERIFICANDO...")
    sleep(3)
    tempoExcedente = verificarAlistamento-18
    print("TEMPO EXCEDENTE DE ALISTAMENTO!\n")
    print(f"{tempoExcedente} ANOS DE ATRASO.")
    print("Dirija-se até a Junta de Serviço Militar de sua cidade para regularização de sua situação.\n")
    print("-=-=--=-=- |FAB - ASAS QUE PROTEGEM O PAÍS| -=-=--=-=-\n")
else:
    print("VERIFICANDO...")
    sleep(3)
    tempoRestante = 18-verificarAlistamento
    print("CIDADÃO INAPTO PARA ALISTAMENTO MILITAR!\n")
    print("O cidadão ainda não completou a idade mínima para o alistamento.")
    print(f"Ainda restam {tempoRestante} ANO(S) até para o alistamento.\n")
    print("-=-=--=-=- |FAB - ASAS QUE PROTEGEM O PAÍS| -=-=--=-=-\n")
