class Vertice:
    def __init__(self, n):
        self.nombre = n
        self.vecinos = list()

        self.d = 0
        self.f = 0
        self.color = 'white'
        self.pred = -1

    def agregarVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)
            self.vecinos.sort()

class Grafo:
    def __init__(self):
        self.vertices = {}
        self.tiempo = 0

    def agregarVertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            return True
        else:
            return False

    def agregarArista(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].agregarVecino(v)
            self.vertices[v].agregarVecino(u)
            return True
        else:
            return False

    def imprimeGrafo(self):
        for key in sorted(list(self.vertices.keys())):
            print("Vertice: " + key)
            print("Descubrimiento/Termino: " + str(self.vertices[key].d) + "/" + str(self.vertices[key].f))

    def dfs(self):
        for u in sorted(self.vertices):
            if self.vertices[u].color == 'white':
                self.dfsVisitar(self.vertices[u])

    def dfsVisitar(self, vert):
        self.tiempo += 1
        vert.d = self.tiempo
        vert.color = 'gris'

        for v in vert.vecinos:
            if self.vertices[v].color == 'white':
                self.vertices[v].pred = vert.nombre
                self.dfsVisitar(self.vertices[v])
        vert.color = 'black'
        self.tiempo += 1
        vert.f = self.tiempo

class Controladora:
    def main(self):
        # Se crea un objeto 'g' de la clase Grafo
        g = Grafo()
        # Se crea un objeto 'a' de la clase Vertice, un vértice
        a = Vertice('a')
        # Se agrega el vértice al grafo
        g.agregarVertice(a)
        # Esta estructura de repetición es para agregar todos los vértices y no hacerlo uno a uno
        for i in range(ord('a'), ord('e')):
            g.agregarVertice(Vertice(chr(i)))

        # Se declara una lista que contiene las aristas del grafo
        edges = ['ab', 'ad', 'bc', 'bd', 'cd']
        # Se agregan las aristas al grafo
        for edge in edges:
            g.agregarArista(edge[0], edge[1])

        # Se realiza DFS
        g.dfs()

        # Se imprime el grafo, como lista de adyacencia
        print("Grafo 1\n")
        g.imprimeGrafo()

# Ejecución del programa
obj = Controladora()
obj.main()
