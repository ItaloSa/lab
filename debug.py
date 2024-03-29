class Node():
    def __init__(self, data):
        self._data = data
        self._father = None
        self._left = None
        self._right = None

    def __str__(self):
        return  str(self._data) + ' '

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
        self._maior = 0
        self._x = 0
        self._inTree = 0
        self._inTreeCount = 0
    
    def __str__ (self):
        self.view(self._root)
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
        if self.inTree(value):
            node = self.treeSearch(value, self._root)
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
        

    def view(self, node):
        if node != None:
            self.view(node.getLeft())
            self._view += str(node)
            self.view(node.getRight())

    def inorderTreeWalk2(self, node):
        if node != None:
            self.inorderTreeWalk2(node.getLeft())
            if node.getData() > self._maior and node.getData() < self._x:
                self._maior = node.getData()
            self.inorderTreeWalk2(node.getRight())

    #prints -----
    def inOrderPrint(self):
        if self.isEmpty():
            return str('0 ')
        else:
            self.inOrder(self._root)
            out = self._view
            self._view = ''
            return out

    def inOrder(self, node):
        if node != None:
            self.inOrder(node.getLeft())
            self._view += str(node)
            self.inOrder(node.getRight())
   
    def inPreOrderPrint(self):
        if self.isEmpty():
            return str('0 ')
        else:
            self.inPreOrder(self._root)
            out = self._view
            self._view = ''
            return out

    def inPreOrder(self, node):
        if node != None:
            self._view += str(node)
            self.inPreOrder(node.getLeft())            
            self.inPreOrder(node.getRight())
    
    def inPostOrderPrint(self):
        if self.isEmpty():
            return str('0 ')
        else:
            self.inPostOrder(self._root)
            out = self._view
            self._view = ''
            return out

    def inPostOrder(self, node):
        if node != None:
            self.inPostOrder(node.getLeft())            
            self.inPostOrder(node.getRight())
            self._view += str(node)
    #prints -----

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

    def greaterLess(self, value):
        node = self._root
        self._x = value
        self.inorderTreeWalk2(node)
        out = self._maior
        self._maior = 0
        self._x = 0 
        return out

    def inTree(self, value):
        self._inTree = value
        self.walkOnTree(self._root)
        if self._inTreeCount > 0:
            self._inTree = 0
            self._inTreeCount = 0
            return True
        else:
            self._inTree = 0
            self._inTreeCount = 0
            return False

    def walkOnTree(self, node):
        if node != None:
            if node.getData() == self._inTree:
                self._inTreeCount += 1
            self.walkOnTree(node.getLeft())            
            self.walkOnTree(node.getRight())

tree = Tree()   

tree.addNode(6382)
tree.addNode(849)
tree.addNode(5996)
tree.addNode(1365)
tree.addNode(6887)
tree.addNode(3142)
tree.addNode(2822)
tree.addNode(8536)
tree.addNode(5732)
tree.addNode(6607)
tree.addNode(3381)
tree.addNode(3925)
tree.addNode(5524)
tree.addNode(3665)
tree.addNode(3598)
tree.addNode(9217)
tree.addNode(4720)
r = tree.treeSearch(6382)
print(r.getFather())
tree.addNode(8693)
tree.addNode(1903)
tree.addNode(1316)
tree.addNode(8905)
tree.addNode(5987)
tree.addNode(1124)
tree.addNode(7842)
tree.addNode(3582)
tree.deleteNode(6382)
tree.deleteNode(1903)
tree.addNode(5348)
tree.deleteNode(5105)
tree.addNode(5059)
tree.addNode(7556)
tree.addNode(3345)
tree.deleteNode(1883)
tree.deleteNode(5824)
tree.addNode(311)
tree.addNode(8925)
tree.addNode(1956)
tree.deleteNode(3925)
tree.deleteNode(5996)
tree.deleteNode(1903)
tree.addNode(6314)
tree.addNode(3357)
tree.addNode(4273)
#tree.deleteNode(4720)
#tree.deleteNode(1429)



print(tree)