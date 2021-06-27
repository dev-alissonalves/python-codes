#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import date
ano_atual = date.today().year

def voto(ano):
    idade = ano_atual-ano
    if idade >= 18 and idade < 65:
        return ("VOTO OBRIGATÓRIO!")
    elif idade >= 65: 
        return ("VOTO OPCIONAL!")
    elif idade < 18 and idade >= 16:
        return ("VOTO OPCIONAL!")
    else:
        return ("VOTO NEGADO!")

ano_nascimento = int(input("Informe o ano do seu nascimento: "))
resp = voto(ano_nascimento)
print(resp)