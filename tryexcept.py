# TRY/EXCEPT

numero_str = 'a'

try:
    numero_float = float(numero_str)
    print('FLOAT:',numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# a forma acima não é a mais indicada

#Captura de Erros
try:
    a = 18
    b = 0
    print(a[1000])
    c = a/b
    
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('Nome n não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('Error:', error)
    print('Nome da classe:',error.__class__.__name__)
except Exception:
    print('Erro desconhecido')

# Finally e Else
try:
    print('Abrir Arquivo')
except:
    print('Dividiu Zero')
else: # executa somente se não tiver capturado erro
    print('Não deu erro')
finally: #finally é sempre executado
    print('Fechar Arquivo')

# Raise - Lançando exceções(erros)

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por 0') #Lança o erro manualmente
    return True

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True

def divide(n,d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n/d

print(divide(8,'0'))