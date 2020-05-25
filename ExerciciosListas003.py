# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
3- Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''
# para criar uma lista pode ser feito com função list() ou []
lista = []

# em um laço for vou digitar os 4 notas 
for i in range(1, 5):
    # usei a função append para add cada número a lista
    lista.append(float(input(f'Ditie o {i}° nota da lista:')))
media = sum(lista)/4
for i, v in enumerate(lista):
    print(f'A {i+1}° nota foi {v}')
print(lista)
print(f'As notas são {lista} e sua média é {media}.')
    
