class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []

    def agregar_arista(self, u, v, w):
        self.grafo.append([u, v, w])

    def encontrar(self, padre, i):
        if padre[i] == i:
            return i
        return self.encontrar(padre, padre[i])

    def unir(self, padre, rango, x, y):
        raiz_x = self.encontrar(padre, x)
        raiz_y = self.encontrar(padre, y)

        if rango[raiz_x] < rango[raiz_y]:
            padre[raiz_x] = raiz_y
        elif rango[raiz_x] > rango[raiz_y]:
            padre[raiz_y] = raiz_x
        else:
            padre[raiz_y] = raiz_x
            rango[raiz_x] += 1

    def kruskal(self):
        resultado = []
        i = 0
        e = 0
        self.grafo = sorted(self.grafo, key=lambda item: item[2])
        padre = []
        rango = []

        for nodo in range(self.V):
            padre.append(nodo)
            rango.append(0)

        while e < self.V - 1:
            u, v, w = self.grafo[i]
            i = i + 1
            x = self.encontrar(padre, u)
            y = self.encontrar(padre, v)

            if x != y:
                e = e + 1
                resultado.append([u, v, w])
                self.unir(padre, rango, x, y)

        print("Las aristas del árbol de expansión mínima son:")
        for u, v, w in resultado:
            print(f"Arista {u} -- {v} con peso {w}")

# Ejemplo de uso
grafo = Grafo(4)
grafo.agregar_arista(0, 1, 10)
grafo.agregar_arista(0, 2, 6)
grafo.agregar_arista(0, 3, 5)
grafo.agregar_arista(1, 3, 15)
grafo.agregar_arista(2, 3, 4)

grafo.kruskal()
