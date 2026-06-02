from itertools import product
import os

os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela

print("\033[1mCALCULADORA DE TABELA-VERDADE\033[0m\n")

print("() - Parêntese\n~  - Não\n∧  - E\n∨  - Ou\n→  - Condicional\n↔  - Bicondicional\nV̲  - Ou Exclusivo\n")

sintaxe = input("Insira a proposição da tabela-verdade: ")
sintaxe = sintaxe.replace(" ", "")

# Definição da precedência
precedencia = {
    '~': 6,
    '∧': 5,
    '∨': 4,
    '→': 3,
    '↔': 2,
    'V̲': 1
}

elementos = []

# Separa a expressão em elementos de uma lista
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

# Separa as variáveis
for elemento in elementos:
    if elemento.isalpha() and elemento not in variaveis:
        variaveis.append(elemento)

n = len(variaveis)

def shunting_yard(elementos):
    saida = []
    operadores = []

    for elemento in elementos:
        if elemento.isalpha():  # Se for variável
            saida.append(elemento)
        elif elemento in precedencia:  # Se for operador
            # Enquanto o topo da pilha tiver precedência maior, move pra saída
            while operadores and operadores[-1] != '(' and precedencia.get(operadores[-1], 0) >= precedencia[elemento]:
                saida.append(operadores.pop())
            operadores.append(elemento)
        elif elemento == '(':
            operadores.append(elemento)
        elif elemento == ')':
            # Move tudo até encontrar o '('
            while operadores and operadores[-1] != '(':
                saida.append(operadores.pop())
            operadores.pop()  # Remove o '('

    while operadores:
        saida.append(operadores.pop())

    return saida

# Imprime a tabela verdade
for combinacao in product(["V", "F"], repeat=n):
    print(list(combinacao))