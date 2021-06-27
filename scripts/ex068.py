#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
print("============ GAME MASTER - (PAR OU ÍMPAR) ============\n")
vitorias = 0
total = 0

while True:
    n = int(input("Informe um número: "))
    jogada = str(input("P/I: ")).strip().upper()[0]
    print(jogada)
    computador = randint(1,10)
    total = n+computador
    resultado = total % 2 == 0
    
    if resultado == True and jogada == "P":
        print(f"\nWow - Você venceu!\nO computador jogou {computador} e você jogou {n}.\nO total foi de {total} - DEU PAR!\n")
        vitorias += 1
    elif resultado == False and jogada == "I":
        print(f"\nWow - Você venceu!\nO computador jogou {computador} e você jogou {n}.\nO total foi de {total} - DEU IMPAR!\n")
        vitorias += 1
    else:
        print(f"\nAaaaarghh - Você perdeu!\nO computador jogou {computador} e você jogou {n}.\nO total foi de {total} - DEU ÍMPAR!\n")
        break
print(f"\n============ GAME OVER ============\nVocê venceu {vitorias} vezes!\n")
