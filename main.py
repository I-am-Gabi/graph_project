import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp

def draw_graph(input_data, node_size=1600, node_color='blue',
               node_alpha=0.3, node_text_size=12, edge_color='blue',
               edge_alpha=0.3, edge_tickness=1, text_font='sans-serif'):


    G = nx.DiGraph(input_data.values)
    A = nx.adjacency_matrix(G)
    print(A.todense())
    graph_pos=nx.shell_layout(G)

    # draw graph
    nx.draw_networkx_nodes(G,graph_pos,node_size=node_size,
                           alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
                           alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
                            font_family=text_font)

    # show graph
    plt.show()


if __name__ == '__main__':
    input_data = pd.read_csv('cost.txt', index_col=0)
    draw_graph(input_data)