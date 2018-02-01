#const
inf = float("inf")

#functs
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

# ------------------- MAIN --------------------------

def main():
    grafo = {}
    sequencial = []

    loop = int(input())
    for l in range(loop):
        entrada = input().split()
        if entrada[0] not in sequencial:
            sequencial.append(entrada[0])
        if entrada[1] not in sequencial:
            sequencial.append(entrada[1])
        if entrada[0] not in grafo:
            grafo[entrada[0]] = ({entrada[1]: 1 })
        else:
            grafo[entrada[0]].update({entrada[1]: 1})
        
    ordenado = sorted(sequencial)
    for i in range(len(ordenado)-1):
        if ordenado[i] in grafo:
            grafo[ordenado[i]].update({ordenado[i+1]: 1})
            if ordenado[i+1] in grafo:
                grafo[ordenado[i+1]].update({ordenado[i]: 1})
            else:
                grafo[ordenado[i+1]]= {ordenado[i]: 1}
        else:
            grafo[ordenado[i]] = ({ordenado[i+1]: 1})
            if ordenado[i+1] in grafo:
                grafo[ordenado[i+1]].update({ordenado[i]: 1})
            else:
                grafo[ordenado[i+1]]= {ordenado[i]: 1}


    x = input()

    comando = input().split()
    resultado = dijkstra(grafo, comando[0])
    print(resultado[comando[1]])


############# DEBUG ################

# grafo2 = {
#     'a': {'b': 1},
#     'b': {'c': 1, 'd': 1, 'a': 1},
#     'c': {'d': 1},
#     'd': {'c': 1}
# }
# x = dijkstra(grafo2, 'a')
# print(x)
main()