# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
17 - Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

    Atleta: Rodrigo Curvêllo
    Primeiro Salto: 6.5 m
    Segundo Salto: 6.1 m
    Terceiro Salto: 6.2 m
    Quarto Salto: 5.4 m
    Quinto Salto: 5.3 m
    
        Resultado final:
        Atleta: Rodrigo Curvêllo
        Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
        Média dos saltos: 5.9 m
'''

# loop infinito para recaber quantos atletas for necessário 
while True:
    nome = input('Digite o nome do atleta: ')
    # condição p parar
    if nome == '':
        break
    #lista dos saltos
    saltos = []
    # um loop for para  pegar os 5 saltos de cada atleta 
    for i in range(1, 6):
        saltos.append(float(input(f'Digite o valor do {i}º salto: ')))
    # soma com função sum
    media = sum(saltos) / 5
    print('=-'*20)        
    print('Resultado final')
    print(f'Atleta: {nome}')
    print(f'Saltos: {saltos[0]} - {saltos[1]} - {saltos[2]} -{saltos[3]} - {saltos[4]}')
    print(f'Média dos saltos: {media:.02f} m')
    print('=-'*20) 
 