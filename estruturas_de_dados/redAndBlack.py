class noneNode():
    def __init__(self):
        self._color = 'black'
        self._key = None

class Node():
    def __init__(self, key, data=None):
        self._key = key
        self._data = data
        self._father = None
        self._left = None
        self._right = None

    def __str__(self):
        return str(self._key)

    def __repr__(self):
        return str(self._key)
    
    def getData(self):
        return self._data

    def getFather(self):
        return self._father

    def getKey(self):
        return self._key   

    def getLeft(self):
        return self._left

    def getRight(self):
        return self._right

    def setData(self, value):
        self._data = value

    def setFather(self, value):
        self._father = value

    def setKey(self, value):
        self._key = value
  
    def setLeft(self, value):
        self._left = value
    
    def setRight(self, value):
        self._right = value

class Tree(Node):

    def __init__(self):
        self._root = None
        self._view = ''
        self._maior = 0
        self._x = 0

    def __repr__(self):
        return 'raiz:', self._root
    
    def add(self, key, data=None):
        node = Node(key, data)
        y = None
        x = self._root
        while x != None:
            y = x
            if node.getKey() < x.getKey():
                x = x.getLeft()
            else:
                x = x.getRight()
        node.setFather(y)
        if y == None:
            self._root = node
        elif node.getKey() < y.getKey():
            y.setLeft(node)
        else:
            y.setRight(node)
    
    def delete(self, value):
        z = self.search(value)
        if z != None:
            if z.getLeft() == None or z.getRight() == None:
                y = z
            else:
                y = self.successor(z)
            if y.getLeft() != None:
                x = y.getLeft()
            else:
                x = y.getRight()
            if x != None:
                x.setFather(y.getFather())
            if y.getFather() == None:
                self._root = x
            else:
                if y == y.getFather().getLeft():
                    y.getFather().setLeft(x)
                else:
                    y.getFather().setRight(x)
            if y != z:
                z.setKey(y.getKey())
            return y

    def maximum(self, node):
        while node.getRight() != None:
            node = node.getRight()
        return node

    def minimum(self, node):
        while node.getLeft() != None:
            node = node.getLeft()
        return node
    
    def leftRotate(self, x):
        y = x.getRight()
        x.setRight(y.getLeft())
        if y.getLeft() != None:
            y.getFather().setLeft(x)
        y.setFather(x.getFather())
        if x.getFather() == None:
            self._root = y
        elif x == x.getFather().getLeft():
            x.getFather().setLeft(y)
        else:
            x.getFather().setRight(y)
        y.setLeft(x)
        x.setFather(y)
    
    def rightRotate(self, x):
        y = x.getLeft()
        x.setLeft(y.getRight())
        if y.getRight() != None:
            y.getFather().setRight(x)
        y.setFather(x.getFather())
        if x.getFather() == None:
            self._root = y
        elif x == x.getFather().getRight():
            x.getFather().setRight(y)
        else:
            x.getFather().setLeft(y)
        y.setRight(x)
        x.setFather(y)

    def search(self, value):
        node = self._root
        while node != None and value != node.getKey():
            if value < node.getKey():
                node = node.getLeft()
            else:
                node = node.getRight()
        return node

    def successor(self, node):
        if node.getRight() != None:
            return self.minimum(node.getRight())
        y = node.getFather()
        while y != None and node == y.getRight():
            node = y
            y = node.getFather()
        return y
    
    #views
    def inOrderPrint(self):
        if self._root is not None:
            raiz = self._root
            self.inOrder(raiz)
            out = self._view
            self._view = ''
            return out
        else:
            return '0 '

    def inOrder(self, node):
        if node != None:
            self.inOrder(node.getLeft())
            self._view += str(node) + ' '
            self.inOrder(node.getRight()) 

    def inPreOrderPrint(self):
        if self._root is not None:
            raiz = self._root
            self.inPreOrder(raiz)
            out = self._view
            self._view = ''
            return out
        else:
            return '0 '

    def inPreOrder(self, node):
        if node != None:
            self._view += str(node) + ' '
            self.inPreOrder(node.getLeft())           
            self.inPreOrder(node.getRight()) 

    def inPostOrderPrint(self):
        if self._root is not None:
            raiz = self._root
            self.inPostOrder(raiz)
            out = self._view
            self._view = ''
            return out
        else: 
            return '0 '

    def inPostOrder(self, node):
        if node != None:            
            self.inPostOrder(node.getLeft())           
            self.inPostOrder(node.getRight()) 
            self._view += str(node) + ' '

    def greaterLess(self, value):
        node = self._root
        self._x = value
        self.inorderTreeWalk2(node)
        out = self._maior
        self._maior = 0
        self._x = 0 
        return out

    def inorderTreeWalk2(self, node):
        if node != None:
            self.inorderTreeWalk2(node.getLeft())
            if node.getKey() > self._maior and node.getKey() < self._x:
                self._maior = node.getKey()
            self.inorderTreeWalk2(node.getRight())

#--------------------------------------------------------------------

t = Tree()
t.add(2)
t.add(1)
t.add(4)
t.add(3)
t.add(5)
print(t.inPreOrderPrint())
r = t.search(4)
t.leftRotate(r)
print(t.inPreOrderPrint())
r = t.search(5)
t.rightRotate(r)
print(t.inPreOrderPrint())