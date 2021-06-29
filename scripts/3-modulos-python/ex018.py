# -*- coding: UTF-8 -*-
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
#from math import sin, cos, tan
angulo = int(input("Informe o valor de um ângulo qualquer: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("Para o ângulo de [{}]° temos:\nSENO [{}]\nCOSSENO [{}]\nTANGENTE [{}]".format(angulo, seno, cosseno, tangente))