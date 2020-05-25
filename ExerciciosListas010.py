# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
10 - Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
'''

lista1 = []
for i in range(1, 11):
    lista1.appendint(input(f'Digite {i}º número: '))
lista2 = []
for i in range(1, 11):
    lista2.appendint(input(f'Digite {i}º número: '))
lista3 = []
# for vai percorrer as duas listas 
for i in range(0, 10):
    # vai add elementos intercalados dos dois outros vetores
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(lista3)
