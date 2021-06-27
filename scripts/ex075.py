#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.

conjunto = int(input("Informe um número: ")), int(input("Informe outro número: ")), int(input("Informe mais um número: ")), int(input("Informe o último número: "))
print(f"\nOs números digitados foram: {conjunto}")
print(f"O número 9 apareceu: {conjunto.count(9)} vezes.")
if 3 in conjunto:
    print(f"O primeiro valor 3 apareceu na {conjunto.index(3)+1}º posição")
else:
    print("O valor 3 não foi encontrado dentro da estrutura!")
print("Os números pares digitados foram: ", end="")
for num in conjunto:
    if num %2 == 0:
        print(num, end=" ")

print("\n")