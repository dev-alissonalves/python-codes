# -*- coding: UTF-8 -*-
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m quadrados

print("======== INÍCIO ========")
largura = float(input("Qual a largura do cômodo? "))
altura = float(input("Qual a altura do cômodo? "))

area = largura*altura
tinta = area/2
print("Seu cômodo tem {}m²\nVocê precisará de {} litros de tinta para pintá-lo.".format(area, tinta))