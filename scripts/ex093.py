#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

cadastro = dict()
gols = list()
print()
print('========----- CADASTRO CAMPEONATO BRASILEIRO -----========')
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print()
cadastro["NOME"] = str(input("Informe o seu nome: "))
partidas = int(input(f"Quantas partidas você jogou, {cadastro['NOME']}: "))
print()
cadastro["PARTIDAS"] = partidas
for g in range(0,partidas):
    gol = (int(input(f"Quantos gols na partida {g+1}: ")))
    gols.append(gol)

cadastro["GOLS"] = gols
cadastro["TOTAL"] = sum(gols)
print()
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print()
print(cadastro)
print()
print("-=-=-=-=-=-=-=-=-=-   RESUMO GERAL   =-=-=-=-=-=-=-=-=-=-=")
print()
for k, v in cadastro.items():
    print(f"O Campo {k} tem valor [{v}]")
print()
print("-=-=-=-=-=-=-=-=-=-    PERFOMANCE    =-=-=-=-=-=-=-=-=-=-=")
print()

print(f"O jogador {cadastro['NOME']} jogou {cadastro['PARTIDAS']} partidas.")
for i, v in enumerate(cadastro["GOLS"]):
    print(f"    => Na partida {i+1}, fez {v} Gol(s).")
print(f"Foi um total de {cadastro['TOTAL']} gol(s).")
print()
print('========-----      CAMPEONATO BRASILEIRO     -----========')
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")