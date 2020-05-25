# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
8 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
'''

idade = list()
altura = list()
for i in range(1, 6):
    idade.append(int(input('Informe sua idade: ')))
    altura.append(float(input('Informe sua altura: ')))
print('=-'*26)
print('A ordem das idades informadas foram:', idade)
print('A ordem das idades de forma inversa é:', idade[::-1])
print('A ordem das alturas informadas foram:', altura)
print('A ordem das Alturas de forma inversa é:', altura[::-1])

