# -*- coding: UTF-8 -*-
#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

#CÓDIGO DE CORES PARA EXERCÍCIOS
#\033[32m
from time import sleep
print("\n\033[;;44m-=-=--=-=-  |SISTEMA DE CRÉDITO IMOBILIÁRIO|  -=-=--=-=-\033[m")
print("--"*28)
print("#"*10 +" \033[;31;mDIGITE AS INFORMAÇÕES PARA CONSULTA\033[m " +"#"*10)

valor_imovel = float(input("\nQUAL O VALOR ESTIMADO DO IMÓVEL A SER ADQUIRIDO? R$ - "))
salario_comprador = float(input("QUAL O VALOR BRUTO DO SEU SALÁRIO? R$ - "))
anos_financiamento = int(input("EM QUANTOS ANOS O SENHOR DESEJA QUITAR A CASA? "))
print("\n")
print("#"*15 +"    \033[;;44mPROCESSANDO... \033[m    " +"#"*15)
print("\n")
sleep(3)
percentualValido = (salario_comprador * 30)/100
valor_prestacao = valor_imovel/(anos_financiamento*12)

if valor_prestacao > percentualValido:
    print("\n\033[;;41m### RENDA INCOMPATÍVEL - EMPRÉSTIMO NEGADO! ###\033[m\n")
    print(f"A SUA PRESTAÇÃO DE R$: {valor_prestacao:.2f} É MAIOR QUE R$: {percentualValido:.2f} QUE CORRESPONDE A 30 % DO SEU SALÁRIO.\n")
    print("#"*15 +"    \033[;;44mFINALIZANDO... \033[m    " +"#"*15)
    sleep(3)
    print("\033[;;44m-=-=--=-=-  |SISTEMA DE CRÉDITO IMOBILIÁRIO|  -=-=--=-=-\033[m\n")
    sleep(3)
    exit()
else:
    print("\033[1;31;42m###### RENDA COMPATÍVEL - EMPRÉSTIMO APROVADO! ######\033[m")
    print(f"SUA PARCELA MENSAL SERÁ DE: R$ {valor_prestacao:.2f} EM {anos_financiamento} ANOS.")
    operacao = int(input("\n[DIGITE (1) PARA ACEITAR O EMPRÉSTIMO]\n[DIGITE (0) PARA REJEITAR E SAIR DO SISTEMA] - "))
    if operacao == 1:
        print("\n")
        print("#"*15 +"    \033[;;44mPROCESSANDO... \033[m    " +"#"*15+"\n")
        sleep(3)
        print(f"\033[7mO valor de R$: {valor_imovel:.2f} está disponível para saque.\nProcure a agência do Banco do Brasil mais próxima.\033[m\n")
        print("\033[;;44m-=-=--=-=-  |SISTEMA DE CRÉDITO IMOBILIÁRIO|  -=-=--=-=-\033[m\n")
    else:
        print("\n")
        print("#"*15 +"    \033[;;44mFINALIZANDO... \033[m    " +"#"*15)
        print("\n")
        sleep(3)
        print("\033[;;44m-=-=--=-=-  |SISTEMA DE CRÉDITO IMOBILIÁRIO|  -=-=--=-=-\033[m\n")
        sleep(3)
        exit()
        