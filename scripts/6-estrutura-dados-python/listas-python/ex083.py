#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

lista_exp = []
expressao = str(input("Informe uma expressão: "))

for caractere in expressao:
    if caractere == "(":
       lista_exp.append("(") 
    elif caractere == ")":
        if len(lista_exp) > 0: #Se a lista não estiver vazia e encontrar o fechamento
            lista_exp.pop() #exclua a abertura - ou seja abriu e fechou
        else:
            lista_exp.append(")") #ou seja não encontrou a abertura e tem um erro
            break

if len(lista_exp) == 0:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está errada!")