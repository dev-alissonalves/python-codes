# -*- coding: UTF-8 -*-
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

import math
#from math import hypot
Cateto_oposto = int(input("Qual o comprimento do cateto oposto? "))
Cateto_adj = int(input("Qual o comprimento do cateto adjacente? "))
hipotenusa = print("A hipotenusa vale: {:.4f}".format(math.hypot(Cateto_oposto, Cateto_adj)))