# LISTAS [ARRAY / VETOR]

#Suporta vários valores de qualquer tipo. É como o Array do Java Script

lista = [123, True, 'Maycon Douglas', 1.2, [14, 18]]
print(lista)
print(lista[1])

#Principais métodos:

del lista[2] # deleta elemento da lista
print(lista)

lista.append('Maycon Douglas') # adiciona elemento no final da lista
print(lista)

lista.pop() # remove o ultimo elemento da lista
print(lista)

lista.insert(2,'Maycon Douglas') #adiciona elemento na lista
print(lista)

lista.clear() # limpa a lista
print (lista)

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b # concatena listas
lista_a.extend(lista_b) # também concatena listas

print('Lista C:', lista_c, 'Lista A:', lista_a)

# TUPLA / TUPLE
# É uma lista imutável

nomes = 'Maycon', 'Douglas', 'Henrique' # pode usar parenteses na declaração
print(nomes)

# ENUMERATE

for indice, nome in enumerate(nomes): # Cria uma tupla com o valor do indice e o conteudo da lista
    print(indice,nome)

# List Comprehension

algarismos = [numero for numero in range(10)]

print(algarismos)

# Abaixo um exemplo de mapeamento da lista
produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} if produto['preco'] > 20 else {**produto} for produto in produtos
]

print(*novos_produtos, sep='\n')

# Abaixo exemplo de filtro da lista
lista_2 = [n for n in range(10) if n < 5]
print(lista_2)

# Usando um for depois de outro for na lista
lista_3 = []
for x in range(3):
    for y in range(3):
        lista_3.append((x,y))

print(lista_3)

lista_4 = [ (x,y) for x in range(3) for y in range(3)]

print(lista_4)