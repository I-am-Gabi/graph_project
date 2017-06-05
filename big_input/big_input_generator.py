import numpy as np

linhas = 2000
colunas = 2000

m = np.random.rand(linhas, colunas)
# print(m.item(0, 0))

for linha in range(linhas):
    for coluna in range(colunas):
        if linha == coluna:
            m.itemset((linha, coluna), 0)
        elif coluna > linha:
            continue
        elif coluna < linha:
            m.itemset((coluna, linha), m.item(linha, coluna))

print(m.item(5, 5))

print(m.item(0, 1))
print(m.item(1, 0))

print(m.item(55, 100))
print(m.item(100, 55))
