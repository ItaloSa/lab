class Nil():
    def __init__(self):
        self._color = 'black'
        self._key = None
        self._father = self
        self._left = self
        self._right = self
    
    def __repr__(self):
        return 'None'

    def __str__(self):
        return 'None'
    
    def getColor(self):
        return self._color

    def getFather(self):
        return self._father

    def getLeft(self):
        return self._left

    def getRight(self):
        return self._right

    def setColor(self, value):
        self._color = value

    def setFather(self, value):
        self._father = value

    def setLeft(self, value):
        self._left = value
    
    def setRight(self, value):
        self._right = value

class Node():
    def __init__(self, treeNone, key, data=None):
        self._key = key
        self._data = data
        self._father = treeNone
        self._left = treeNone
        self._right = treeNone

    def __str__(self):
        return str(self._key)

    def __repr__(self):
        return str(self._key)
    
    def getColor(self):
        return self._color

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

    def setColor(self, value):
        self._color = value

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
        self._none = Nil()
        self._root = self._none
        self._view = ''
        self._maior = 0
        self._x = 0

    def __repr__(self):
        return 'Tree', self._root
    
    def __str__(self):
        return 'Tree', self._root
    
    def leftRotate(self, node):
        y = node.getRight()
        node.setRight(y.getLeft())
        if y.getLeft() != self._none:
            y.getFather().setLeft(node)
        y.setFather(node.getFather())
        if node.getFather() == self._none:
            self._root = y
        elif node == node.getFather().getLeft():
            node.getFather().setLeft(y)
        else:
            node.getFather().setRight(y)
        y.setLeft(node)
        node.setFather(y)

    def rightRotate(self, node):
        y = node.getLeft()
        node.setLeft(y.getRight())
        if y.getRight() != self._none:
            y.getFather().setRight(node)
        y.setFather(node.getFather())
        if node.getFather() == self._none:
            self._root = y
        elif node == node.getFather().getRight():
            node.getFather().setRight(y)
        else:
            node.getFather().setLeft(y)
        y.setRight(node)
        node.setFather(y)
  
    def search(self, value):
        node = self._root
        while node != self._none and value != node.getKey():
            if value < node.getKey():
                node = node.getLeft()
            else:
                node = node.getRight()
        return node

    def maximum(self, node):
        while node.getRight() != self._none:
            node = node.getRight()
        return node

    def minimum(self, node):
        while node.getLeft() != self._none:
            node = node.getLeft()
        return node

    def successor(self, node):
        if node.getRight() != self._none:
            return self.minimum(node.getRight())
        y = node.getFather()
        while y != self._none and node == y.getRight():
            node = y
            y = node.getFather()
        return y

    def add(self, value):
        node = Node(self._none, value)
        y = self._none
        x = self._root
        while x is not self._none:
            y = x
            if node.getKey() < x.getKey():
                x = x.getLeft()
            else:
                x = x.getRight()
        node.setFather(y)
        if y is self._none:
            self._root = node
        elif node.getKey() < y.getKey():
            y.setLeft(node)
        else:
            y.setRight(node)
        node.setLeft(self._none)
        node.setRight(self._none)
        self.treeBalance(node)

    def height(self, node):
        if node is self._none:
            return -1
        else:
            leftHeight = self.height(node.getLeft())
            rightHeight = self.height(node.getRight())
            return 1+max(rightHeight, leftHeight)

    def balanceVerify(self, node):
        leftHeight = self.height(node.getLeft())
        rightHeight = self.height(node.getRight())
        return  leftHeight - rightHeight

    def treeBalance(self, node):
        while node.getFather() is not self._none:
            if self.balanceVerify(node.getFather()) == 2 and self.balanceVerify(node) == 1:
                self.rightRotate(node.getFather())
            if self.balanceVerify(node.getFather()) == -2 and self.balanceVerify(node) == -1:
                self.leftRotate(node.getFather())
            if self.balanceVerify(node.getFather()) == 2 and self.balanceVerify(node) == -1:
                self.leftRotate(node)
                self.rightRotate(node.getFather().getFather())
            if self.balanceVerify(node.getFather()) == -2 and self.balanceVerify(node) == 1:
                self.rightRotate(node)
                self.leftRotate(node.getFather().getFather())
            node = node.getFather()

    def nodeLevel(self, value):
        node = self.search(value)
        level = 1
        if node is self._none:
            return -1
        elif node is self._root:
            return 1
        else:
            while node is not self._root:
                node = node.getFather()
                level += 1
            return level

    #views
    def inOrderPrint(self, v1, v2):
        if self._root is not self._none:
            rainode = self._root
            self.inOrder(rainode, v1,v2)
            out = self._view
            self._view = ''
            return out
        else:
            return '0 '

    def inOrder(self, node, v1, v2):
        if node != self._none:
            self.inOrder(node.getLeft(), v1, v2)
            if node.getKey() >= v1 and node.getKey() <= v2:
                self._view += str(node) + ' '
            self.inOrder(node.getRight(), v1, v2)   
    
# t = Tree()
# t.add(5)
# t.add(6)
# t.add(3)
# t.add(7)
# t.add(4)
# t.add(2)
# t.add(9)
# t.add(8)

# x = t.search(10)
# lv = t.nodeLevel(5)
# print(t.inOrderPrint(1, 8))

def programa():
    genres = int(input())
    for i in range(genres):
        tree = Tree()
        while True:
            inpt = input().split()
            command = inpt[0]
            if command is 'I':
                tree.add(inpt[1])
            elif command is 'N':
                print(tree.nodeLevel(inpt[1]))
            elif command is 'L':
                print(tree.inOrderPrint(inpt[1], inpt[2]))
            elif command is 'F':
                if i is not genres-1:
                    print('')
                break

p = programa()