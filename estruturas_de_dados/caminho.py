#caminho mais curto
inf = float("inf")

class Vertice():
    def __init__(self, v, adj):
        self._v = v
        self._dist = inf
        self._pai = ''
        self._adj = adj
    
    def __repr__(self):
        return '<' + str(self._adj) + ' d ' + str(self._dist) + '>'
    
    def get_dist(self):
        return self._dist
    
    def get_pai(self):
        return self._pai

    def get_adj(self):
        return self._adj

    def set_dist(self, value):
        self._dist = value
    
    def set_pai(self, value):
        self._pai += str(value)
    
    def set_adj(self, value):
        self._adj = value

# grafo = {
#     'a': {'b': 1, 'd': 3},
#     'b': {'a': 1, 'c': 2},
#     'c': {'b': 2, 'd': 1},
#     'd': {'a': 3, 'c': 1}
# }

# grafo = {
#     '0': {'1': 2, '2': 4},
#     '1': {'0': 2, '3': 1},
#     '2': {'0': 4, '3': 5},
#     '3': {'1': 1, '2': 5}
# }



# def dijkstra():
def inicializa(grafo, start):
    distancias = {}
    vertices = {}
    q = {}
    for key, value in grafo.items():
        q[key] = inf
        vertices[key] = Vertice(key, value)
        #print('vertice: ' + str(vertices[key]))
        for item in value:
            #print(item)
            distancias[(key, item)] = grafo[key][item]

    vertices[start].set_dist(0)
    q[start] = 0

    #print(min(q, key=q.get))
    #print(vertices[min(q, key=q.get)])
    return distancias, vertices, q

def dijkstra(grafo, start):
    distancias, vertices, q = inicializa(grafo, start)
    s = {} #colocar só as distancias ('a', 'b'): peso
    #Sprint(distancias)
    while len(q) != 0:
        u = min(q, key=q.get)
        q.pop(u)
        s[u] = vertices[u].get_dist()
        #print(vertices[u].get_adj())
        for v, p in vertices[u].get_adj().items():
            #relaxa
            if vertices[v].get_dist() > vertices[u].get_dist() + distancias[(u,v)]:
                vertices[v].set_dist(vertices[u].get_dist() + distancias[(u,v)])
                q[v] = vertices[u].get_dist() + distancias[(u,v)]
                vertices[v].set_pai(u)
    #print(s)
    #s.pop(min(s, key=s.get))
    #print(vertices[min(s, key=s.get)])
    #print(max(s, key=s.get))
    return max(s.items(), key=lambda x: x[1])

def main():
    maximo = {}
    for i in range

dijkstra(grafo, '3')