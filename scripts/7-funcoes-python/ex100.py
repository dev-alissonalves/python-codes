#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
def somaPar(lista):
    soma = 0
    for c in lista:
        if c %2 == 0:
            soma += c
    print(f"A soma total dos números pares foi: {soma}")

def sorteia():
    for c in range(1, 6):
        geranum = randint(1, 10)
        numeros.append(geranum)  
    print(f"A lista gerada aleatoriamente foi ---> {numeros}")

#ProgramaPrincipal
numeros = list()
sorteia()
somaPar(numeros)