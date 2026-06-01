from itertools import product
import os

os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela

print("\033[1mCALCULADORA DE TABELA-VERDADE\033[0m\n")

print("() - Parêntese\n~  - Não\n∧  - E\n∨  - Ou\n→  - Condicional\n↔  - Bicondicional\nV̲  - Ou Exclusivo\n")

sintaxe = input("Insira a proposição da tabela-verdade: ")
sintaxe = sintaxe.replace(" ", "")

elementos = []

for i in range(len(sintaxe)):
    if sintaxe[i] in ["(",")"]:
        elementos.append(sintaxe[i])
    elif sintaxe[i].isalpha():
        elementos.append(sintaxe[i])
    elif sintaxe[i] in ["~", "∧", "∨", "→", "↔", "V̲"]:
        elementos.append(sintaxe[i])
    else:
        print(f"Caractere desconhecido: {sintaxe[i]}.")

variaveis = []

for elemento in elementos:
    if elemento.isalpha() and elemento not in variaveis:
        variaveis.append(elemento)

n = len(variaveis)

for combinacao in product(["V", "F"], repeat=n):
    print([combinacao])