#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista_num = []
lista_par = []
lista_impar = []

while True:
    numero = int(input("\nInforme um valor: "))
    lista_num.append(numero)
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
    op = ""
    op = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if op == "N":
        break
print(f"A lista completa é: {lista_num}")
print(f"A lista de números pares é: {lista_par}")
print(f"A lista de números ímpares é: {lista_impar}")