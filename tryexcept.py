# TRY/EXCEPT

numero_str = 'a'

try:
    numero_float = float(numero_str)
    print('FLOAT:',numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# a forma acima não é a mais indicada