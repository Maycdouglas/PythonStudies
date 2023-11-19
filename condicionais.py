# CONDICIONAIS

entrada = input('Escolha um número de 1 a 3')

numero = int(entrada)

if numero == 1:
    print('Escolheu o número 1')
elif numero == 2:
    print('Escolheu o número 2')
elif numero == 3:
    print('Escolheu o número 3')
else:
    print('número inválido')

# OPERADORES LÓGICOS

falso = not True # Diferentemente das outras linguagens, não usamos o sinal '!' para representar o operador not
verdadeiro = not False

palavra = 'cruzeiro'
print('z' in palavra) # retorna True
print('b' not in palavra) # retorna False

# OPERAÇÃO TERNARIA

print('Valor' if True else "Outro Valor")