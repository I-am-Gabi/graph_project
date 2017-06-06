
def wsm(repository):
    size = len(repository.data[0].nodes)

    new_matrix = []
    for i in range(0, size):
        l = []
        for j in range(0, size):
            wsm_score = 0
            for m in repository.data:
                if m.connections_normalize.item(i, j) < 0:
                    #print(i, j)
                    wsm_score = -1
                    continue
                wsm_score += m.connections_normalize.item(i, j) * m.weight
            l.append(float(str(wsm_score)[:4]))
        new_matrix.append(l)

    return(new_matrix)




