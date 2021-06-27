#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ("alisson", "alves", "emilly", "tomas", "henrique", "ilza", "avelino", "beta", "isis", "ana beatriz")

for p in palavras:
    print(f"\nNa palavra {p} temos: ", end="--> ")
    for letra in p:
        if letra in "aeiou":
            print(f"{letra}", end=" ") 