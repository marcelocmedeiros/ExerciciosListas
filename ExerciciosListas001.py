# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
'''
# criando variável lista = função list()
lista = list()
# em um laço for vou digitar os 5 vetores 
for i in range(1, 6):
    # usei a função append para add cada número a lista
    lista.append(int(input(f'Ditie o {i}° número da lista:')))
print(lista)
