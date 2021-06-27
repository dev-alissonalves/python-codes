# -*- coding: UTF-8 -*-
#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
aluno1 = input("Nome do primeiro aluno: ")
aluno2 = input("Nome do segundo aluno: ") 
aluno3 = input("Nome do terceiro aluno: ") 
aluno4 = input("Nome do quarto aluno: ")
vetor = [aluno1, aluno2, aluno3, aluno4]

sorteio = print("O aluno escolhido foi: {}".format(random.choice(vetor)))