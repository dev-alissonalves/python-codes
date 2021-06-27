#Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
# A) valores pares digitados. 
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
pares = []
valor = 0
soma = 0
maior = 0
for i in range(0,3):
    for j in range(0,3):
        valor = int(input(f"Insira o valor na posição [{i},{j}]: "))
        matriz[i][j] = valor
        if valor %2 == 0:
            pares.append(valor)
        if j == 2:
            soma += valor
        if i == 1 and j == 0:
            maior = valor
        else:
            if i == 1 and valor > maior:
                maior = valor
            else:
                valor = maior
            
print("\nOs valores que compõe a matriz são: \n")
for k in range(0,3):
    for l in range(0,3):
        print(f"[{matriz[k][l]:^5}]", end=" ")
    print()

print(f"\nA soma dos valores pares que compõem a matriz é: {sum(pares)}\n")
print(f"A soma dos valores da 3ª coluna é: {soma}\n")
print(f"O maior valor digitado na 2ª linha é: {maior}\n")
print("\n")