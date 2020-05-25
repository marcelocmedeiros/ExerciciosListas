# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
14 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    a) "Telefonou para a vítima?"
    b) "Esteve no local do crime?"
    c) "Mora perto da vítima?"
    d) "Devia para a vítima?"
    e) "Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
# lista de sim para saber quantas respostas foram positivas
sim = []
# lista das perguntas
perguntas = ['Telefonou para a vítima?','Esteve no local do crime?','Mora perto da vítima?','Devia para a vítima?','Já trabalhou com a vítima?']

print('Digite S-SIM e N-NÃO')
# laço vai passar pela lista de pergunta e fazer cada uma
for p in perguntas:
    resp = input(f'{p} ').upper()
    if resp == 'S':
        sim.append(resp)
# condição para classificar o entrevistado
if len(sim) == 2:
    print('Você é Suspeito, não saia da cidade!')
elif len(sim) >= 3 and len(sim) <= 4:
    print('Você está preso por que é Cúmplice do crime.')
elif len(sim) == 5:
    print('Assassino e está preso!')
else:
    print('Pode ir você é Inocente!')
    
# por while 
'''
print("Digite S-SIM e N-NÃO\n")
# lista das perguntas 
perguntas = ["Telefonou para a vítima? ---> ", "Esteve no local do crime? ---> ", "Mora perto da vítima? ---> ", "Devia para a vítima? ---> ", "Já trabalhou com a vítima? ---> "]
# soma das respostas 
soma = 0
# contador q limita o while
i = 0
while i < len(perguntas):
    resp = input(perguntas[i]).upper()
    if resp == "sim":
        soma = soma + 1
    else:
        soma = soma
    i = i + 1
# condição para classificar o entrevistado
if soma < 2:
    print("Você é inocente!")
elif soma == 2:
    print("Você é suspeito!")
elif 4<= soma <= 5:
    print("Você é  cumplice!")
elif soma == 5:
    print("Você é o assassino!!")
'''