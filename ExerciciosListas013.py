# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
13 - Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
'''
# listas temperaturas 
temperaturas = []
# for para receber 12 temperaturas
for i in range(1, 13):
    temperaturas.append(float(input(f'Digite a temperatura do {i}º mês: ')))
# média usando a função sum / 12
media = sum(temperaturas) / 12
print(media)
i = 0
# lista de meses 
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
print('Meses com temperatura acima da média')
# 2º laço vai passar por todas as temperaturas e comprar se é maior q média
for t in temperaturas:
    if t > media:
        print(meses[i])

    i += 1
        