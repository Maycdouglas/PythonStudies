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





