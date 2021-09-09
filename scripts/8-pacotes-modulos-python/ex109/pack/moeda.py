#Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

def aumentar(preço = 0, taxa = 0, formato = False):
    res = preço + (preço * taxa/100)
    return res if formato is False else conv(res)
    
def diminuir(preço = 0, taxa = 0, format = False): 
    res = preço - (preço * taxa/100)
    return res if formato is False else conv(res)

def dobro(preço = 0, formato = False):
    res = preço*2
    return res if formato is False else conv(res)

def metade(preço = 0, formato = False):
    res = preço/2
    return res if formato is False else conv(res)

def conv(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')