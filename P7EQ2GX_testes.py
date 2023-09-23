# P7EQ2GX.py
# Universidade Federal Fluminense
# Instituto de Matemática e Estatística
# Bacharelado em Estatística
# TCC0032 - Programação de Computadores
# Semestre 002/2023; Turma J1; 29/08/2023
# Professor John Reed
# Aluno: Frederick Caldas
# P7EQ2GX.py: Encontra as raízes da equação de segundo grau, de acordo com as demandas de cada caso.
# Estratégia: Segundo o princípio da eficiência e pelo método da classificação de problemas.

#
# Declaração de Objetos
from cmath import sqrt

# Recebe input do tipo float; do contrário, 
def input_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            print('O valor inserido foi: ', valor)
        except ValueError:
            print("Houve um erro. Tente novamente.")
            continue
        else:
            return valor  

def eq_2_gx():
    '''
    Classifica funções de segundo grau e, em seguida, encontra suas raízes.

    Argumentos: Coeficientes da equação

    Retorna: Se a função possui raízes reais ou complexas, e diz os valores.
    '''
    # boas-vindas
    print('Bem-vindo, senhor usuário! \n Programa EQ2GX')
    
    # inserindo o coeficiente A
    A = input_float('Insira o coeficiente A: ')
    B = input_float('Insira o coeficiente B: ')
    C = input_float('Insira o coeficiente C: ')

    # fórmulas utilizadas
    delta = B ** 2 - 4 * A * C
    bhaskara_r1 = (- B + sqrt(delta)) / 2 * A
    bhaskara_r2 = (- B - sqrt(delta)) / 2 * A
    c2r1 = (- sqrt(- 4 * A * C)) / 2 * A
    c2r2 = (sqrt(- 4 * A * C)) / 2 * A
    c3r1 = - B / 2 * A

    # classificação de casos
    if A == 0:
        print('Esta não é uma equação de segundo grau.')
    else:
        if delta < 0:
            if B != 0:
                print('Esta equação de segundo grau possui duas raízes complexas')
                print('As raízes da equação são ',
                      bhaskara_r1, 'e ', bhaskara_r2)
            else:
                print(
                    'Esta equação de segundo grau possui raízes puramente imaginárias.')
                print('As raízes da equação são ', c2r1, 'e ', c2r2)
        else:
            if delta == 0:
                print('Esta equação de segundo grau possui duas raízes reais iguais.')
                if B == 0:
                    print('A raíz da equação é ', 0)
                else:
                    print('A raíz da equação é ', c3r1)
            else:
                print('Esta equação de segundo grau possui duas raízes reais distintas')
                print('As raízes da equação são ',
                      bhaskara_r1, 'e ', bhaskara_r2)
    # Despedida
    print("Procedimento Concluído. Obrigado pela paciência.")


# Terminação [Em outras linguagens, que não o Python, exigem alguns comandos de terminação]
eq_2_gx()
