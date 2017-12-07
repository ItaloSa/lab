class Node():
    def __init__(self, data, father=None, left=None, right=None):
        self._data = data
        self._father = father
        self._left = left
        self._right = right

    def __str__(self):
        return str(self.__value)

    def getData(self):
        return self._data
    
    def setData(self, value):
        self._data = value

    def getFather(self):
        return self._father
    
    def setFather(self, value):
        self._father = value

    def getLeft(self):
        return self._left
    
    def setLeft(self, value):
        self._left = value

    def getRight(self):
        return self._right
    
    def setRight(self, value):
        self._right = value

class Tree(Node):
    def __init__(self)
        self._root = None
    
    def isRoot(self, p):
        return self.getFather(p) is None

    def isEmpty(self):
        return self._root is None

    def isLeft(self, p):
        q = self.getFather(p)
        if q == None:
            return False
        elif self.getLeft(q) == p:
            return True
        else:
            return False
    
    def isRight(self, p):
        q = self.getFather(p)
        if q == None:
            return False
        elif self.getRight(q) == p:
            return True
        else:
            return False
    
    def getBrother(self, p):
        if self.isRoot(p):
            return False
        elif self.isLeft(p):
            return self.getRight(getFather(p))
        else:
            return self.getLeft(getFather(p))

    def addRoot(self, value):        
        self._root = Node(value)

    def addLeft(self, value):
        if self.isEmpty():
            self.addRoot(value)
        else:            
            node = self._root
            while node.getLeft() is not None:
                node = node.getLeft()
            node.setLeft(Node(value))
    
    def addRight(self, value):
        if self.isEmpty():
            self.addRoot(value)
        else:            
            node = self._root
            while node.getRight() is not None:
                node = node.getRight()
            node.setRight(Node(value))

