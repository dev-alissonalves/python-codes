#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

def aumentar(preço, taxa):
    res = preço + (preço * taxa/100)
    return res
    
def diminuir(preço, taxa): 
    res = preço - (preço * taxa/100)
    return res

def dobro(preço):
    return preço*2

def metade(preço):
    return preço/2
