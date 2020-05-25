# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
12 - Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
'''
# listas
idades = []
alturas = []
# for q vai cadastrar todos os alunos com suas idades e alturas
for i in range(1, 31):
    idades.append(int(input(f'Digite a idade do {i}º aluno: ')))
    alturas.append(float(input(f'Digite a altura do {i}º aluno: ')))
    
# usei função sum p somas todosos valores da lista alturas
media = sum(alturas) / 30
total = 0
for i in range(0, 30):
    # condição determinada na questão p obter o total 
    if idades[i] > 13 and alturas[i] < media:
        total += 1

print(f'Total de alunos com mais de 13 anos e altura inferio a media de altura: {total}')
