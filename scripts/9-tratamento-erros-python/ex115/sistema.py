#coding: utf-8

from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = "pyPack.txt"

if not arquivoEncontrado(arq):
    criarArquivo(arq)

while True:
    res = menu(["Ver pessoas cadastradas", "Cadastrar nova Pessoa", "Sair do Sistema"])

    if res == 1:
        cabeçalho("Lendo arquivos...")
        lerArquivo(arq)
    elif res == 2:
        cabeçalho("Cadastrando nova pessoa...")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastro(arq, nome, idade)
    elif res == 3:
        cabeçalho("Saindo do sistema... Até logo!")
        break
    else:
        cabeçalho("\033[31mERRO! Digite uma opção válida!\033[m")
    sleep(2)
    print("\n")

