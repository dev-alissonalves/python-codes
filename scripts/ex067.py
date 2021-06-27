#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
from time import sleep

print("\n============ TABUADA DINÂMICA ============\n")
cont = 0
while True:
    n = int(input("Informe um número: "))
    if n < 0:
        break
    else:
        print("--------------------------------------------------")
        print(f"\033[7;42mTABUADA DE {n}\033[m\n")
        while cont < 11:       
            print(f"{n} X {cont} = {n*cont}")
            cont += 1
        print(f"\033[41mTABUADA DE {n} FINALIZADA!\033[m\n")
        print("--------------------------------------------------\n")
        cont = 0

print("verificando incosistência...")
sleep(3)
print("------>   \033[41mERRO!\033[m   <------")
print("\033[41mO número informado é um número negativo!\033[m")
print("\n============ TABUADA DINÂMICA ============\n")