# -*- coding: UTF-8 -*-
#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:– à vista dinheiro/cheque: 10% de desconto – à vista no cartão: 5% de desconto – em até 2x no cartão: preço formal – 3x ou mais no cartão: 20% de juros
from time import sleep
print("-=-=--=-=- |PORTO INFORMÁTICA & ACESSÓRIOS| -=-=--=-=-")
print("-------------------------------------------------------\n")
print("-> DESEJA ANALISAR NOSSO CATÁLOGO DE PRODUTOS?\nDIGITE [1] PARA ACESSAR CATÁLOGO\nDIGITE [0] PARA SAIR DO SISTEMA\n")
op = int(input("AGUARDANDO: "))

if op == 1:
    print("-=-=--=-=- |## acessando banco de dados ##| -=-=--=-=-")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    sleep(1)
    print(".\n")
    print("-=-=--=-=- |## LISTAGEM DE PRODUTOS ##| -=-=--=-=-")
    print("[cod_prod 101] - HD EXTERNO - R$ 299,00")
    print("[cod_prod 102] - SSD KINGSPEC - R$ 300,00")
    print("[cod_prod 103] - MEMÓRIA RAM DESKTOP 2GB - R$ 80,00")
    print("[cod_prod 104] - MEMÓRIA RAM NOTEBOOK 2GB - R$ 130,00")
    print("[cod_prod 105] - PLACA DE REDE WI-FI - R$ 80,00\n")
    print("[PARA COMPRAR INFORME O CÓDIGO DO PRODUTO]")
    print("[PARA SAIR DIGITE (0)]\n")
    prod = int(input("AGUARDANDO: "))
    if prod == 101:
        valorBase = 299
        print("HD EXTERNO - [SELECIONADO]\n")

        print("-=-=--=-=- |## PROCESSANDO COMPRA... ##| -=-=--=-=-")
        sleep(1)
        print(".")
        sleep(1)
        print(".")
        sleep(1)
        print(".")
        sleep(1)
        print(".\n")

        print("|DIGITE A FORMA DE PAGAMENTO|")
        print("[1] - À VISTA NO DINHEIRO - 10% DE DESCONTO")
        print("[2] - À VISTA NO CARTÃO - 5% DE DESCONTO")
        print("[3] - 2X NO CARTÃO - 299,00")
        print("[4] - 3X OU MAIS - 20% DE JUROS\n")
        pg_forma = int(input("AGUARDANDO: "))
        if pg_forma == 1:
            preco_pagar = valorBase - (valorBase*10)/100
            print(f"VALOR A PAGAR: R$ {preco_pagar:.2f}\n")
        elif pg_forma == 2:
            preco_pagar = valorBase - (valorBase*5)/100
            print(f"VALOR A PAGAR: R$ {preco_pagar:.2f}\n")
        elif pg_forma == 3:
            preco_pagar = valorBase/2
            print(f"VALOR DA PARCELA (1/2): R$ {preco_pagar:.2f}\n")
        elif pg_forma == 4:
            parcelas = int(input("Em quantas parcelas? "))
            preco_pagar = valorBase + (valorBase*20)/100
            print(f"VALOR A PAGAR: (1+{parcelas-1}) de R$ {(preco_pagar/parcelas):.2f}\n")
        else:
            print("Algo deu errado...\nTente executar novamente!")
    elif prod == 102:
        valorBase = 300
        print("SSD KINGSPEC - [SELECIONADO]\n")

        print("-=-=--=-=- |## PROCESSANDO COMPRA... ##| -=-=--=-=-")
        sleep(1)
        print(".")
        sleep(1)
        print(".")
        sleep(1)
        print(".")
        sleep(1)
        print(".\n")

        print("|DIGITE A FORMA DE PAGAMENTO|")
        print("[1] - À VISTA NO DINHEIRO - 10% DE DESCONTO")
        print("[2] - À VISTA NO CARTÃO - 5% DE DESCONTO")
        print("[3] - 2X NO CARTÃO - 299,00")
        print("[4] - 3X OU MAIS - 20% DE JUROS\n")
        pg_forma = int(input("AGUARDANDO: "))
        if pg_forma == 1:
            preco_pagar = valorBase - (valorBase*10)/100
            print(f"VALOR A PAGAR: R$ {preco_pagar:.2f}\n")
        elif pg_forma == 2:
            preco_pagar = valorBase - (valorBase*5)/100
            print(f"VALOR A PAGAR: R$ {preco_pagar:.2f}\n")
        elif pg_forma == 3:
            preco_pagar = valorBase/2
            print(f"VALOR DA PARCELA (1/2): R$ {preco_pagar}\n")
        elif pg_forma == 4:
            parcelas = int(input("Em quantas parcelas? "))
            preco_pagar = valorBase + (valorBase*20)/100
            print(f"VALOR A PAGAR: (1+{parcelas-1}) de R$ {(preco_pagar/parcelas):.2f}\n")
        else:
            print("Algo deu errado...\nTente executar novamente!")
    elif prod == 103:
        valorBase = 80
        print("MEMÓRIA RAM DESKTOP 2GB - [SELECIONADO]\n")

        print("-=-=--=-=- |## PROCESSANDO COMPRA... ##| -=-=--=-=-")
        sleep(1)
        print(".")
        sleep(1)
        print(".")
        sleep(1)
        print(".")
        sleep(1)
        print(".\n")

        print("|DIGITE A FORMA DE PAGAMENTO|")
        print("[1] - À VISTA NO DINHEIRO - 10% DE DESCONTO")
        print("[2] - À VISTA NO CARTÃO - 5% DE DESCONTO")
        print("[3] - 2X NO CARTÃO - 299,00")
        print("[4] - 3X OU MAIS - 20% DE JUROS\n")
        pg_forma = int(input("AGUARDANDO: "))
        if pg_forma == 1:
            preco_pagar = valorBase - (valorBase*10)/100
            print(f"VALOR A PAGAR: R$ {preco_pagar:.2f}\n")
        elif pg_forma == 2:
            preco_pagar = valorBase - (valorBase*5)/100
            print(f"VALOR A PAGAR: R$ {preco_pagar:.2f}\n")
        elif pg_forma == 3:
            preco_pagar = valorBase/2
            print(f"VALOR DA PARCELA (1/2): R$ {preco_pagar:.2f}\n")
        elif pg_forma == 4:
            parcelas = int(input("Em quantas parcelas? "))
            preco_pagar = valorBase + (valorBase*20)/100
            print(f"VALOR A PAGAR: (1+{parcelas-1}) de R$ {(preco_pagar/parcelas):.2f}\n")
        else:
            print("Algo deu errado...\nTente executar novamente!")
    elif prod == 104:
        valorBase = 130
        print("MEMÓRIA RAM NOTEBOOK 2GB - [SELECIONADO]\n")

        print("-=-=--=-=- |## PROCESSANDO COMPRA... ##| -=-=--=-=-")
        sleep(1)
        print(".")
        sleep(1)
        print(".")
        sleep(1)
        print(".")
        sleep(1)
        print(".\n")

        print("|DIGITE A FORMA DE PAGAMENTO|")
        print("[1] - À VISTA NO DINHEIRO - 10% DE DESCONTO")
        print("[2] - À VISTA NO CARTÃO - 5% DE DESCONTO")
        print("[3] - 2X NO CARTÃO - 299,00")
        print("[4] - 3X OU MAIS - 20% DE JUROS\n")
        pg_forma = int(input("AGUARDANDO: "))
        if pg_forma == 1:
            preco_pagar = valorBase - (valorBase*10)/100
            print(f"VALOR A PAGAR: R$ {preco_pagar:.2f}\n")
        elif pg_forma == 2:
            preco_pagar = valorBase - (valorBase*5)/100
            print(f"VALOR A PAGAR: R$ {preco_pagar:.2f}\n")
        elif pg_forma == 3:
            preco_pagar = valorBase/2
            print(f"VALOR DA PARCELA (1/2): R$ {preco_pagar:.2f}\n")
        elif pg_forma == 4:
            parcelas = int(input("Em quantas parcelas? "))
            preco_pagar = valorBase + (valorBase*20)/100
            print(f"VALOR A PAGAR: (1+{parcelas-1}) de R$ {(preco_pagar/parcelas):.2f}\n")
        else:
            print("Algo deu errado...\nTente executar novamente!")
    elif prod == 105:
        valorBase = 80
        print("PLACA DE REDE WI-FI - [SELECIONADO]\n")

        print("-=-=--=-=- |## PROCESSANDO COMPRA... ##| -=-=--=-=-")
        sleep(1)
        print(".")
        sleep(1)
        print(".")
        sleep(1)
        print(".")
        sleep(1)
        print(".\n")

        print("|DIGITE A FORMA DE PAGAMENTO|")
        print("[1] - À VISTA NO DINHEIRO - 10% DE DESCONTO")
        print("[2] - À VISTA NO CARTÃO - 5% DE DESCONTO")
        print("[3] - 2X NO CARTÃO - 299,00")
        print("[4] - 3X OU MAIS - 20% DE JUROS\n")
        pg_forma = int(input("AGUARDANDO: "))
        if pg_forma == 1:
            preco_pagar = valorBase - (valorBase*10)/100
            print(f"VALOR A PAGAR: R$ {preco_pagar:.2f}\n")
        elif pg_forma == 2:
            preco_pagar = valorBase - (valorBase*5)/100
            print(f"VALOR A PAGAR: R$ {preco_pagar:.2f}\n")
        elif pg_forma == 3:
            preco_pagar = valorBase/2
            print(f"VALOR DA PARCELA (1/2): R$ {preco_pagar:.2f}\n")
        elif pg_forma == 4:
            parcelas = int(input("Em quantas parcelas? "))
            preco_pagar = valorBase + (valorBase*20)/100
            print(f"VALOR A PAGAR: (1+{parcelas-1}) de R$ {(preco_pagar/parcelas):.2f}\n")
        else:
            print("Algo deu errado...\nTente executar novamente!")

    else:
        print("SAINDO...")
        print(".")
        sleep(1)
        print(".")
        sleep(1)
        print(".")
        sleep(1)
        print(".")
        print("-=-=--=-=- |PORTO INFORMÁTICA & ACESSÓRIOS| -=-=--=-=-\n")
        exit()
else:
    print("SAINDO...")
    print(".")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    print("-=-=--=-=- |PORTO INFORMÁTICA & ACESSÓRIOS| -=-=--=-=-\n")
    exit()