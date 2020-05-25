# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
21 - Faça um programa que carregue uma lista com os modelos de cinco carros
(exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o
consumo desses carros, isto é, quantos quilômetros cada um desses carros faz
com um litro de combustível. Calcule e mostre:
    O modelo do carro mais econômico;
    Quantos litros de combustível cada um dos carros cadastrados consome para
    percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo.Os dados são fictícios e podem mudar a cada execução do programa
Comparativo de Consumo de Combustível
        Veículo 1
        Nome: fusca
        Km por litro: 7
        Veículo 2
        Nome: gol
        Km por litro: 10
        Veículo 3
        Nome: uno
        Km por litro: 12.5
        Veículo 4
        Nome: Vectra
        Km por litro: 9
        Veículo 5
        Nome: Peugeout
        Km por litro: 14.5
Relatório Final
    1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
    2 - gol             -   10.0 -  100.0 litros - R$ 225.00
    3 - uno             -   12.5 -   80.0 litros - R$ 180.00
    4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
    5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17

O menor consumo é do peugeout.
'''

print('Comparativo de Consumo de Combustivel')
# lista de veiculose consumo
veiculos = []
consumo = []
preco = 2.25
# laço for para pedir moledo e consumo e add as listas
for i in range(1, 4):
    veiculos.append(input('Veiculo %d: ' % i))
    consumo.append(float(input('Km por litro: ')))

print('Relatorio Final')
# contadores para menor consumo
eco = 0
ecoIndice = 0
i = 0
# laço for p impressão indentada da lista veiculos
for i in range(0, 3):
    # caculos do custo e gasto
    custo = 1000 / consumo[i]
    gasto = custo * preco
    print(f'{i + 1} - {veiculos[i]} - {consumo[i]:.02f} - {custo:.01f} litros - R$ {gasto:.02f}')
    # condição para menor consumo
    if consumo[i] > eco:
        eco = consumo[i]
        ecoIndice = i
    i = i + 1
print( "o carro mais economico eh o ",veiculos[ecoIndice],".")
 
