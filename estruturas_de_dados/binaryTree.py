class Node():
    def __init__(self, data, father=None, left=None, right=None):
        self._data = data
        self._father = father
        self._left = left
        self._right = right

    def __str__(self):
        return str(self._data)

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

class binaryTree(Node):
    def __init__(self):
        self._root = None
        self._view = ''
    
    def __str__(self):
        node = self._root      
        self.inorderTreeWalk(node)
        out = self._view
        self._view = ''
        return out

    def inorderTreeWalk(self, node):
        global out        
        if node is not None:
            self.inorderTreeWalk(node.getLeft())
            self._view += str(node.getData()) + ' '
            self.inorderTreeWalk(node.getRight())

    def isRoot(self, p):
        return self.getFather(p) is None

    def isEmpty(self):
        return self._root is None

    def getFather(self, value):
        return value.getFather()

    def getLeft(self, value):
        return value.getLeft()

    def getRight(self, value):
        return value.getRight()

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

    def addRoot(self, value):        
        self._root = Node(value)

 #ops   
    def getBrother(self, p):
        if self.isRoot(p):
            return False
        elif self.isLeft(p):
            return self.getRight(self.getFather(p))
        else:
            return self.getLeft(self.getFather(p))
#end of ops

    def addNode(self, value):
        if self.isEmpty():
            self.addRoot(value)
        else: 
            node = self._root
            while True:
                if value > node.getData():                    
                    if node.getRight() is None:
                       node.setRight(Node(value))                       
                       break
                    else:
                        node = node.getRight()
                else:
                    if node.getLeft() is None:
                       node.setLeft(Node(value))                       
                       break
                    else:
                        node = node.getLeft()
    
    def treeSearch(self, value, node=None):
        if node is None:
            node = self._root
        while node != None and value != node.getData():
            if value < node.getData():
                node = node.getLeft()
            else:
                node = node.getRight()
        return node

    def treeMinimum(self, node):
        while node.getLeft() != None:
           node = node.getLeft() 
        return node

    def treeMaximum(self, node):
        while node.getRight() != None:
           node = node.getLeft() 
        return node

    def treeSuccessor(self, node):
        if node.getRight() != None:
            return self.treeMinimum(node.getRight())
        y = node.getFather()
        while y != None and node == y.getFather():
            node = y
            y = y.getFather()
        return y

    def treeDelete(self, value):
        y = None
        x = None
        node = self.treeSearch(value)
        if node.getLeft() == None or node.getRight() == None:
            y = node            
        else:
            y = self.treeSuccessor(node)     
        
        if y.getLeft() != None:
            x = y.getLeft()       
        else:
            x = y.getRight()
        
        if x != None:
            node.setFather(y.getFather())

        if y.getFather() == None:
            self._root = x
        else:
            if y == y.getFather().getLeft():
                y.getFather.setLeft(x)
            else:
                y.getFather.setRight(x)
       
        if y != node:
            node.setData(y.getData)
        
        return y


#teste
arvore = binaryTree()
arvore.addNode(1)
arvore.addNode(2)
arvore.addNode(3)

print(arvore)
arvore.treeDelete(3)
print(arvore)