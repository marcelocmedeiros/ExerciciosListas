# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
5 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores.
'''
# criei 3 listas p serem impressas no final
lista = []
listaPar = []
listaImpar= []

for i in range(1, 21):
    num = (int(input(f'Informe o {i}ª número da lista: ')))
    lista.append(num)
    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)
print(f'A lista dos números digitados é: {lista}')
print(f'A lista dos números pares é: {listaPar}')
print(f'A lista dos números ímpares é: {listaImpar}')
