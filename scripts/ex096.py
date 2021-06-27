#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

#Funções utilizadas no programa principal
def mostraLinha():
    print("-" * 30)

def calculoArea (x, y):
    area = x * y
    print(f"O terreno com {x}m de lagura por {y}m de comprimento possui uma área de {area} m².")


mostraLinha()
print("--- CÁLCULO DE ÁREA DE UM TERRENO ---")
largura = float(input("Qual a largura (m): "))
comprimento = float(input("Qual o comprimento (m): "))
calculoArea(largura, comprimento)
mostraLinha()
