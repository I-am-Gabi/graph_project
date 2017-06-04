from engine.repository import Repository

# Algorítmo para verificação e identificação de gargalos.

def gargalo(matrix):
    sugestoes = []
    for index_origem in range(len(matrix.nodes)):
        # print('origem: '+str(index_origem))
        for index_destino in range(index_origem, len(matrix.nodes)):
            # print('destino: ' + str(index_destino))
            if index_origem == index_destino:
                continue
            s = gargalo_origem_destino(matrix, index_origem, index_destino)
            if s != None:
                sugestoes.append(s)
    return sugestoes


def gargalo_origem_destino(matrix, index_origem, index_destino):

    no_origem = index_origem
    no_destino = index_destino

    caminho = []
    pais = []
    cores = []

    pilha = [no_origem]

    for _ in matrix.nodes:
        cores.append('w')
        pais.append(None)

    # DFS do grafo
    while pilha:
        no_atual = pilha.pop()
        cores[no_atual] = 'g'

        adjs = matrix.get_adjs(no_atual)
        for adj in adjs:
            if cores[adj] == 'w':
                pais[adj] = no_atual
                pilha.append(adj)

        cores[no_atual] = 'b'

    # construir caminho a partir do DFS
    no_atual = no_destino
    caminho.append(no_atual)
    while no_atual !=  no_origem:
        no_atual = pais[no_atual]
        caminho.append(no_atual)

    if len(caminho) <= 2:
        return None

    caminho_reverso = reversed(caminho)
    caminho = []
    for no in caminho_reverso:
        caminho.append(no)
    print('caminho: '+str(caminho))

    # pegar menor e maior valor das conexões
    valor_menor = None
    origem_menor = None
    destino_menor = None

    valor_maior = None
    origem_maior = None
    destino_maior = None
    for index in range(0,(len(caminho)-1)):
        if valor_menor == None or matrix.connections.item(caminho[index], (caminho[index+1])) < valor_menor:
            valor_menor = matrix.connections.item(caminho[index], (caminho[index+1]))
            origem_menor = index
            destino_menor = index + 1
        if valor_maior == None or matrix.connections.item(caminho[index], (caminho[index+1])) > valor_maior:
            valor_maior = matrix.connections.item(caminho[index], (caminho[index + 1]))
            origem_maior = index
            destino_maior = index + 1

    return {'caminho': caminho,
            'menor':{'aresta_origem': origem_menor,
                     'aresta_destino': destino_menor,
                     'valor_aresta': valor_menor},
            'maior':{'aresta_origem': origem_maior,
                     'aresta_destino': destino_maior,
                     'valor_aresta': valor_maior}}


reposirorio = Repository()
print(reposirorio.data[1].connections)
print(gargalo(reposirorio.data[1]))