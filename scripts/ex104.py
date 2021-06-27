#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt("Digite um n: ")

def leiaInt():
    while True:
        valor = input("Digite um valor numérico: ")
        teste = valor.isnumeric()
        while teste != True:
            valor = input("ERRO! Digite um valor numérico: ")
            if valor.isnumeric() == True:
                break
        break
    return valor       
print("-="*20)
valor = leiaInt()
print(f"O valor digitado foi: {valor}")
print("-="*20)