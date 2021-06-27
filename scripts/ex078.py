#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
print("\n")
menor = 0
maior = 0
for valores in range(0, 5):
    lista.append(int(input(f"Informe o {valores+1}º valor: ")))
    if valores == 0:
        menor = lista[valores]
        maior = lista[valores]
    else:
        if lista[valores] < menor:
            menor = lista[valores]
        elif lista[valores] > maior:
            maior = lista[valores]


print(f"Os valores digitados foram: {lista}")
print(f"O maior valor digitado foi: {maior} nas posições: ", end="")
for cont, val in enumerate(lista):
        if val == maior:
            print(f"{cont}... ", end="") 

print()
print(f"O menor valor digitado foi: {menor} nas posições: ", end="")
for cont, val in enumerate(lista):
        if val == menor:
            print(f"{cont}... ", end="") 
print("\n")

#modo mais básico sem mostrar a posição
"""
print("\n")
print("-"*40)
print("Valores adicionados com sucesso!")
print(f"O maior valor digitado na lista foi: {max(lista)}")
print(f"O menor valor digitado na lista foi: {min(lista)}")
print("-"*40)
print("\n")"""