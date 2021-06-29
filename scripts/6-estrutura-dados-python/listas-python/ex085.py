#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
numeros = [[],[]]
valor = 0

print()
for num in range(1,8):
    valor = int(input(f"Informe o {num}° valor: "))   
    if valor %2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

print()
numeros[0].sort()
numeros[1].sort()
print(f"Os valores pares são: {numeros[0]}")
print(f"Os valores impares são: {numeros[1]}")