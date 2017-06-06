#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np

from engine.Action import Action

sys.path.append('../')

from algo.dijkstra import dijkstra
from algo.gargalo import gargalo

from engine.repository import Repository
from engine.wsm import wsm
from engine.normalize import normalize


def run(action, choice=None, start=None, target=None):
    r = Repository()
    r.build()

    if action == Action.SPM:
        return(run_spm(r, start, target))
    elif action == Action.BOTTLENECK:
        return(run_analyzer_bottleneck(choice))


def run_spm(r, start, target):
    normalize(r)
    final_matrix = wsm(r)
    best_path = dijkstra(final_matrix, start, target)[::-1]
    return best_path


def run_analyzer_bottleneck(choice):
    matrix_index = choice - 1
    return gargalo(r.data[matrix_index])


if __name__ == '__main__':
    while True:
        try:
            escolha = eval(input('Escolha uma ação. Opções disponíveis:\n1. Caminho mínimo\n2. Identificar gargalos\n'))
            r = Repository()
            r.build()
            # dijikstra
            if escolha == 1:
                normalize(r)

                result = wsm(r)

                print('Nós do grafo: ' + str(r.data[0].nodes))
                start = eval(input('Escolha o nó de partida do pacote\n'))
                target = eval(input('Escolha o nó de chegada do pacote\n'))

                final_result = dijkstra(result, start, target)[::-1]

                print(final_result)
                break
            # gargalo
            elif escolha == 2:
                try:
                    escolha = eval(input('Escolha um critério a ser analisado. Opções disponíveis:\n1. Banda\n2. '
                                         'Distância\n'))
                    if escolha != 1 and escolha != 2:
                        raise NameError

                    index_matrix = escolha - 1

                    print(gargalo(r.data[index_matrix]))
                    break
                except NameError:
                    raise NameError
            else:
                raise NameError
        except NameError:
            print('Opção inválida!')
