#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. 
#No final da execução, mostre a média entre todos os valores e qual foi o maior e 
# o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou 
# não continuar a digitar valores.
soma = 0
media = 0
maior = 0
menor = 0
op = 1
cont = 0
while op != 0:
    cont += 1
    n = int(input("Informe um número: "))
    soma += n
    media = soma/cont
    if cont == 1:
        maior = n
        menor = n
    else: 
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

    op = int(input("Deseja continuar? [1-SIM/0-NÃO]: "))
    

print(f"A média dos valores informados é: [{media}]\nO menor valor informado foi: [{menor}]\nO maior valor informado foi: [{maior}]\n")