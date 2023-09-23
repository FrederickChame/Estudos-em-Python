# inspirado no livro: Entendendo Algoritmos - Aditya Y. Bhargava

from collections import deque

grafo = {}
grafo['voce'] = ['Mikaela', 'Lucas', 'Pedro', 'Matheus', 'Jaqueline']
grafo['Mikaela'] = ['Ruan', 'Vera', 'Marco']
grafo['Lucas'] = ['Matheus']
grafo['Pedro'] = ['Jaqueline', 'Leonardo']
grafo['Marco'] = ['Vera']
grafo['Vera'] = ['Marco']
grafo['Matheus'] = ['Lucas']
grafo['Leonardo'] = ['Keller', 'Jaqueline', 'Pedro']

# critério
def pessoa_e_vendedor(nome):
    return nome[-1] == 'r' # se o nome da pessoa termina com r, ela é uma vendedora.

# pesquisa em largura: procura um vendedor de café.
def pesquisa(nome):
    fila_de_pesquisa = deque()              # cria uma nova lista.
    fila_de_pesquisa += grafo[nome]        # adiciona todos os seus vizinhos à lista de pesquisa.
    verificadas = []                            # registro de pessoas que já foram verificadas.

    while fila_de_pesquisa:                     # enquanto a fila de pesquisa não estiver vazia...
        try:
            pessoa = fila_de_pesquisa.popleft()         # pega a primeira pessoa da fila
            if not pessoa in verificadas:               # verifica somente se a pessoa já não tiver sido verificada.
                if pessoa_e_vendedor(pessoa):           # verifica se a pessoa é uma vendedora de café.
                    print(pessoa + ' é um vendedor de café!')     # sim, ela é uma vendedora de café.
                    return True
                else:                                               # não, ela não é uma vendedora de café.
                    fila_de_pesquisa += grafo[pessoa]               # adiciona todos os amigos dessa pessoa à lista.
                    verificadas.append(pessoa)              # marca a pessoa como verificada.
        except KeyError:                                    # se uma pessoa não for uma key, não tem amigos. 
            continue                                        #  não adicionar amigos
    return False                    # se acabar a fila, ninguém é vendedor

pesquisa('voce')