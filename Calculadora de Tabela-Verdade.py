from itertools import product
import os

os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela

print("\033[1mCALCULADORA DE TABELA-VERDADE\033[0m\n")

print("() - Parêntese\n~  - Não\n∧  - E\n∨  - Ou\n→  - Condicional\n↔  - Bicondicional\nV̲  - Ou Exclusivo\n")

sintaxe = input("Insira a proposição da tabela-verdade: ")
sintaxe = sintaxe.replace(" ", "")

elementos = []

# Separa a expressão em elementos de uma lista
i = 0
while i < len(sintaxe):
    if sintaxe[i] == 'V' and i + 1 < len(sintaxe) and sintaxe[i + 1] == '\u0332':
        elementos.append('V̲')
        i += 2 # Pula os dois caracteres do V̲
    elif sintaxe[i] in ["(", ")"]:
        elementos.append(sintaxe[i])
        i += 1
    elif sintaxe[i].isalpha():
        elementos.append(sintaxe[i])
        i += 1
    elif sintaxe[i] in ["~", "∧", "∨", "→", "↔"]:
        elementos.append(sintaxe[i])
        i += 1
    else:
        print(f"Caractere desconhecido: {sintaxe[i]}.")
        i += 1

variaveis = []

# Separa as variáveis
for elemento in elementos:
    if elemento.isalpha() and elemento not in variaveis:
        variaveis.append(elemento)

n = len(variaveis)

# Variáveis do leitor
posicao = 0
valores_atuais = {}

def simbolo_atual():
    # Retorna o símbolo atual sem avançar
    if posicao < len(elementos):
        return elementos[posicao]
    return None

def avancar():
    # Avança para o próximo símbolo
    global posicao
    posicao += 1

def ler_elemento():
    # Caso seja uma variável (p, q, r...)
    if simbolo_atual().isalpha():
        variavel = simbolo_atual()
        avancar()
        return valores_atuais[variavel]
    
    # Caso seja uma expressão entre parênteses
    elif simbolo_atual() == '(':
        avancar() # Pula o '('
        resultado = ler_xor() # Lê o que está dentro
        avancar() # Pula o ')'
        return resultado

def ler_negacao():
    # Caso seja uma negação
    if simbolo_atual() == '~':
        avancar() # Pula o '~'
        return not ler_negacao() # Lê o que vem depois e nega
    
    # Caso contrário, lê o elemento básico
    return ler_elemento()

def ler_conjuncao():
    # Lê o lado esquerdo
    esquerda = ler_negacao()
    
    # Enquanto houver '∧', lê o lado direito e combina
    while simbolo_atual() == '∧':
        avancar() # Pula o '∧'
        direita = ler_negacao() # Lê o lado direito
        esquerda = esquerda and direita # Combina os dois
    
    return esquerda

def ler_disjuncao():
    # Lê o lado esquerdo
    esquerda = ler_conjuncao()
    
    # Enquanto houver '∨', lê o lado direito e combina
    while simbolo_atual() == '∨':
        avancar() # Pula o '∨'
        direita = ler_conjuncao() # Lê o lado direito
        esquerda = esquerda or direita # Combina os dois
    
    return esquerda

def ler_condicional():
    # Lê o lado esquerdo
    esquerda = ler_disjuncao()
    
    # Enquanto houver '→', lê o lado direito e combina
    while simbolo_atual() == '→':
        avancar() # Pula o '→'
        direita = ler_disjuncao() # Lê o lado direito
        esquerda = (not esquerda) or direita # Combina os dois
    
    return esquerda

def ler_bicondicional():
    # Lê o lado esquerdo
    esquerda = ler_condicional()
    
    # Enquanto houver '↔', lê o lado direito e combina
    while simbolo_atual() == '↔':
        avancar() # Pula o '↔'
        direita = ler_condicional() # Lê o lado direito
        esquerda = esquerda == direita # Combina os dois
    
    return esquerda

def ler_xor():
    # Lê o lado esquerdo
    esquerda = ler_bicondicional()
    
    # Enquanto houver 'V̲', lê o lado direito e combina
    while simbolo_atual() == 'V̲':
        avancar() # Pula o 'V̲'
        direita = ler_bicondicional() # Lê o lado direito
        esquerda = esquerda != direita # Combina os dois
    
    return esquerda

def exibir(valor):
    # Exibe V em verde ou F em vermelho
    return "\033[32mV\033[0m" if valor else "\033[31mF\033[0m"

def imprimir_tabela():
    global posicao, valores_atuais

    # Cabeçalho da tabela
    cabecalho = "  ".join(variaveis) + "  " + sintaxe
    print("\n" + cabecalho)
    print("─" * len(cabecalho))

    # Imprime uma linha para cada combinação de V e F
    for combinacao in product([True, False], repeat=n):
        valores_atuais = dict(zip(variaveis, combinacao))
        posicao = 0 # Reinicia a leitura da expressão

        resultado = ler_xor()

        linha = "  ".join(exibir(v) for v in combinacao) + "  " + exibir(resultado)
        print(linha)

imprimir_tabela()