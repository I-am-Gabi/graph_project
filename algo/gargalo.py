#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Algorítmo para verificação e identificação de gargalos.


def gargalo(matrix):
    sugestoes = {'nos_desconexos': [], 'gargalos': []}
    nos_desconexos = False
    for index_origem in range(len(matrix.nodes)):
        # print('origem: '+str(index_origem))
        for index_destino in range(index_origem, len(matrix.nodes)):
            # print('destino: ' + str(index_destino))
            if index_origem == index_destino:
                continue
            s = gargalo_origem_destino(matrix, index_origem, index_destino)
            if s is not None:
                if not nos_desconexos:
                    if 'nos_desconexos' in s:
                        sugestoes['nos_desconexos'] = s['nos_desconexos']
                        del s['nos_desconexos']
                        nos_desconexos = True
                else:
                    del s['nos_desconexos']
                sugestoes['gargalos'].append(s)
    return sugestoes


def gargalo_origem_destino(matrix, index_origem, index_destino):

    no_origem = index_origem
    no_destino = index_destino

    caminho = []
    pais = []
    cores = []

    descoconexos = []

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

    for i in range(len(matrix.nodes)):
        if cores[i] == 'w':
            descoconexos.append(i)

    if cores[no_destino] == 'w':
        return None

    # construir caminho a partir do DFS
    no_atual = no_destino
    caminho.append(no_atual)
    while no_atual != no_origem:
        no_atual = pais[no_atual]
        caminho.append(no_atual)

    if len(caminho) <= 2:
        return None

    caminho_reverso = reversed(caminho)
    caminho = []
    for no in caminho_reverso:
        caminho.append(no)
    # print('caminho: '+str(caminho))

    # pegar menor e maior valor das conexões
    valor = None
    origem = None
    destino = None
    for index in range(0, (len(caminho)-1)):
        if matrix.type == 'cost':
            if valor is None or matrix.connections.item(caminho[index], (caminho[index + 1])) > valor:
                valor = matrix.connections.item(caminho[index], (caminho[index + 1]))
                origem = index
                destino = index + 1
        else:
            if valor is None or matrix.connections.item(caminho[index], (caminho[index + 1])) < valor:
                valor = matrix.connections.item(caminho[index], (caminho[index + 1]))
                origem = index
                destino = index + 1

    dados = {'caminho': caminho, 'aresta_origem': origem, 'aresta_destino': destino, 'valor_aresta': valor}

    if descoconexos:
        dados['nos_desconexos'] = descoconexos

    return dados
