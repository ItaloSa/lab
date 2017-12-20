# inicio debug ---------------------------------
def debug_ma(ma):
    for li in ma:
        print(li)
#fim debug -------------------------------------

#passo 1 - montar a matriz ~ ok
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
#    debug_ma(ma)

    for i in range(1, nLi+1):
        ent = input()
        for j in range(1, nCo+1):
            ma[i][j] = ent[j-1]

    return ma, nLi, nCo

#passo 2 - fazer as jogadas
def jogadas(matriz):
    numJgds = int(input())
    for n in range(numJgds):
        jogada = input().split()
        i,j = int(jogada[0]), int(jogada[1])
        if matriz[i][j] == '#':
            matriz[i][j] = 'd'

#passo 3 - pesquisar os destruidos
def busca(ma,i,j):
    value = ma[i][j]
    global tam_na, tam_dest, val
    if value is '0': #limite
        return False
    elif value is 'v': #visitado
        return False
    elif value is '.': #agua
        return False
    elif value is '#': #navio

        tam_na += 1
        ma[i][j] = 'v' #visitado

        val+=1
    elif value is 'd': #destruido
        
        tam_na += 1
        tam_dest += 1
        ma[i][j] = 'v' #visitado

        val+=1

    ma[i][j] = 'v' #visitado

    busca(ma,i,j+1)#olha a frente
    busca(ma,i,j-1)#olha a traz
    busca(ma,i-1,j)#olha em cima
    busca(ma,i+1,j)#olha em baixo
    
#debug
#ma, nLi, nCo = entrada()
#debug_ma(ma)
ma, nLi, nCo = entrada()
jogadas(ma) #realizando as jogadas
#print('---')
dest = 0
for i in range(1,nLi+1):
    for j in range(1,nCo+1):
        if ma[i][j] != '.' and ma[i][j] != 'v':
            tam_dest = 0
            tam_na = 0
            val = 0
            busca(ma,i,j)
#           print(tam_dest, tam_na)
            if val > 0:    
                if tam_na - tam_dest == 0:
                    dest += 1
print(dest)