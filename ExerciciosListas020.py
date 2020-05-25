# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.
'''
20 - As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono. Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:

a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário
de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima.
Ao final, o programa deverá apresentar:
    O salário de cada funcionário, juntamente com o valor do abono;
    O número total de funcionário processados;
    O valor total a ser gasto com o pagamento do abono;
    O número de funcionário que receberá o valor mínimo de 100 reais;
    O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.
'''

# lista p salários
print('Digite 0 para encerrar o programa')
salarios = [] 
# while p n° indefinido de cadastros
while True:
    salario = float(input('Salário: '))
    # condição p prog parar
    if salario == 0:
        break
    # add lista salários
    salarios.append(salario)

print('Projeção de Gastos com Abono')
print('============================')
#\t coloca um table de separação
print('Salário\t\tAbono')
# contadores 
totalAbono = 0.0
totalPiso = 0
# criei um lista abono para saber o maior abono
listaAbono = []
# loop for para impresão ser interada a cada loop 
for salario in salarios:
    abono = salario * 0.2
    if (abono < 100):
        abono = 100.0
        totalPiso += 1
    listaAbono.append(abono)
    totalAbono += abono
    print(f'R$ {salario:.02f}\tR$ {abono:.02f}')
print('================================')
print(f'Foram processados {len(salarios)} salários')
print(f'Total gasto com abonos: R${totalAbono:.02f}')
print(f'Valor minimo pago a {totalPiso} colaboradores')
print(f'Maior valor de abono pago: R${max(listaAbono):.02f}')
print('================================')

