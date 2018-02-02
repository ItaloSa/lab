def kruskal(m, n, arestas):
    geradora = [None for i in range(m)]
    resultante = []

    ordenada = sorted(arestas, key=arestas.get)
    print(ordenada)

    cnt = 0
    for i in ordenada:
        if i[0] not in geradora:
            if i[1] not in geradora:
                resultante.append((i[0], i[1]))
                geradora[cnt] = i[0]
        else:
            if i[1] not in geradora:
                resultante.append((i[0], i[1]))
                geradora[cnt] = i[0]
        cnt += 1

    #print(ordenada)
    #print(geradora)
    #print(resultante)
    return resultante

arestas = {
    (1, 2): 10,
    (2, 3): 5,
    (3, 1): 7
}

def start(m , n, arestas):
    resultante = kruskal(m, n, arestas)

    f = [ sorted(i) for i in resultante ]
    for i in sorted(f):
        saida = ''
        for j in i:
            saida += str(j) + ' '
        print(saida[:-1])

def main():
    cnt = 1
    while 1:
        e1 = input().split()
        n, m = int(e1[0]), int(e1[1])        
        if n is 0:
            break
        else:
            print('Teste ', cnt)
            arestas = {}
            for i in range(m):
                e2 = input().split()
                a, b, p = int(e2[0]), int(e2[1]), int(e2[2])
                arestas[(a, b)] = p
            start(m, n, arestas)
            #print(arestas)
            print()
        cnt += 1
            
        

main()