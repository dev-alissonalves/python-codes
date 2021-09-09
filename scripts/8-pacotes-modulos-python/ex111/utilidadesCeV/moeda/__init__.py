def aumentar(preço = 0, taxa = 0, formato = False):
    res = preço + (preço * taxa/100)
    return res if formato is False else conv(res)
    
def diminuir(preço = 0, taxa = 0, formato = False): 
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

def resumo(preço = 0, taxa_aumento = 10, taxa_redução = 20):
    print("\n")
    print("-"*40)
    print("RESUMO DO VALOR".center(40))
    print("-"*40)
    print(f"Preço analisado: \t\t{conv(preço)}")
    print(f"Dobro do valor é: \t\t{dobro(preço, True)}")
    print(f"Aumento do valor em {taxa_aumento}% é: \t{aumentar(preço, taxa_aumento, True)}")
    print(f"Redução do valor em {taxa_redução}% é: \t{diminuir(preço, taxa_redução, True)}")
    print(f"Metade do valor é: \t\t{metade(preço, True)}")
    print("\n")