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
        self.caminho = -1

class Dijkstra():
    def __init__(self, vertices):
        self.heap = Heap()
        self.vertices = [i for i in range(vertices)]
        self.weights = [{} for i in range(vertices)]
        self.nodes = [Node() for i in range(vertices)]

    def start(self):
        self.heap.heapify(self.vertices)
        while self.heap.currentSize is not 0:
            u = self.heap.delMin()
            for v in self.weights[u]:
                if self.nodes[v].distance > self.nodes[u].distance + self.weights[u][v]:
                    self.nodes[v].distance = self.nodes[u].distance + self.weights[u][v]
                self.nodes[v].caminho = u
    
    def addDistance(self, u, v, w):
        self.weights[u][v] = w

'''
enquanto Q ≠ ø
         u ← extrair-mín(Q)                     //Q ← Q - {u}
         para cada v adjacente a u
              se d[v] > d[u] + w(u, v)          //relaxe (u, v)
                 então d[v] ← d[u] + w(u, v)
                       π[v] ← u
'''

x = Dijkstra(3)
x.addDistance(0, 1, 2)
x.addDistance(0, 2, 4)
x.addDistance(1, 3, 1)
x.addDistance(2, 3, 5)

x.start()

# bh = Heap()
# bh.heapify([9,5,6,2,3])



# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.currentSize)

