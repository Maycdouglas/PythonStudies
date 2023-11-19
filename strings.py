# FORMATAÇÃO DE STRINGS - F-STRINGS

nome = 'Maycon Douglas'
altura = 1.76
peso = 76

frase = f'{nome} tem {altura:.2f} de altura e pesa {peso} quilos' # o f antes da string permite a utilização de variaveis dentro dela.
# o :.2f permite decidir quantas casas decimais serão impressas
# se utilizar ,:.2f o numero 1000 será impresso como 1,000.00

print(frase)

variavel = 'ABC'
print(f'{variavel: >10}') # preenche a esquerda
print(f'{variavel:&<10}') # preenche a direita
print(f'{variavel:&^10}') # preenche ao redor
print(f'{1000.487:0>+10,.2f}') # inserção de sinal em número
print(f'{1000.487:0=+10,.2f}') # inserção de sinal em numero, forçando a aparecer antes dos zeros inseridos



frase = 'nome = {0} altura = {1} peso = {2:.2f} altura de novo: {1}'.format(nome, altura, peso) # Outra forma de formatação da string
#tem que numerar todos, para que seja possivel utilizar o indice. Se numerar ninguém, será utilizada a ordem.

print(frase)

frase = 'nome = {n} altura = {a} peso = {p:.2f} altura de novo: {a}'.format(n = nome, a = altura, p = peso) # Outra forma utilizando parametros nomeados

print(frase)

    # Interpolação básica de strings
    # %s - string
    # %d e %i - int
    # %f - float
    # %x e %X - Hexadecimal

time = 'Cruzeiro'
preco = 299.990908
camisa = 'A camisa do %s custa R$%.2f' % (time,preco)
print (camisa)
print('O hexadecimal de %d é %08X' % (4000, 4000))
# CONCATENAÇÃO E REPETIÇÃO

concatenacao = "A" + "B" + "C"
print(concatenacao)

a_dez_vezes = 'A' * 10
print(a_dez_vezes)

# FATIAMENTO DE STRINGS
# [i:f:p] - i = inicio, f = fim, p = passo

fatia = 'Maycon Douglas'
print(len(fatia)) # retorna tamanho da string
print(fatia[::-1]) # inverte a string
print(fatia[-1:-(len(fatia) + 1):-1]) # também inverte a string
print(fatia[0:len(fatia) - 1]) # retorna um pedaço da string
print(fatia[0:len(fatia):2]) # retorna a string pulando de 2 em 2 caracteres



