#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("\n============ BANCO PORTO ============\n")
saque = int(input("Qual valor será sacado? R$: "))
total = saque
ced = 50
qtd = 0

while True:
    if total >= ced:
        total -= ced
        qtd += 1
    else:
        if qtd > 0:
            print(f"Total de {qtd} cédulas de R$: {ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        qtd = 0
        if total == 0:
            break
print("\n============ VOLTE SEMPRE AO BANCO PORTO ============\n")