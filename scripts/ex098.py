#Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada: 
# (A) de 1 ate 10, de 1 em 1 
# (B) de 10 até 0, de 2 em 2 
# (C) uma contagem personalizada.
from time import sleep

def mostraLinha():
    print("-" * 30)

def contador (inicio, fim, passo):
    print("CONTAGEM (A)")
    for c in range(inicio, fim+1, passo):
        print(c, end=" ", flush = True)
        sleep(1)
    print()
    print()    
    print("CONTAGEM (B)")
    for cont in range(fim, inicio-2, -(passo+1)):
        print(cont, end=" ", flush = True)
        sleep(1)
    print()
    print()    
    print("CONTAGEM (C)")
    print("Agora é sua vez de personalizar a contagem!")
    inicio = int(input("Início: "))
    fim = int(input("Fim: "))
    passo = int(input("Passo: "))
    print()
    for a in range(inicio, fim+1, passo):
        print(a, end=" ", flush = True)
        sleep(1)


#CONTAGEM AUTOMÁTICA
mostraLinha()
print("Contagem de números...")
i = 1
f = 10
p = 1
contador(i, f, p)
print()
mostraLinha()
