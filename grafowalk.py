inf = float("inf")

class Heap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def heapify(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1

class Node():
    def __init__(self):
        self.distance = inf
        self.caminho = 0
        self.adjacente = {} # { vertice: distancia }
    
    def __str__(self):
        return 'd: ' + str(self.distance) + ' ' + 'c: ' + str(self.caminho)
    
    def __repr__(self):
        return 'dist: ' + str(self.distance) + ' ' + 'caminho: ' + str(self.caminho) + '\n'
    

    def addDistance(self, v, w):
        self.adjacente[v] = w

class grafoWalk():
    def __init__(self, vertices):
        self.heap = Heap()
        self.vertices = [Node() for i in range(vertices)]
        self.Q = [i for i in range(vertices)]
    
    def start(self):
        self.heap.heapify(self.Q)
        self.vertices[0].distance = 0
        self.vertices[0].caminho = -1
        #print(self.heap.heapList)
        while self.heap.currentSize > 0:
            u = self.heap.delMin()
            for v in self.vertices[u].adjacente:
                if self.vertices[v].distance > self.vertices[u].distance:
                    self.vertices[v].distance = self.vertices[u].distance + self.vertices[u].adjacente[v]
                    self.vertices[v].caminho += u

    def addDistance(self, u, v, w):
        self.vertices[u].addDistance(v, w)


'''
enquanto Q ≠ ø
         u ← extrair-mín(Q)                     //Q ← Q - {u}
         para cada v adjacente a u
              se d[v] > d[u] + w(u, v)          //relaxe (u, v)
                 então d[v] ← d[u] + w(u, v)
                       π[v] ← u
'''


inpt = input().split()
vertices = int(inpt[0])
voo = int(inpt[1])
x = grafoWalk(vertices)
for i in range(voo):
    comando = input().split()
    x.addDistance(int(comando[0]), int(comando[1]), int(comando[2]))

x.start()

print(x.vertices)

# bh = Heap()
# bh.heapify([9,5,6,2,3])



# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.currentSize)

