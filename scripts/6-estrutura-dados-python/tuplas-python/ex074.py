#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
valor = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)) 
menor = sorted(valor)

print(f"\nOs valores sorteados foram: {valor}")

#modo1 - utilizando lógica
print(f"O menor valor sorteado foi o número: {menor[0]}\nE o maior valor foi o número: {menor[len(valor)-1]}\n")

#modo2 - utilizando o método pronto do python
print(f"O menor valor sorteado foi o número: {min(valor)}\nE o maior valor foi o número: {max(valor)}\n")
    