
inf = float("inf")

# grafo2 = {
#     0: {1: 2, 2: 4},
#     1: {3: 1, 0: 2},
#     2: {0: 4, 3: 5},
#     3: {1: 1, 2: 5}
# }

def inicializa(grafo, s):
    distancias = {}
    for vertice in grafo.items():
        distancias[vertice[0]] = inf
    distancias[s] = 0 
    return distancias

def relaxa(grafo, q, u, dist_de_u, v):
    try:
        if q[v] > dist_de_u + grafo[u][v]:
            q[v] = dist_de_u + grafo[u][v]
    except:
        pass


def dijkstra(grafo, s):
    distancias = inicializa(grafo, s)
    s = {}
    q = distancias
    while len(q) is not 0:
        u = min(q, key=q.get)
        dist_de_u = q.pop(u)
        s[u] = dist_de_u
        for vertice in grafo[u]:
            relaxa(grafo, q, u, dist_de_u, vertice)
    return s

def start(grafo, vertices):
    #x = inicializa(grafo , 0)
    minimo = inf
    for i in range(vertices):
        d = dijkstra(grafo, i)        
        d.pop(min(d, key=d.get))
        #print(d)
        k = d[max(d, key=d.get)]       
        if k < minimo:
            minimo = k
    print(minimo)

grafo = {}

c1 = input().split()
for j in range(int(c1[0])):
    grafo[j] = {}
for i in range(int(c1[1])):
    c2 = input().split()    
    if int(c2[1]) not in grafo[int(c2[0])]:
        grafo[int(c2[0])].update({int(c2[1]):int(c2[2])})
        grafo[int(c2[1])].update({int(c2[0]):int(c2[2])})
    else: 
        #print(grafo[int(c2[0])][int(c2[1])], ' > ', int(c2[2]))
        if grafo[int(c2[0])][int(c2[1])] > int(c2[2]):
            grafo[int(c2[0])].update({int(c2[1]):int(c2[2])})
            grafo[int(c2[1])].update({int(c2[0]):int(c2[2])})


    
#print(grafo)

start(grafo, int(c1[0]))