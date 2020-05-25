# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
18 - Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++.
Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número.
Após o final da votação, o programa deverá exibir:
        O total de votos computados;
        Os númeos e respectivos votos de todos os jogadores que receberam votos;
        O percentual de votos de cada um destes jogadores;
        O número do jogador escolhido como o melhor jogador da partida,
        juntamente com o número de votos e o percentual de votos dados a ele.
Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e
retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco,
obedecendo a mesma disposição apresentada na tela.
'''

# lista q para cada indice vai acumulando os votos 
votosAtletas = [0] * 23
numeroAtleta = -1
# contador de todos os votos
totalVotos = 0
print('Enquete: Quem foi o melhor jogador?')
# loop while p soma infinita de votos
while (numeroAtleta != 0):
    numeroAtleta = int(input('Numero do jogador (0=fim): '))
    # só aceita votos do 1 até 23
    if (numeroAtleta < 0) or (numeroAtleta > 23):
        print('Informe um valor entre 1 e 23 ou 0 para sair!')
        continue
    # para parar digite 0
    if (numeroAtleta != 0):
        # se != 0 voto será inserido na posição do indice da lista e não no valor digitado +1 p cada loop de voto
        votosAtletas[numeroAtleta - 1] += 1
        # soma +1 contador totalVotos == 0
        totalVotos += 1

print('Resultado da votacao:')

print('Foram computados %d votos' % totalVotos)
# \t equivale a 1 tab de formatação e 2 (%%) p segunda ser exibida
print('Jogador\tVotos\t%%')
contador = 1
# vai indicar o melhor quando da comparação if
melhorJogador = 0
# laço for p impressão indentada p cada jogador dentroda lista
for votosAtleta in votosAtletas:
    # condição p exibir só serão exibidos os atletas com pelomenos 1 voto (voto>0)
    if (votosAtleta > 0):
        # repitir formatação \t p todos ficarem um abaixo do outro
        print('%d\t%d\t%.2f%%' %\
              (contador, votosAtleta, votosAtleta / float(totalVotos) * 100))
        # condição p saber quem teve mais votos (melhorJogador)
        if (votosAtleta > votosAtletas[melhorJogador]):
            melhorJogador = contador - 1
    contador += 1
# melhorJogador + 1 == pq melhorJogador = incice, mas o voto foi na sua camisa então deve +1 p ser o atleta correspondente 
# votosAtletas[melhorJogador] são os voto pego pelo indice da lista 
print('O melhor jogador foi o numero %d, com %d votos, correspondendo a '\
    '%.2f%% do total de votos' %\
    (melhorJogador + 1, votosAtletas[melhorJogador],
        votosAtletas[melhorJogador] / float(totalVotos) * 100))
        
    


    