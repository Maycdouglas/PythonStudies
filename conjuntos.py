# SETS - Conjuntos em Python (tipo set)

# São dados mutáveis, mas só aceitam tipos imutáveis como valor interno
# São muito eficientes para remover valores duplicados de iteráveis, pois seus valores serão sempre únicos
# - não tem indexes
# - não garantem ordem
# - são iteraveis

s1 = set('Maycon')
print(s1)

s2 = {'Maycon', 2, 1, 3}
print(s2)

lista = [1,1,1,2,2,3,4,3,5,4,2]
s3 = set(lista)
print(s3)

# Métodos Úteis
s1.add('Douglas')
print(s1)

s1.update('Henrique')
print(s1)

s1.discard('Douglas')
print(s1)

s1.clear()
print(s1)

# Operadores Úteis

s4 = {1,2,3}
s5 = {2,3,4}
s6 = s4 | s5 # União de dois set
s7 = s4 & s5 # Interseção de dois set
s8 = s4 - s5 # Diferença é apenas os itens presentes na esquerda
s9 = s4 ^ s5 # Diferença simétrica são os itens que não estão presentes nos dois set

print(f'{s4=}',f'{s5=}',f'{s6=}',f'{s7=}',f'{s8=}',f'{s9=}', sep='\n')