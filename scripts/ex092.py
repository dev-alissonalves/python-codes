#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
cadastro = dict()
print()
print('========----- CADASTRO RESURSOS HUMANOS -----========')
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print()
cadastro["NOME"] = str(input("Informe o nome: "))
ano_nascimento = int(input("Ano de nascimento (ex.2002): "))
idade = (date.today().year)-ano_nascimento
cadastro["IDADE"] = idade
ctps = int(input("Informe número da sua CTPS (0-NÃO TEM): "))

if ctps != 0:
    cadastro["CTPS"] = ctps
    cadastro["CONTRATAÇÃO"] = int(input("Informe o ano de sua contração: "))
    cadastro["SALÁRIO"] = float(input("Informe o valor do seu salário R$: "))
    cadastro["APOSENTADORIA"] = 65-idade
else:
    cadastro["CTPS"] = "NÃO POSSUI!"
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print()
for k, v in cadastro.items():
    print(f"    - {k} tem o valor: [{v}]")

print()
print('========----- CADASTRO RESURSOS HUMANOS -----========')
print()