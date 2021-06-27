# -*- coding: UTF-8 -*-
#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

from time import sleep
print("-=-=--=-=--=-=--=-=- |SISTEMA FINANCEIRO| -=-=--=-=--=-=--=-=-")
salario = float(input("Caro trabalhardor, informe o valor da sua remuneração: "))
print("PROCESSANDO...\n")
sleep(3)
if salario <= 1250:
    salario = salario + (salario * 15 / 100)
    print(f"Você recebeu um aumento de 15%\nSeu salário atualizado é: R$ {salario:.2f}\n")
else:
    salario = salario + (salario * 10 / 100)
    print(f"Você recebeu um aumento de 10%\nSeu salário atualizado é: R$ {salario:.2f}\n")

print("-=-=--=-=--=-=--=-=- |OPERAÇÃO FINALIZADA| -=-=--=-=--=-=--=-=-")