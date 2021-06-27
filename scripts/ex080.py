#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista_num = []
for cont in range(0, 5):
    numero = int(input(f"\nInforme o {cont+1}º número: "))
    if cont == 0 or numero > lista_num[-1]: # -1 vai até o último elemento da lista
        lista_num.append(numero)
        print("Valor adicionado no final da lista...")
    else: 
        i = 0
        while i < len(lista_num):
            if numero <= lista_num[i]:
                lista_num.insert(i, numero)
                print(f"Valor adicionado na {i}º posição...")
                break
            i += 1

print(lista_num)