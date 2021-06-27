#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
alunos = []
cadastro = []
cont = 1
print()
print("-="*10, "SISTEMA DE BOLETIM ESCOLAR", "-="*10)
while True:
    alunos.append(str(input(f"\nDigite o nome do {cont}º aluno: ")).strip().upper())
    alunos.append(float(input(f"Digite a 1ª nota do aluno: ")))
    alunos.append(float(input("Digite a 2ª nota do aluno: ")))
    media = (alunos[1] + alunos[2])/2
    alunos.append(media)
    cadastro.append(alunos[:])
    alunos.clear()
    media = 0
    cont += 1
    op = ""
    op = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if op == "N":
        break

print()
print("-="*15)
print(f"{'No.':<4}{'NOME':<10}{'MÉDIA':>8}")
print("-="*15)
for i, c in enumerate(cadastro):
    print(f"{(i):<4}{cadastro[i][0]:<10}{cadastro[i][3]:>8.1f}")
while True:
    detalhe = int(input("\nDeseja ver o detalhe de notas de qual aluno? (999 - interrompe): "))
    if detalhe == 999:
        print("\nFinalizando...\n")
        print("-="*10, "SISTEMA DE BOLETIM ESCOLAR", "-="*10)
        print()
        break
    if detalhe < len(cadastro):
        print(f"\nAs Notas de {cadastro[detalhe][0]} são: [{cadastro[detalhe][1]}][{cadastro[detalhe][2]}]")

    

