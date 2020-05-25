# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
7 - Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
'''


lista = list()
# multip = 1 pq 1 elemento neutro da multiplicação
multip = 1
for i in range(1, 6):
    num = (int(input(f'Informe o {i}º número da lista: ')))
    # add a lista
    lista.append(num)
    multip *= num
print('=-'*28)    
print('A soma de todos os números da lista é:', sum(lista))
print('A Multiplicação de todos os números da lista é:', multip)
print('A lista é:', lista)
print('=-'*28)
