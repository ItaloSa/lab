#CamelCase code

class Node():
    def __init__(self, data):
        self._data = data
        self._father = None
        self._left = None
        self._right = None

    def __str__(self):
        return '<' + str(self._data) + '>'

    def getData(self):
        return self._data

    def getFather(self):
        return self._father

    def getLeft(self):
        return self._left

    def getRight(self):
        return self._right

    def setData(self, value):
        self._data = value

    def setFather(self, value):
        self._father = value
    
    def setLeft(self, value):
        self._left = value
    
    def setRight(self, value):
        self._right = value

class Tree(Node):
    def __init__(self):
        self._root = None
        self._view = ''   
    
    def __str__ (self):
        self.inorderTreeWalk(self._root)
        out = self._view
        self._view = ''
        return out
    
    def addNode(self, value):
        node = Node(value)
        y = None
        x = self._root
        while x != None:
            y = x
            if node.getData() < x.getData():
                x = x.getLeft()
            else:
                x = x.getRight()
        node.setFather(y)
        if y == None:
            self._root = node
        elif node.getData() < y.getData():
            y.setLeft(node)
        else:
            y.setRight(node)
    
    def deleteNode(self, value):
        node = self.treeSearch(value)
        if node.getLeft() == None or node.getRight() == None:
            y = node
        else:
            y = self.treeSucessor(node)
        
        if y.getLeft() != None:
            x = y.getLeft()
        else:
            x = y.getRight()
        
        if x != None:
            x.setFather(y.getFather())
        
        if y.getFather() == None:
            self._root = x
        elif y == y.getFather().getLeft():
            y.getFather().setLeft(x)
        else:
            y.getFather().setRight(x)
        
        if y != node:
            node.setData(y.getData())
        
        return y

    def inorderTreeWalk(self, node):
        if node != None:
            self.inorderTreeWalk(node.getLeft())
            self._view += str(node)
            self.inorderTreeWalk(node.getRight())

    def isRoot(self, node):
        return node == self._root

    def isEmpty(self):
        return self._root is None
    
    def treeMaximum(self, node):
        while node.getLeft() != None:
            node = node.getLeft()
        return node

    def treeMinimum(self, node):
        while node.getRight() != None:
            node = node.getRight()
        return node
    
    def treeSearch(self, value, node=None):
        if node == None:
            node = self._root
        if value == None or value == node.getData():
            return node
        if value < node.getData():
            return self.treeSearch(value, node.getLeft())
        else:
            return self.treeSearch(value, node.getRight())
    
    def treeSucessor(self, node):
        if node.getRight() != None:
            return self.treeMinimum(node.getRight())
        y = node.getFather()
        while y != None and node == y.getRight():
            node = y
            y = y.getFather()
        return y
