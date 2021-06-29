#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f"Insira o valor na posição [{i},{j}]: "))

print("\nOs valores que compõe a matriz são: \n")
for k in range(0,3):
    for l in range(0,3):
        print(f"[{matriz[k][l]:^5}]", end=" ")
    print()
print("\n")