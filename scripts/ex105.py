#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#– total de notas passadas 
#- A maior nota
#- A menor nota    
#– A média da turma
#– A situação (opcional)
from typing import Dict

def notas(n, sit=False):
    data = dict()

    total = maior = menor = soma = media = 0
    data["TOTAL"] = total = len(n)
    data["MAIOR"] = maior = max(n)
    data["MENOR"] = menor = min(n)
    data["MÉDIA"] = media = sum(n)/len(n)
    
    if sit == True:
        if media <= 5:
            data["SITUAÇÃO"] = "PODE MELHORAR!"
        elif media >= 7 and media < 8.5:
            data["SITUAÇÃO"] = "BOA NOTA!"
        elif media >= 8.5:
            data["SITUAÇÃO"] = "EXCELENTE NOTA!"
        else:
            data["SITUAÇÃO"] = "NECESSITA ESTUDAR MAIS!"   
    print(data)


print("-="*20)
lista = list()
qtd = int(input("Informe quantas notas serão inseridas: "))
for c in range(0, qtd):
    valores = 0
    valores = float(input(f"Informe a {c+1}ª nota: "))
    lista.append(valores)

op = input("Deseja imprimir a situação do aluno? [S/N]: ").strip().upper()[0]

if op in "Ss":
    notas(lista, sit=True)
else:
    notas(lista)

print("-="*30)