#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista_num = list()  
while True:
    valor = int(input("\nDigite um número: "))
    if valor not in lista_num:
        lista_num.append(valor)
        print("Valor cadastrado com sucesso!")
        print()
    else:
        print("Valor já cadastrado, não será adicionado...")
        print()
    
    op = ""
    op = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    
    if op == "N":
        break
    print()
lista_num.sort()
print("-=="*30)
print(f"Os valores digitados foram: {lista_num}")