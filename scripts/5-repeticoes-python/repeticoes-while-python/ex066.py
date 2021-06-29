#Exercício Python 66: Crie um programa que receba vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. Ao final, mostre quantos números foram digitados e qual foi a soma entre eles.

print("\n============ JOGO DOS NÚMEROS ============\n")
cont = 0
soma = 0
while True:
    n = int(input("Informe um número inteiro [999 PARA PARAR]: "))
    if n == 999:
        break
    
    cont += 1
    soma += n
print(f"\nVocê digitou \033[41m[{cont}]\033[m número(s)\nA soma deles é = \033[41m[{soma}]\033[m\n")
print("FIM!")
print("============ JOGO DOS NÚMEROS ============\n")