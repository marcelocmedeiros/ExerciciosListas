# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
4- Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
'''
# crei uma lista das consoantes digitadas
lista = []
# variável vogal vai ser util para saber o caracter consoante
vogal = 'aeiou'
# somatoria de consoantes 
consoantes = 0
# laço for para digitar os 10 caracteres
for i in range(1, 11):
    letra = input(f'Digite o {i}º caractere: ').lower() # tudo maiúscula
    # verificar se não estiver em vogal é consante
    if letra not in vogal:
        # soma + 1 na variável consoantes
        consoantes += 1
        # add na lista de consoante
        lista.append(letra)

print(f'Total de consoantes: {consoantes}')
print(lista)
