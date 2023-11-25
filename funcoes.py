# FUNCÕES

def funcao(nome, sobrenome = "Douglas"):
    print(f'Meu nome é {nome} e meu sobrenome é {sobrenome}')

funcao('Maycon')

# Função com *args
# permite que insira diversos argumentos em uma tupla
# por convenção, utiliza-se args

def soma(*args):
    soma = 0
    for x in args:
        soma = soma + x
    return soma

print(soma(1,2,2,20))
print(soma(1,2,3,4,5,6,7,8,9))

# Exemplo de função recebendo função como argumento e também utilizando o *args (Empacotamento e Desempacotamento)
def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)

print(
    executa(saudacao,'Bom dia', 'Maycon')
)

# Exemplo de Closure

def criar_saudacao(saudacao):
    def saudar(nome):
            return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

print(falar_bom_dia('Maycon'))
print(falar_boa_noite('Maycon'))

# Função Lambda

lista = [
     {'nome': 'Maycon', 'sobrenome': 'Douglas'},
     {'nome': 'David', 'sobrenome': 'Jorge'},
     {'nome': 'Melissa', 'sobrenome': 'Alencar'},
     {'nome': 'Amanda', 'sobrenome': 'Pereira'}
]

def ordena(item):
     print('ITEM:', item)
     return item['nome']

lista.sort(key=ordena)
print(lista)

# Agora vamos utilizar a função Lambda:

lista.sort(key=lambda item: item['nome'])

for item in lista:
     print(item)