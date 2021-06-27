#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, 
# que é a condição de parada. No final, mostre quantos números foram digitados e 
# qual foi a soma entre eles (desconsiderando o flag).

print("\n============ JOGO DOS NÚMEROS ============\n")
n = int(input("Informe um número inteiro: "))
soma = 0
cont = 0
while n != 999:
    cont += 1
    soma += n
    n = int(input("Informe um outro número inteiro [999 PARA PARAR]: "))

print(f"\nVocê digitou \033[41m[{cont}]\033[m número(s)\nA soma deles é = \033[41m[{soma}]\033[m\n")
print("FIM!")
print("============ JOGO DOS NÚMEROS ============\n")