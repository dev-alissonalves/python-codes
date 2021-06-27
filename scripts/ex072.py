#Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezesete", "dezoito", "dezenove", "vinte")

while True:
    valor = int(input("\nInsira um valor entre [0-20]: "))
    while valor < 0 or valor > 20:
         valor = int(input("\nPor favor, tente novamente!\nInsira um valor entre [0-20]: "))
    
    if valor >= 0 and valor <= 20:
        print(f"Você digitou o número {numeros[valor]}!\n")
         
    op = " "
    while op not in "SN":
        op = str(input("Deseja continuar? [S/N]: " )).strip().upper()[0]
    
    if op == "N":
        break

