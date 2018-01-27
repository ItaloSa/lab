class Heap:
    def __init__(self):
        self.heapList = []
        self.currentSize = 0

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i]['id'] > self.heapList[mc]['id']:
              tmp = self.heapList[i]['id']
              self.heapList[i]['id'] = self.heapList[mc]['id']
              self.heapList[mc]['id'] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2]['id'] < self.heapList[i*2+1]['id']:
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

x = [ {'id': 5}, {'id': 7}, {'id': 1}]
h = Heap()
h.heapify(x)
print(h.heapList)
h.delMin()
print(h.heapList)