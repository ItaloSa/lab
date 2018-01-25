class Node():
    def __init__(self, key):
        self._key = key
        self._father = None
        self._right = None        
        self._left = None

    def getKey(self):
        return self._key

    def setKey(self, value):
        self._key = value

    def getRight(self):
        return self._right

    def setRight(self, value):
        self._right = value

    def getLeft(self):
        return self._left

    def setLeft(self, value):
        self._left = value

    def getFather(self):
        return self._father

    def setFather(self, value):
        self._father = value

class Tree():
    def __init__(self):
        self._none = Node(None)
        self._none.setFather(self.getTreeNone())
        self._none.setLeft(self.getTreeNone())
        self._none.setRight(self.getTreeNone())        
        self._root = self.getTreeNone()

    def getTreeNone(self):
        return self._none

    def setTreeNone(self, valor):
        self._none = valor

    def getRoot(self):
        return self._root

    def setRoot(self, valor):
        self._root = valor

    def srch(self, key):
        node = self.getRoot()
        while node != self.getTreeNone() and key != node.getKey():
            if key < node.getKey():
                node = node.getLeft()
            else:
                node = node.getRight()
        return node

    def height(self, node):
        if node == self.getTreeNone():
            return -1
        h1 = self.height(node.getLeft())
        h2 = self.height(node.getRight())
        return (1 + max(h1, h2))    

    def treeBalanceVerify(self, no):
        return self.height(no.getLeft()) - self.height(no.getRight())

    def treeBalance(self, nodo):
        while nodo.getFather() != self.getTreeNone():
            if self.treeBalanceVerify(nodo.getFather()) == 2 and self.treeBalanceVerify(nodo) == 1:
                self.rightRotate(nodo.getFather())

            if self.treeBalanceVerify(nodo.getFather()) == 2 and self.treeBalanceVerify(nodo) == -1:
                self.leftRotate(nodo)
                self.rightRotate(nodo.getFather().getFather())

            if self.treeBalanceVerify(nodo.getFather()) == -2 and self.treeBalanceVerify(nodo) == -1:
                self.leftRotate(nodo.getFather())
                
            if self.treeBalanceVerify(nodo.getFather()) == -2 and self.treeBalanceVerify(nodo) == 1:
                self.rightRotate(nodo)
                self.leftRotate(nodo.getFather().getFather())

            nodo = nodo.getFather()

    def leftRotate(self, node):
        y = node.getRight()
        node.setRight(y.getLeft())  
        if y.getLeft() != self.getTreeNone():
            y.getLeft().setFather(node)
        y.setFather(node.getFather())
        if node.getFather() == self.getTreeNone(): 
            y.getLeft().setFather(node)
        y.setFather(node.getFather())  
        if node.getFather() == self.getTreeNone():
            self.setRoot(y)
        elif node == node.getFather().getLeft():
            node.getFather().setLeft(y)
        else:
            node.getFather().setRight(y)
        y.setLeft(node) 
        node.setFather(y)

    def rightRotate(self, x):
        y = x.getLeft()
        x.setLeft(y.getRight())
        y.getRight().setFather(x)
        y.setFather(x.getFather())
        if x.getFather() == self.getTreeNone():
            y.getRight().setFather(x)
        y.setFather(x.getFather())
        if x.getFather() == self.getTreeNone():
            self.setRoot(y)
        elif x == x.getFather().getRight():
            x.getFather().setRight(y)
        else:
            x.getFather().setLeft(y)
        y.setRight(x)
        x.setFather(y)

    def add(self, key):
        novo = Node(key)
        y = self.getTreeNone()
        x = self.getRoot()
        while x != self.getTreeNone():
            y = x
            if novo.getKey() < x.getKey():
                x = x.getLeft()
            else:
                x = x.getRight()
        novo.setFather(y)
        if y == self.getTreeNone():
            self.setRoot(novo)
        elif novo.getKey() < y.getKey():
            y.setLeft(novo)
        else:
            y.setRight(novo)
        novo.setRight(self.getTreeNone())
        novo.setLeft(self.getTreeNone())
        self.treeBalance(novo)

    def nodeLevel(self, nodo):
        if nodo == self.getTreeNone():
            return -1
        else:
            x = nodo
            nivel = 1
            while x != self.getRoot():
                x = x.getFather()
                nivel += 1
            return nivel
        
    def inOrder(self, x, li, init, end):
        if x != self.getTreeNone():
            self.inOrder(x.getLeft(), li, init, end)
            if x.getKey() >= init and x.getKey() <= end:
                li.append(x.getKey())
            self.inOrder(x.getRight(), li, init, end)

def lopt(t, inpt):
    init = int(inpt[1])
    end = int(inpt[2])
    li = []
    t.inOrder(t.getRoot(), li, init, end)
    if len(li) > 0:
        out = ''
        for i in li:
            out += str(i) + ' '
        print(out)
    else:
        print('-1')

def  boot():
    genres = int(input())
    for i in range(genres):
        if i > 0:
            print('')
        t = Tree()
        while True:
            inpt = input()
            inpt = inpt.split()
            if inpt[0] is 'F':
                break
            if inpt[0] == 'I':
                t.add(int(inpt[1]))
            if inpt[0] == 'N':
                nodo = t.srch(int(inpt[1]))
                print(t.nodeLevel(nodo))
            if inpt[0] == 'L':
                lopt(t, inpt)

boot()