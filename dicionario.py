# TIPO DICT
# Dicionários são estruturas de dados do tipo par de "chave" e "valor"
# Chaves podem ser de tipos imutáveis (str,int,float,bool,tuple...)
# O valor pode ser de qualquer tipo, incluindo dicionário
# Usamos as chaves " {} " ou a classe dict para criar dicionários
#
#
#
#
#
#
#
#
#
#

import copy

pessoa = {
    'nome': 'Maycon',
    'sobrenome': 'Gomes',
    'idade': 23,
    'altura': 1.76,
    'enderecos': [
        {'rua': 'aristoteles braga', 'numero': 195},
        {'rua': 'gabriel lopes leles', 'numero': 85},
    ],
}

pessoa_2 = dict(nome = 'Maycon', sobrenome = 'Douglas')

print(pessoa)
print(pessoa['nome'])

for chave in pessoa:
    print(chave, pessoa[chave])

pessoa_3 = {}
print(pessoa_3)
pessoa_3['nome'] = 'Luiz Otávio' # Cria a chave no Dict, já que não existia essa chave nele
print(pessoa_3)

# também é possível criar a chave dinamicamente
chave = 'sobrenome'
pessoa_3[chave] = 'Gomes'
print(pessoa_3[chave])

# Deletar chave
print(pessoa_3)
del pessoa_3['sobrenome']
print(pessoa_3)

# Para o programa não parar quando tentar acessar uma chave inexistente

if pessoa_3.get('sobrenome') is None:
    print('Chave não existe')
else:
    print(pessoa_3['sobrenome'])

# Métodos úteis nos Dicts

print(pessoa.__len__())
print(len(pessoa))

# ambas as formas acima retorna a quantidade de chaves que tem no dicionário

print(pessoa.keys()) # Retorna as chaves
# o tipo retornado é dict_keys, parece uma lista mas não é. Entretanto, pode-se utilizar coerção

print(pessoa.values()) # Retorna os valores das chaves

print(pessoa.items()) # Retorna os itens, apresentando chaves e seus valores

pessoa.setdefault('sexo','Masculino') # Permite criar uma chave e definir um valor padrão para ela quando não for informado
print(pessoa['sexo'])

# COPY e DEEPCOPY

pessoa_4 = pessoa.copy() # Dessa forma, apenas copia os dados imutaveis. É o Shallow Copy, cópia rasa
print(pessoa_4)

pessoa_5 = copy.deepcopy(pessoa) # Dessa forma, consegue copiar os dados mutaveis. É a cópia profunda.
print(pessoa_5)

# GET

print(pessoa.get('nome','Não existe')) # Pega o valor da chave. Se não existir, retorna o segundo parametro da função

# POP
endereco = pessoa_4.pop('enderecos') # Apaga o item informado, mas também retorna ele
print(endereco, pessoa_4)

# POPITEM
sexo = pessoa_4.popitem() # Apaga o último item adicionado e retorna o item
print(sexo, pessoa_4)

# UPDATE

# Atualiza valores do dicionario e também permite criar novas chaves. Aceita listas e tuplas como argumento

print(pessoa_4)
pessoa_4.update({
    'sexo': 'masculino',
    'nome': 'Henrique'
})

print(pessoa_4)

pessoa_4.update(nome='Maycon',peso=76)
print(pessoa_4)