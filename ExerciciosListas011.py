# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
11 - Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
'''

'''
5 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores.
'''
print('Primeiro vetor')
# criei 3 listas p serem impressas no final
lista1 = []
for i in range(1, 4):
    lista1.append(int(input(f'Digite {i}º número: ')))
print('Segundo vetor')
lista2 = []
for i in range(1, 4):
    lista2.append(int(input(f'Digite {i}º número: ')))
print('Terceiro vetor')
lista3 = []
for i in range(1, 4):
    lista3.append(int(input(f'Digite {i}º número: ')))

lista4 = []
# for vai percorrer as duas listas
for i in range(0, 3):
    # vai add elementos intercalados dos dois outros vetores
    lista4.append(lista1[i])
    lista4.append(lista2[i])
    lista4.append(lista3[i])
print(lista1)
print(lista2)
print(lista3)
print(lista4)
