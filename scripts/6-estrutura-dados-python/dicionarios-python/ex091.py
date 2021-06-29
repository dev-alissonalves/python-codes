#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter
from time import sleep
rank = list()
data = {
    "jogador1" : randint(1,6),
    "jogador2" : randint(1,6),
    "jogador3" : randint(1,6),
    "jogador4" : randint(1,6)
}
print('========----- JOGO DA SORTE -----========')
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
for k, v in data.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1)
print()
print('=====----- RANKING DE POSIÇÕES -----=====')
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
rank = sorted(data.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(rank):
    print(f"{i+1}º foi o {v[0]} que tirou {v[1]}.")
    sleep(1)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print()