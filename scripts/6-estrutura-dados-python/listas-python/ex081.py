#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados. 
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista_num = []
cont = 0
while True:
    numero = int(input("\nInforme um número: "))
    lista_num.append(numero)
    cont += 1
        
    op = ""
    op = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if op == "N":
        break
    
lista_num.sort(reverse=True)
print()
print(f"Foram digitados: {cont} número(s).")    
print(f"A lista de valores digitados foi: {lista_num}")
if 5 in lista_num:
    print("O valor 5 faz parte desta lista!")
else:
    print("Valor 5 não foi encontrado nessa lista!")