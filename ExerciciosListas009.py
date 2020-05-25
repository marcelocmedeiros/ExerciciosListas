# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
9 - Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
'''
# 1ª lista recebe os valores e a 2ª lista recebe o quadrado dos valores da 1ªlista
lista = []
quadrados = []
# for para add 1ª lista
for i in range(1, 11):
    lista.append(int(input(f'Informe o {i}° número da lista: ')))
# for para add 2ª lista
for y in lista:
        # y ** 2 o quadrado de cada elemento da 1ª lista
    quadrados.append(y**2)
print('A soma dos quadrados dos elementos da lista é', sum(quadrados))
