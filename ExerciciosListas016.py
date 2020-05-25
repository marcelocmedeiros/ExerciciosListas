# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
16 - Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9% por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9% por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
        a- $200 - $299
        b- $300 - $399
        c- $400 - $499
        d- $500 - $599
        e- $600 - $699
        f- $700 - $799
        g- $800 - $899
        h- $900 - $999
        i- $1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário,
sem fazer vários ifs aninhados.
'''

salarioBase = 200
# lista [0]*9 == [0, 0, 0, 0, 0, 0, 0, 0, 0] o salário vai ser acumulado no indice da lista e não por valor literal
vendedores = [0]*9
# laço for p pegar 9 vendas e colocar na posição da lista correspondente ao salário
for i in range(1, 10):
    valorVendas = float(input('Informe o valor das vendas do vendedor: '))
    # calculo do salário
    salario = valorVendas * 0.09 + salarioBase
    # calculo do indice
    indice = int(salario / 100) - 1
    # condição p indice > 9 ou indice < 0
    if (indice > 9):
        indice = 9
    elif (indice < 1):
        indice = 1
    else:
        indice = indice
    # contador do vededores 
    vendedores[indice - 1] += 1
print(vendedores)# para entender como esta sendo feito print final 
# laço for p impressão indentada p cada faixa de salário 
for i in range(0, 9):
    print(f'{i * 100 + 200} - {(i + 1) * 100 + 199} : {vendedores[i]}')
