#Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial (num=1, show=False):
    f = 1
    if show == False:
        for c in range(num, 0, -1):
            f *= c
        return f
    else:
        for c in range(num, 0, -1):        
            f *= c
            print(c, end="")
            if c > 1:
                print(f" x ", end="")
            else:
                print(end=" = ")    
        return f

valor = int(input("Informe o valor para cálculo: "))
MostraCalculo = str(input("Deseja visualizar o cálculo? [S/N]-: ")).strip().upper()[0]
if MostraCalculo == "S":
    resp = fatorial(valor, True)
    print(resp)
else:
    resp = fatorial(valor, False)
    print(f"O resultado do cálculo fatorial é: {resp}")