def leiaInt(msg): 
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido!\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[31mEntrada de dados interrompida pelo usuário!\033[m")
            return 0
        else:
            return n

def leiaFloat(msg): 
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número real válido!\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[31mEntrada de dados interrompida pelo usuário!\033[m")
            return 0
        else:
            return n

n1 = leiaInt("Digite um número: ")
n2 = leiaFloat("Digite um valor real: ")
print(f"O número inteiro digitado foi {n1} e o real foi {n2}")