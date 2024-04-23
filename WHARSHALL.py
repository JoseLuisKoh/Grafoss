def warshall(grafo):
    V = len(grafo)
    clausura_transitiva = [[0] * V for _ in range(V)]

    for i in range(V):
        for j in range(V):
            clausura_transitiva[i][j] = grafo[i][j]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                clausura_transitiva[i][j] = (clausura_transitiva[i][j] or 
                                             (clausura_transitiva[i][k] and clausura_transitiva[k][j]))

    return clausura_transitiva

# Ejemplo de uso
grafo = [[1, 1, 0, 1],
         [0, 1, 1, 0],
         [0, 0, 1, 1],
         [0, 0, 0, 1]]

clausura = warshall(grafo)
print("La clausura transitiva del grafo es:")
for fila in clausura:
    print(fila)
