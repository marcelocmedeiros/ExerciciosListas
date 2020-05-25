# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
6 - Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
'''
# lista de médias 
medias = []
# 1° laço com 10 alunos
for i in range(1, 11):
    # acumulador da soma e média
    soma = media = 0
    # 2° laço com as 4 notas
    for y in range(1, 5):

        nota = float(input(f'Digite a {y}º nota do {i}º aluno: '))
        soma += nota
    media = soma / 4
    medias.append(media)

print(f'Médias: {medias}')

alunos = 0
for m in medias:
    if m >= 7:
        alunos +=1
print(f'Número de alunos com média maior ou igual a 7 é {alunos}')
