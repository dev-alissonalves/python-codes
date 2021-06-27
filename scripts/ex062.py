#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar 
# mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos. 

#modo1
print("\n============ PROGRESSÃO ARITMÉTICA ============\n")
termo = int(input("Informe o primeiro termo da P.A.: "))
razao = int(input("Informe a razão da P.A.: "))
print("\n")
cont = 1
termos = 11
total = 0
while termos != 0:
    total = total + termos
    while cont < total:
        pa = termo + (cont - 1)*razao #fórmula básica da PA
        print(f"{cont}º termo = {pa}")
        cont += 1
    print("\nPAUSA!\n")
    termos = int(input("Informe a quantidade de termos que deseja mostrar a mais: "))

print(f"A quantidade de termos mostrados foi:  {total-1}")
print("\n============ PROGRESSÃO ARITMÉTICA ============\n")