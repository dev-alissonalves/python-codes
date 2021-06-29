#Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer 
#e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8 

n = int(input("Informe a quantidade de elementos da SEQ. de Fibonacci que devo mostrar: "))
t1 = 0
t2 = 1
print(f"{t1} -> {t2}", end="") #mostrando os primeiros elementos
cont = 3 #contador iniciou em 3 porque já mostrei os 2 primeiros
while cont <= n:
    prox = t1 + t2 #príximo valor é a soma dos anteriores
    print(f" -> {prox}", end="")
    t1 = t2 #dei um passo para t1 virar t2
    t2 = prox #dei um passo para t2 virar o prox
    cont += 1
print(f" -> FIM")