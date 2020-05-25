# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
22 - Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles. 
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
    necessita da esfera;
    necessita de limpeza;
    a.necessita troca do cabo ou conector;
    a.quebrado ou inutilizado. 
Uma identificação igual a zero encerra o programa.

Ao final o programa deverá emitir o seguinte relatório:

Quantidade de mouses: 100
    Situação                        Quantidade              Percentual
    1- necessita da esfera                  40                     40%
    2- necessita de limpeza                 30                     30%
    3- necessita troca do cabo ou conector  15                     15%
    4- quebrado ou inutilizado              15                     15%
'''

# lista q para cada indice q vai acumular cada defeito
problemas = [0] * 4
# escreve o indice de cada defeito 
print('''1- necessita da esfera
2- necessita de limpeza
3- necessita troca do cabo ou conector
4- quebrado ou inutilizado ''')
# while para o cadastro indeterminado de mouse
while True:
    # número de identificação do mouse
    identificacao = int(input('Identificação: '))
    # condição para parar o programa
    if identificacao == 0:
        break
    # informa qual é o tipo de problema 
    problema = int(input('Digite o número do problema: '))
    # soma +1 p cada loop ao indice correspondente da lista 
    problemas[problema - 1] = problemas[problema - 1] + 1
                
print('Situação                          Quantidade         Percentual')
# função sum para soma os problemas 
total = sum(problemas)
# printe formatado = 100 * problemas / total para mostrar a porcetagem
print(f'1- necessita da esfera                  {problemas[0]}              {(100 * problemas[0]) / total:.02f}%')
print(f'2- necessita de limpeza                 {problemas[1]}              {(100 * problemas[1]) / total:.02f}%')
print(f'3- necessita troca do cabo ou conector  {problemas[2]}              {(100 * problemas[2]) / total:.02f}%')
print(f'4- quebrado ou inutilizado              {problemas[3]}              {(100 * problemas[3]) / total:.02f}%')
