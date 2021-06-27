#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

cadastro = list()
jogador = dict()
gols_jogador = list()
gols_total = list()
print()
print('========----- CADASTRO CAMPEONATO BRASILEIRO -----========')
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print()

while True:
    jogador.clear()
    jogador["NOME"] = str(input("Informe o seu nome: "))
    partidas = int(input(f"Quantas partidas você jogou, {jogador['NOME']}: "))
    print()
    jogador["PARTIDAS"] = partidas
    for c in range(0, partidas):
        gol = (int(input(f"Quantos gols na partida {c+1}: ")))
        gols_jogador.append(gol)

    gols_total = gols_jogador[:]
    jogador["GOLS"] = gols_total[:]
    jogador["TOTAL"] = sum(gols_jogador)

    cadastro.append(jogador.copy())
    gols_jogador.clear()
    
    op = ""
    while True:
        op = str(input("Deseja continuar? [S/N]: ")).upper()[0]
        if op in "SN":
            break
        print("ERRO! Digite apenas S ou N.")
    if op == "N":
        break    
    print()

print()
print("-=-=-=-=-=-=-=-=-=-    PERFOMANCE    =-=-=-=-=-=-=-=-=-=-=")
print()
print("cod", end=" ")
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()

for k, v in enumerate(cadastro):
    print(f"{k:>3} ", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()

print()
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para finalizar): "))
    if busca == 999:
        break
    if busca >= len(cadastro):
       print(f"ERRO! Não existe jogador com código {busca}.")
       print()
    else:
        print()
        print(f"-- LEVANTAMENTO DO JOGADOR {cadastro[busca]['NOME']}: ")
        for i, g in enumerate(cadastro[busca]['GOLS']):
            print(f"No jogo {i+1} fez {g} Gols.")
        print()
