# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
15 - Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
Após esta entrada de dados, faça:
    a) Mostre a quantidade de valores que foram lidos;
    b) Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    c) Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    d)Calcule e mostre a soma dos valores;
    e)Calcule e mostre a média dos valores;
    f)Calcule e mostre a quantidade de valores acima da média calculada;
    g)Calcule e mostre a quantidade de valores abaixo de sete;
    h)Encerre o programa com uma mensagem;
'''
# lista p notas
notas = []

# loop infinito para notas 
while True:
    nota = float(input('Digite a nota. Para encerrar [-1]: '))
    # condição de parada digitar -1
    if nota < 0:
        break
    notas.append(nota)
# sum == soma as notas / len(notas) == n° de notas
media = sum(notas) / len(notas)
# 2 contadores acima da media e abaixo de 7
acimaMedia = 0
abaixo7 = 0
for n in notas:
    if n > media:
        acimaMedia += 1
    if n < 7:
        abaixo7 += 1

print(f'Quantidade de valores lidos: {len(notas)}')
print('Os valores que foram informados é:', notas)
'''# Percorre toda a lista de trás para frente
for i in reversed(notas):
    # Exibe o valor na tela um abaixo do outro
    print(i)'''
print('Os valores na ordem inversa à que foram informados é', notas[::-1])
print(f'A soma dos valores é: {sum(notas):.02f}')
print(f'A média dos valores é: {media:.02f}')
print(f'Quantidade de valores acima da média é: {acimaMedia}')
print(f'Quantidade de valores abaixo de sete é: {abaixo7}')
print('O programa foi encerrado')


