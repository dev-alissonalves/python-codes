# -*- coding: UTF-8 -*-
#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex. 6.127 e mostra 6.

#import math -> primeiro jeito de importar
from math import trunc # -> jeito mais específico de importar
num = float(input("Informe um número real qualquer: "))
print("A porção inteira do número digitado é: {}".format(math.trunc(num))) # -> pode ser utilizado também int(num)



