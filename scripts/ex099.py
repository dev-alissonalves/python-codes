#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*nums):
    maior = 0
    tam = len(nums)
    for c in nums:
        if c > maior:
            maior = c
    print(f"O maior valor é: {maior}")
    print()

maior(1, 2, 3, 4, 5)
maior(1, 3, 5)
maior(15, 4, 8, 6)
maior(4, 7, 8)
maior(200, 575, 2)
maior(2, 9, 4, 5, 7, 1)
maior()