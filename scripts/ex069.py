#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos.B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos

print("\n--== CADASTRO DE PESSOAS ==--")
print("-----------------------------\n")

maior = 0
masculino = 0
feminino = 0
mulher_20anos = 0
idade = 0

while True:
    idade = int(input("INFORME A IDADE: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("INFORME O SEXO [M/F]: ")).strip().upper()[0]
    print("\nDADOS CADASTRADOS!\n")
    if idade > 18:
        maior+= 1 
    if sexo == "M":
        masculino +=1
    if sexo == "F" and idade < 20:
        mulher_20anos += 1
    op = " "
    while op not in "SN":
        op = str(input("Deseja continuar? [S/N]: ")).strip().upper()
    if op == "N":
        break
print(f"\nForam cadastradas {maior} pessoa(s) com mais de 18 anos.\nObtivemos um número de {masculino} homem(s) cadastrado(s).\nNo total {mulher_20anos} mulheres tem menos de 20 anos de idade.\n")

