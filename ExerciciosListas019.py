# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
19 - Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"
As possíveis respostas são:
        1- Windows Server
        2- Unix
        3- Linux
        4- Netware
        5- Mac OS
        6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da
enquete e informe ao final o resultado da mesma. O programa deverá ler os
valores até ser informado o valor 0, que encerra a entrada dos dados.
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
Os valores referentes a cada uma das opções devem ser armazenados num vetor.
Após os dados terem sido completamente informados, o programa deverá calcular
a percentual de cada um dos concorrentes e informar o vencedor da enquete.
O formato da saída foi dado pela empresa, e é o seguinte:
        Sistema Operacional     Votos   %
        -------------------     -----   ---
        Windows Server           1500   17%
        Unix                     3500   40%
        Linux                    3000   34%
        Netware                   500    5%
        Mac OS                    150    2%
        Outro                     150    2%
        -------------------     -----
        Total                    8800
O Sistema Operacional mais votado foi o Unix, com 3500 votos,
correspondendo a 40% dos votos.
'''

print("\nQual o melhor Sistema Operacional para Servidores?\n")
print("""As opções são:
    1- Windows XP
    2- Unix
    3- Linux
    4- Netware
    5- Mac Os
    6- Outro
    Digite 0 para sair\n""")
# criei a lista votos 
votos = []
# 1 loop p add os votos
while True:
    # 2° loop p fazer computar os votos 
    while True:
        voto = int(input('Digite a opção: '))
        # condição de voto inválido
        if voto > 6 or voto < 0:
            print('Opção inválida.')
        else:
            break
    # condição para parar == 0
    if voto == 0:
        break
    votos.append(voto)
# criando a porcentagem count para soma os votos de cada opção / len total de votos * 100 p apresentar porcentagem
porcWin = votos.count(1) / (len(votos))*100
porcUni = votos.count(2) / (len(votos))*100
porcLin = votos.count(3) / (len(votos))*100
porcNet = votos.count(4) / (len(votos))*100
porcMac = votos.count(5) / (len(votos))*100
porcOut = votos.count(6) / (len(votos))*100
print("-----------------------------------------------------" )
print("Sistema Operacional     Votos          Porcentagem")
print("Windows XP              ", votos.count(1),"    ","    ""%(#)0.2f%%" % {"#" : porcWin} )
print("Unix                    ", votos.count(2),"    ","    ""%(#)0.2f%%" % {"#" : porcUni})
print("Linux                   ", votos.count(3),"    ","    ""%(#)0.2f%%" % {"#" : porcLin})
print("Netware                 ", votos.count(4),"    ","    ""%(#)0.2f%%" % {"#" : porcNet})
print("Mac Os                  ", votos.count(5),"    ","    ""%(#)0.2f%%" % {"#" : porcMac})
print("Outtros                 ", votos.count(6),"    ","    ""%(#)0.2f%%" % {"#" : porcOut})
print("-----------------------------------------------------\n")
print("Total  ", len(votos))