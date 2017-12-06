# inicio debug ---------------------------------


def debug_ma(ma):
    for li in ma:
        print(li)
#fim debug -------------------------------------
def matriz(i,j):
    matriz = []
    for i in range(i+2):
        matriz.append(['0']*(j+2))
    return matriz

def entrada():
    e = input().split()
    nLi = int(e[0])
    nCo = int(e[1])

    ma = matriz(nLi,nCo)
    #debug_ma(ma)

    for i in range(1, nLi+1):
        ent = input()
        for j in range(1, nCo+1):
            ma[i][j] = ent[j-1]

    return ma, nLi, nCo

def busca(ma,i,j):
    value = ma[i][j]
    global nOvelhas, nLobos, val
    if value is '0':
        return False
    elif value is '#':
        return False
    elif value is 't':
        return False
    elif value is 'k':
        #variavel global de ovelha +=1

        nOvelhas += 1
        ma[i][j] = 't'

        val+=1
    elif value is 'v':
        #variavel global de lobo +=1

        nLobos += 1
        ma[i][j] = 't'

        val+=1
    ma[i][j] = 't'

    busca(ma,i,j+1)#olha a frente
    busca(ma,i,j-1)#olha a traz
    busca(ma,i-1,j)#olha em cima
    busca(ma,i+1,j)#olha em baixo

#programa
#nOvelhas = 0
#nLobos = 0
'''
 se em um determinado pasto houver mais ovelhas do que lobos, as
ovelhas sobrevivem e matam todos os lobos naquele pasto. Caso contrário, as
ovelhas daquele pasto são comidas pelos lobos, que sobrevivem. Note que caso
um pasto possua o mesmo número de lobos e ovelhas, somente os lobos
sobreviverão, já que lobos são predadores naturais, ao contrário de ovelhas
'''
ma, nLi, nCo = entrada()
nO = 0
nL = 0
for i in range(1,nLi+1):
    for j in range(1,nCo+1):
        if ma[i][j] != '#' and ma[i][j] != 't':
            nOvelhas = 0
            nLobos = 0
            val = 0
            busca(ma,i,j)
            if val > 0:
                #print('round')
                #print(nOvelhas, nLobos)
                if nOvelhas > nLobos:
                    nO += nOvelhas
                elif nLobos > nOvelhas:
                    nL += nLobos
                else:
                    nL += nLobos

    #print(nO, nL)

print(nO, nL)
#debug_ma(ma)
