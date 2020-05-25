# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
11 - Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
'''

lista1 = []
for i in range(1, 11):
    lista1.appendint(input(f'Digite {i}º número: '))
lista2 = []
for i in range(1, 11):
    lista2.appendint(input(f'Digite {i}º número: '))
lista3 = []
for i in range(1, 11):
    lista2.appendint(input(f'Digite {i}º número: '))

lista4 = []
# for vai percorrer as duas listas 
for i in range(0, 10):
    # vai add elementos intercalados dos dois outros vetores
    lista4.append(lista1[i])
    lista4.append(lista2[i])
    lista4.append(lista3[i])

print(lista4)