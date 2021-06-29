#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela

aluno = {}
aluno["nome"] = str(input("Informe o nome do aluno: "))
aluno["media"] = float(input("Informe a media do aluno: "))
if aluno["media"] >= 7:
    aluno["situação"] = "APROVADO!"
else:
    aluno["situação"] = "REPROVADO!"

print("-="*20)
print(f"Nome do aluno é: {aluno['nome']}")
print(f"A média do aluno foi: {aluno['media']}")
print(f"A situação do aluno é: {aluno['situação']}")
print("-="*20)
print()

#segunda forma de mostrar
for k, v in aluno.items():
    print(f"{k} é {v}")