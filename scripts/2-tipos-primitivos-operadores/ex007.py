# -*- coding: UTF-8 -*-
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

n1 = int(input("Informe sua nota no primeiro bimestre: "))
n2 = int(input("Informe sua nota no segundo bimestre: "))
n3 = int(input("Informe sua nota no terceiro bimestre: "))
media = (n1+n2+n3)/3

print("Sua média final é: {}".format(media))