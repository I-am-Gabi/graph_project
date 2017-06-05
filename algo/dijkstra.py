
def dijkstra(matrix, start, target):
    d = []
    rot = []
    d.append(0)
    rot.append(-1)
    A = [0]
    F = []
    for i in range(1, len(matrix[0])):
        d.append(-1)
        rot.append(0)
        A.append(i)

    while A:
        min_dist = d[0]
        r = 0
        for node in A:
            if d[node] != -1 and d[node] < min_dist:
                min_dist = d[node]
                r = node
        F.append(r)
        A.remove(r)
        for i in A:
            if matrix[i][r] == 0: continue
            for j in matrix[i]:

                p = min(d[j], (d[r] + 1.))
                if p < d[i]:
                    d[i] = p
                    rot[i] = r

    print(d)
    print(rot)
    print(F)





    #A = np.array(matrix)
    #G = nx.from_numpy_matrix(A, create_using=nx.DiGraph())
    #print(nx.dijkstra_path(G, 0, 3))

# grafo = Graph()
# print(grafo.repository.data)
# dijkstra(grafo.repository.data[1])
