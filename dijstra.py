import sys

class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = [[0 for columna in range(vertices)] for fila in range(vertices)]

    def imprimir_solucion(self, distancias):
        print("Vertice \tDistancia desde el vertice de origen")
        for nodo in range(self.V):
            print(nodo, "\t", distancias[nodo])

    def minima_distancia(self, distancias, conjunto_cerrado):
        minima = sys.maxsize
        for v in range(self.V):
            if distancias[v] < minima and conjunto_cerrado[v] == False:
                minima = distancias[v]
                indice_minima = v
        return indice_minima

    def dijkstra(self, vertice_origen):
        distancias = [sys.maxsize] * self.V
        distancias[vertice_origen] = 0
        conjunto_cerrado = [False] * self.V

        for _ in range(self.V):
            u = self.minima_distancia(distancias, conjunto_cerrado)
            conjunto_cerrado[u] = True
            for v in range(self.V):
                if self.grafo[u][v] > 0 and conjunto_cerrado[v] == False and distancias[v] > distancias[u] + self.grafo[u][v]:
                    distancias[v] = distancias[u] + self.grafo[u][v]

        self.imprimir_solucion(distancias)

grafo = Grafo(9)
grafo.grafo = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]]

grafo.dijkstra(0)
