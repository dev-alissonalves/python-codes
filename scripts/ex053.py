# -*- coding: UTF-8 -*-
#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

print("============ VERIFICANDO PALÍNDROMOS ============\n")
frase = str(input("Digite uma frase: ")).strip().upper() #retira espaços e joga tudo pra maiúsculas

frase_separada = frase.split() #separa a frase em palavras
frase_sem_espacos = "".join(frase_separada) #junta as palavras sem espaços
frase_inversa = "" #criando a variável que vai receber a frase inversa
#OUTRO MODO DE SE FAZER SEM O FOR É: 
# FRASE_INVERSA = frase_sem_espacos[::-1]
for percorre_letra in range(len(frase_sem_espacos) - 1, -1, -1): #percorre a frase sem espaço de maneira inversa
    frase_inversa = frase_inversa + frase_sem_espacos[percorre_letra] #vai lendo a frase de maneira inversa e vai guardando na variável frase_inversa

print(f"O inverso de \033[42m[{frase_sem_espacos}]\033[m é \033[41m[{frase_inversa}]\033[m")
if frase_inversa == frase_sem_espacos:
    print("\n\033[7m##### TEMOS UM PALÍNDROMO! #####\033[m\n")
else:
    print("\n\033[7m##### A FRASE DIGITADA NÃO É UM PALÍNDROMO #####\033[m\n")
