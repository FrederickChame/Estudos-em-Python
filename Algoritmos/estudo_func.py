# Registro de algumas funções que andei construindo para me exercitar


import numpy as np
import math

#########################################
#           FUNÇÕES MATEMÁTICAS         #
#########################################

def dec_to_bin(numero):
    '''
    Função que converte números decimais em números binários
    '''
    resultado = 0
    indice = 1
    while numero > 0:
        if numero % 2 == 1:
            resultado += 1 * indice
            numero = (numero - 1) / 2
            indice = indice * 10
        if numero % 2 == 0:
            indice = indice * 10
            numero = numero / 2
    return resultado        

def bin_to_dec(numero):
    '''
    Tentativa de criar uma função que converte valores decimais com ponto flutuante em seu valor correspondente em representação decimal.
    '''
    numero = str(numero)
    if '.' in numero:
        alg_int = []
        alg_frac = []
        i = 0
        while str(numero)[i] != '.':
            alg_int.append(str(numero)[i])
            i += 1
            print('processando')
        if str(numero)[i] == '.':
            i += 1
            while i <= len(str(numero)) - 1:
                alg_frac.append(str(numero)[i])
                print('processando.')
                i += 1

        alg_int_ordenados = alg_int[::-1]
        indice = 0
        representacao_int = 0
        for algarismo in alg_int_ordenados:
            representacao_int += int(algarismo) * (2 ** indice)
            indice += 1
            print('processando..')
        index = 1
        representacao_frac = 0
        for digito in alg_frac:
            representacao_frac += int(digito) * (2 ** - index)
            index += 1
            print('processando...')
        return representacao_int + representacao_frac
    else: #Tratamento de casos onde o input é inteiro
        algarismos = [int(x) for x in str(numero)] # Cria uma lista com os algarismos do número a ser convertido
        algarismos_ordenados = algarismos[::-1] # Ordena-os de modo a iniciar o tratamento pelas unidades
        indice = 0
        representacao_int = 0
        for algarismo in algarismos_ordenados:
            representacao_int += algarismo * (2 ** indice)
            indice += 1
            print('processando int...')
        return representacao_int
    
def mdc(num1, num2):
    '''Tentativa de implementação do Algoritmo de Euclides para obter o MDC de dois números'''
    candidato = num2
    resto = num1 % num2
    while resto != 0:
        resto_passado = resto
        resto = candidato % resto
        candidato = resto_passado
    if resto == 0:
        return candidato

def fatorial(numero):
    if numero == 0:
        return 1
    elif 0 < numero <= 2:
        return numero
    else:
        resultado = numero
        anterior = numero - 1
        while anterior != 1:
            resultado *= anterior
            anterior -= 1
        return resultado
    
def arranjo(n,k):
    return (fatorial(n)/fatorial(n - k))

def combinacao(n, k):
    return (fatorial(n)/(fatorial(k) * fatorial(n - k)))

#########################################
#           FUNÇÕES ESTATÍSTICAS        #
#########################################

def freq_rel(freq_evento, espaco_amostral):
    '''função que retorna a frequência relativa de um evento'''
    if type(freq_evento) == list:
        pass
    return freq_evento / len(espaco_amostral)

def num_classes(tamanho_amostra):
    '''Função que retorna o número de classes recomendado para agrupar intervalos de dados contínuos.
     Esse valor é também conhecido como Expressão de Sturges'''
    from math import log
    return 1 + 3.3 * log(tamanho_amostra)

def percentil(lista:list, porcentagem:int):
    '''     --- FUNÇÃO PARA DADOS NÃO AGRUPADOS ---
    Dada uma lista de valores, retorna o percentil desejado.
    O valor retornado pela função indica:
    a) No valor inteiro, a posição da lista em que se encontra o percentil desejado
    b) No valor decimal, indica se o percentil encontra-se numa posição exata da lista ou aproximadamente entre duas posições registradas
    
    Exemplo de interpretação: o 99º Percentil indica que 99% dos valores da lista (amostra) são inferiores ao valor do percentil,
    e 1% são maiores.'''
    return (((len(lista)/100) * porcentagem) + (1/2))

def percentil_agrupados(lista:list, porcentagem:int):
    '''     --- FUNÇÃO PARA DADOS AGRUPADOS EM CLASSES ---
    Dada uma lista de valores particionada em classes, retorna o percentil
    Como interpretar:
    Compare o valor retornado pela função com a coluna das frequências acumuladas;
    Observe qual é a primeira linha que possui uma frequência acumulada maior do que o percentil obtido
    O percentil obtido encontra-se na classe da linha imediatamente anterior à linha observada.'''
    percentil = ((sum(lista)/100) * porcentagem)
    return percentil

def outliers_boxplot(lista:list):
    AIQ = percentil(lista, 75) - percentil(lista, 25)
    outliers = []
    for i in lista:
        if i > (percentil(lista, 75) + 1.5 * AIQ) or (i < percentil(lista, 25) - 1.5 * AIQ):
            outliers.append(i)
    return outliers

################################################
#           FUNÇÕES DE MACHINE LEARNING        #
################################################

# Dados de Exemplo
X = np.random.randint(1,10, size=(100,1)) # Gerando uma lista de dados cujos valores estao entre 1 e 10
y = 1000 + 20000 * X + np.random.randint(1,100) * 1000 # Regra da relação linear que existe entre os dados X e y, e que buscamos descobrir através do modelo 
parametros = np.random.randn(2,1)
taxa_aprendizado = 0.01
iteracoes = 500
X_bias = np.c_[np.ones((100,1)), X] # Adiciona coluna de uns que servirá para colher do algoritmo o bias

