# -*- coding: UTF-8 -*-
#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
print("\n============ OPERA SYSTEM ============\n")
valor1 = float(input("Olá, digite um valor: "))
valor2 = float(input("Digite outro valor: "))
operacao = 0
soma = 0
multiplicar = 0
maior = 0
while operacao != 5:
    print("\n[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR\n[ 4 ] NOVOS NÚMEROS\n[ 5 ] QUIT\n")
    operacao = int(input("QUAL OPERAÇÃO DEVO REALIZAR? "))
    if operacao == 1:
        print("SOMAR [SELECIONADO]\nPROCESSANDO...\n")
        sleep(3)
        soma = valor1 + valor2
        print(f"SOMA = \033[41m{soma}\033[m\n") 
    elif operacao == 2:
        multiplicar = valor1 * valor2
        print("MULTIPLICAR [SELECIONADO]\nPROCESSANDO...\n")
        sleep(3)
        print(f"MULTIPLICAÇÃO = \033[41m{multiplicar}\033[m\n")
    elif operacao == 3:
        print("MAIOR [SELECIONADO]\nPROCESSANDO...\n")
        sleep(3)
        if valor1 > valor2:
            maior = valor1
        elif valor1 == valor2:
            print(f"O número \033[41m{valor1}\033[m é igual ao valor \033[41m{valor2}\033[m")
            maior = valor1  
        else:
            maior = valor2
        
        print(f"O maior número é: \033[41m{maior}\033[m")
    elif operacao == 4:
        print("NOVOS NÚMEROS [SELECIONADO]\nPROCESSANDO...\n")
        sleep(3)
        valor1 = float(input("Digite novamente o valor 1: "))
        valor2 = float(input("Digite novamente o valor 2: "))        

print("\n============ OPERA SYSTEM ============")
print("\nSAINDO...\n")
sleep(3)
