# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
2- Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''

# criando variável lista = função list()
lista = list()
# usei função .sort(reverse = True) p colocar na ordem decrescente
lista.sort(reverse = True)

# em um laço for vou digitar os 10 vetores 
for i in range(1, 11):
    # usei a função append para add cada número a lista
    lista.append(int(input(f'Ditie o {i}° número da lista:')))
print(lista)
# pode ser feito com print
# print(lista[::-1])