def mean_squared_error(caracteristicas, rotulos_alvo, parametros):
    num_exemplos = len(rotulos_alvo)
    custo = (1/2*num_exemplos) * np.sum(np.square(caracteristicas.dot(parametros) - rotulos_alvo))
    return custo

def gradiente_descendente(caracteristicas, rotulos_alvo, parametros, taxa_aprendizado, iteracoes):
    num_exemplos = len(rotulos_alvo)
    historico_custo = np.zeros(iteracoes)
    for i in range(iteracoes):
        gradientes = 1/num_exemplos * caracteristicas.T.dot(caracteristicas.dot(taxa_aprendizado) - rotulos_alvo)
        parametros = parametros - taxa_aprendizado * gradientes
        historico_custo[i] = mean_squared_error(caracteristicas, rotulos_alvo, parametros)
    return parametros, historico_custo

# Uma vez obtidos os parametros satisfatórios com o modelo, basta realizar o produto vetorial entre os novos parametros e os novos dados sob o formato X_bias
y_predicao = X_bias.dot(parametros)

#######################################################
# MÚSICA #
######################################################

def escala_maior(tonica):
    '''
    Recebe a tônica e retorna a sua escala maior correspondente.
    '''
    # Começa de todas as opções cromáticas
    cromatica = ["Dó", "Dó#", "Ré", "Ré#", "Mi", "Fá", "Fá#", "Sol", "Sol#", "Lá", "Lá#", "Si"]
    
    # Cria ordenação da lista cromática partindo da tonica
    indice_tonica = cromatica.index(tonica)
    tonica_cromatica = cromatica[indice_tonica:] + cromatica[:indice_tonica]
    
    # Seleciona intervalos de escala maior a partir dos indices
    tonica_maior = [tonica_cromatica[i] for i in [0, 2, 4, 5, 7, 9, 11]]
    return tonica_maior

#print(escala_maior("Ré"))

def escala(tonica, modo= None):
    '''
    Recebe a tônica e retorna a sua escala maior correspondente.
    '''
    # Modos possíveis
    modos = {
             "Maior": [0, 2, 4, 5, 7, 9, 11],
             "Dórico": [0, 2, 3, 5, 7, 9, 10],
             "Frígio": [0, 1, 3, 5, 7, 8, 10],
             "Lídio": [0, 2, 4, 6, 7, 9, 11],
             "Mixolídio": [0, 2, 4, 5, 7, 9, 10],
             "Menor": [0, 2, 3, 5, 7, 8, 10],
             "Lócrio": [0, 1, 3, 5, 6, 8, 10]}

    # Começa de todas as opções cromáticas
    cromatica = ["Dó", "Dó#", "Ré", "Ré#", "Mi", "Fá", "Fá#", "Sol", "Sol#", "Lá", "Lá#", "Si"]
    
    # Cria ordenação da lista cromática partindo da tonica
    indice_tonica = cromatica.index(tonica)
    tonica_cromatica = cromatica[indice_tonica:] + cromatica[:indice_tonica]
    
    if modo in modos:
        # Seleciona intervalos de escala desejada a partir dos indices
        escala_desejada = [tonica_cromatica[i] for i in modos[modo]]
        return escala_desejada
    else:
    # Retorna um dicionário com todas as escalas diatônicas
        escalas_diatonicas = {}
        for chave, valor in modos.items():
            escalas_diatonicas[chave] = [tonica_cromatica[i] for i in modos[chave]]
        return escalas_diatonicas
        
# print(escala("Dó", "Lócrio"))

def qual_escala_maior(notas: list):
    """
    Função que recebe uma lista de notas e retorna quais são as escalas candidatas ao uso.
    Convenção: as notas na lista devem começar em maiúsculo, e não devem ser utilizados bemóis.
    """
    escalas = {
                "Dó Maior":["Dó", "Ré", "Mi", "Fá", "Sol", "Lá", "Si"],
                "Ré Maior":["Ré", "Mi", "Fá#", "Sol", "Lá", "Si", "Dó#"],
                "Mi Maior":["Mi", "Fá#", "Sol#", "Lá", "Si", "Dó#", "Ré#"],
                "Fá Maior":["Fá", "Sol", "Lá", "Lá#", "Dó", "Ré", "Mi"],
                "Sol Maior":["Sol", "Lá", "Si", "Dó", "Ré", "Mi", "Fá#"],
                "Lá Maior":["Lá", "Si", "Dó#", "Ré", "Mi", "Fá#", "Sol#"],
                "Si Maior":["Si", "Dó#", "Ré#", "Mi", "Fá#", "Sol#", "Lá#"]
               }
    candidatas = []
    notas = set(notas)
    for chave, valor in escalas.items():
        set(valor)
        if notas.issubset(valor) == True:
            candidatas.append(chave)
    return candidatas
        
# notas_candidatas = ["Dó"]
# print(qual_escala_maior(notas_candidatas))


'''
def qual_escala(notas: list, escala_especifica=None):
    
    # Começa de todas as opções cromáticas
    cromatica = ["Dó", "Dó#", "Ré", "Ré#", "Mi", "Fá", "Fá#", "Sol", "Sol#", "Lá", "Lá#", "Si"]    
    

    # É necessário? Talvez verificar apenas se está presente na escala maior e daí fazer os ajustes para as demais.
    for i in cromatica:
        total_escalas = escala(i)

    # Dá para reaproveitar algo daqui debaixo?
    candidatas = []
    notas = set(notas)
    for chave, valor in escalas.items():
        set(valor)
        if notas.issubset(valor) == True:
            candidatas.append(chave)

    # Criar um objeto que recebe o nome da tônica + o nome do modo e depois retorná-lo na função.

    return dicionario_nomes_escalas
'''