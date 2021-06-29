# -*- coding: UTF-8 -*-
#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print("============ TABUADA AUTOMÁTICA ============")
n1 = int(input("Informe um número: "))
print(f"A tabuada de {n1} é: \n")
for cont in range (1, 11):
    print("{}X{} = {}" .format(n1, cont, n1*cont))
print("\n============ TABUADA AUTOMÁTICA ============")