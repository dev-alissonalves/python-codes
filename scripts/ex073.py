#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: 
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

tabela_brasileirao = (
    "Flamengo", "Internacional", "Atlético - MG", "São Paulo", "Fluminense", "Grêmio", "Palmeiras", "Santos", "Athlético Paranaense", "Bragantino - Red Bull", "Ceará", "Corinthians", "Atlético - GO", "Bahia", "Sport", "Fortaleza", "Vasco da Gama", "Goiás", "Coritiba", "Botafogo")

print(f"\n(A) Os cinco primeiros colocados do campeonato foram: {tabela_brasileirao[:5]}\n")
print(f"(B) Os últimos colocados do campeonato foram: {tabela_brasileirao[-4:]}\n")
print(f"(C) Os times em ordem alfabética são: {sorted(tabela_brasileirao)}\n")
#modo1 -busca o índice de elemento qualquer
print(f"O time da Bahia está na {tabela_brasileirao.index('Bahia')}ª posição")

#modo2 - busca um elemento usando for
for cont in range(0, len(tabela_brasileirao)):
    if tabela_brasileirao[cont] == "Bahia":
        print(f"(D) O time da {tabela_brasileirao[cont]} está na {cont+1}º Posição.\n")   
    elif cont == len(tabela_brasileirao)-1 and tabela_brasileirao[cont] != "Chapecoense":
        print("(D) O time da Chapecoense não se encontra no campeonado este ano!\n")