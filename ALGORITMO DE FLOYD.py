
INF = 99999

def floyd_warshall(grafo, V):
    distancia = grafo

    for k in range(V):
        for i in range(V):
            for j in range(V):
                distancia[i][j] = min(distancia[i][j], distancia[i][k] + distancia[k][j])

    imprimir_solucion(distancia, V)

def imprimir_solucion(distancia, V):
    print("Las distancias más cortas entre cada par de vértices:")
    for i in range(V):
        for j in range(V):
            if distancia[i][j] == INF:
                print("{:7}".format("INF"), end=" ")
            else:
                print("{:7}".format(distancia[i][j]), end=" ")
        print()

grafo = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]]
V = 4

floyd_warshall(grafo, V)
