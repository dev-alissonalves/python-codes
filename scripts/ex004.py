# -*- coding: UTF-8 -*-
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

var = input("Digite algo: ")
print("Qual o tipo primitivo?")
print(type(var))
print("Ele é numérico?")
print(var.isnumeric())

print("É possível mostrar?")
print(var.isprintable())

print("Está escrito todo em maiúsculo?")
print(var.isupper())

print("Ele é alfabético?")
print(var.isalpha())

print("Ele é composto por espaços?")
print(var.isspace())

print("Ela está capitalizada?")
print(var.istitle())