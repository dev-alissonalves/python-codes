#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(msg):
    tam = len(msg)
    print("-" * (tam + 4))
    print(f"  {msg}")
    print("-" * (tam + 4))


mensagem = str(input("Digite uma mensagem: "))
escreva(mensagem)
