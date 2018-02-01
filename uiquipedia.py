''' 
entrada

A B
A C
C D

'''
cnt = 0
found = False

def sequencial(indice, palavra1, palavra2):
    d1 = indice.index(palavra1)
    d2 = indice.index(palavra2)
    return abs(d1 - d2)

def direta(grafo, palavra1, palavra2):
    global cnt, found
    if palavra1 == palavra2:
        found = True
        return cnt
    if palavra1 in grafo:
        cnt += 1
        for palavra in grafo[palavra1]:
            direta(grafo, palavra, palavra2)
    else:
        return None

palavras = {}
grafo = {}

comando1 = int(input())
for i in range(comando1):
    inpt = input().split()
    #sequencial
    for palavra in inpt:
        if palavra not in palavras:
            palavras[palavra] = 1 #peso
    #grafo
    if inpt[0] not in grafo:
        grafo[inpt[0]] = [inpt[1]]
    else:
        grafo[inpt[0]].append(inpt[1])

#linha em branco
x = input()

indice = sorted(palavras)

#print(indice)
#print(grafo)
#print('')

busca = input().split()
palavra1 = busca[0]
palavra2 = busca[1]

seq = sequencial(indice, palavra1, palavra2)
direta(grafo, palavra1, palavra2)  

if found:
    print(min(seq, cnt))
else:
    print(seq)