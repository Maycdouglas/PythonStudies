import sys
import meu_package

# Comentário em Linha

"""
não é um comentário! Mas é utilizado como comentário multi-linhas
o termo correto é DocStrings e são lidas pelo programa.
Também pode ser utilizada as aspas simples (''' '''')
"""

# IMPRESSÃO DE DADOS

print("Hello World!") # Impressão
print(12, 14, end=" ## ") # Impressão trocando o padrão de quebra de linha, utilizando o argumento nomeado END.
print(12, 14, sep="-") # Impressão trocando o separador, utilizando o argumento nomeado SEP. Também pode ser utilizado as aspas simples (' ')
lista = ["Maycon","Douglas","Henrique"]
print(*lista) # Imprime todos os elementos da lista separadamente

# INSERÇÃO DE DADOS PELO USUÁRIO

#input = input('Qual é o seu nome? ') # A função input() permite o usuário inserir um valor. Ela SEMPRE retorna uma String
#print(f'O seu nome é {input=}') # Ao utilizar o sinal de = após a variável, fará que imprima o nome da variável junto. Bom para testes

# ELLIPSIS

exemplo = ... # Esse operador permite que o código rode normalmente, servido de placeholder para no futuro inserir algo
# o termo PASS também pode ser utilizado.

# EMPACOTAMENTO E DESEMPACOTAMENTO
nome1, nome2, nome3 = ['Maycon', 'Douglas', 'Henrique'] # cada valor dessa lista é atribuído a cada uma das variaveis
print(nome1,nome2,nome3)

_,nome, *resto = ['Maycon', 'Douglas', 'Henrique', 'da Silva', 'Gomes'] # os valores em '_' e '*resto' são desconsiderados. 
#'_' é o mais correto

print(_,nome,resto)

# IS INSTANCE
instancia = 'Maycon'
print(instancia,isinstance(instancia,str)) # verifica se aquela variavel é uma instancia de uma determinada classe

# GENERATOR EXPRESSION

lista = [n for n in range(100)]
generator = (n for n in range(100))

print(sys.getsizeof(lista)) #Retorna o espaço ocupado pelo objeto na memória do computador
print(sys.getsizeof(generator))

print(generator)
print(next(generator))
# Basicamente a função pausa e só executa cada iteração quando você chama o método next. Permite não ocupar tanta memória

# GENERATOR FUNCTION

def generator(n=0):
    yield 1 # YIELD faz pausar e retornar o valor.
    print('Continuando')
    yield 2
    print('Mais uma...')
    yield 3
    return 'Acabou'

gen = generator(n=0)
print(next(gen)) # Para a função executar, o next deve ser usado a cada pausa
print(next(gen))

## YIELD FROM

def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield from gen1() #Permite dar continuidade de um generator anterior
    yield 4
    yield 5
    yield 6

g = gen2()
for numero in g:
    print(numero)

print(meu_package.dobra(2))
