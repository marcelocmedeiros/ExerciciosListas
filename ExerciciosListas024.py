# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
24 - Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes armazene os resultados em um vetor. Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
'''

from random import randint

numeros = [] 
for i in range(1, 101):
    n =  randint(1, 6)
    numeros.append(n)
    
print(f'O número 1 teve {numeros.count(1)} lançamentos')
print(f'O número 2 teve {numeros.count(2)} lançamentos')
print(f'O número 3 teve {numeros.count(3)} lançamentos')
print(f'O número 4 teve {numeros.count(4)} lançamentos')
print(f'O número 5 teve {numeros.count(5)} lançamentos')
print(f'O número 6 teve {numeros.count(6)} lançamentos')
