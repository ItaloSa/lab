class TreeNode():
    def __init__(self,dado):
        self.__dado = dado
        self.__left = None
        self.__right = None
        self.__pai = None
        
    def getDado(self):
        return self.__dado
    def setDado(self,novodado):
        self.__dado = novodado
    
    def getFilhoEsquerdo(self):
        return self.__left
    def setFilhoEsquerdo(self,novoFilho):
        self.__left = novoFilho
    
    def getFilhoDireito(self):
        return self.__right
    def setFilhoDireito(self,Novofilho):
        self.__right = Novofilho
    
    def getPai(self):
        return self.__pai
    def setPai(self,novoPai):
        self.__pai = novoPai
    
class AVLTree():
    def __init__(self):
        self.__none = TreeNode(None)
        self.__none.setFilhoDireito(self.__none)
        self.__none.setFilhoEsquerdo(self.__none)
        self.__none.setPai(self.__none)
        self.__raiz = self.__none
        
    def getNone(self):
        return self.__none
    
    def getRaiz(self):
        return self.__raiz
    def setRaiz(self,novaRaiz):
        self.__raiz = novaRaiz
        
   
    def Tree_search(self,x,valor):
        while x != None and valor != x.getDado():
            if valor < x.getDado():
                x = x.getFilhoEsquerdo()
            else:
                x = x.getFilhoDireito()
        return x
    
    def inorder_Tree_Walk(self,x):
        if x != self.__none:
            self.inorder_Tree_Walk(x.getFilhoEsquerdo())
            print(x.getDado(),self.BalanceVerify(x))
            self.inorder_Tree_Walk(x.getFilhoDireito())
    def posorder_tree_walk(self,x):
        if x != None:
            self.posorder_tree_walk(x.getFilhoEsquerdo())
            self.posorder_tree_walk(x.getFilhoDireito())
            print(x.getDado())
    def preorder_tree_Walk(self,x):
        if x != None:
            print(x.getDado())
            self.preorder_tree_Walk(x.getFilhoEsquerdo())
            self.preorder_tree_Walk(x.getFilhoDireito())

    def recursive_tree_search(self,x,value):
        if x == self.__none or value == x.getDado():
            return x        
        if value < x.getDado():
            return self.recursive_tree_search(x.getFilhoEsquerdo(), value)
        else:
            return self.recursive_tree_search(x.getFilhoDireito(), value)
        

    def tree_Minimum(self,nodo):
        while nodo.getFilhoEsquerdo() != None:
            nodo = nodo.getFilhoEsquerdo()
        return nodo
    
    def tree_Maximum(self,nodo):
        while nodo.getFilhoDireito() != None:
            nodo = nodo.getFilhoDireito()
        return nodo
    
    def tree_Sucessor(self,nodo):
        if nodo.getFilhoDireito()!= None:
            return self.tree_Minimum(nodo.getFilhoDireito())
        y = nodo.getPai()
        while y != None and nodo == y.getFilhoDireito():
            nodo = y
            y = y.getPai()
        return y
    
    def tree_Predecessor(self,nodo):
        if nodo.getFilhoEsquerdo()!= None:
            return self.tree_Maximum(nodo.getFilhoEsquerdo())
        y = nodo.getPai()
        while y != None and nodo == y.getFilhoEsquerdo():
            nodo = y
            y = y.getPai()
        return y
            
           
    def tree_insert(self,z):
        y = self.__none
        x = self.getRaiz()
        while x != self.__none:
            y = x
            if z.getDado()< x.getDado():
                x = x.getFilhoEsquerdo()
            else:
                x = x.getFilhoDireito()
        z.setPai(y)
        if y == self.__none:
            self.setRaiz(z)
        elif z.getDado() < y.getDado():
            y.setFilhoEsquerdo(z)
        else:
            y.setFilhoDireito(z)
        z.setFilhoDireito(self.__none)
        z.setFilhoEsquerdo(self.__none)
        self.Balance(z)
            
                
    def transplant(self,u,v):
        if u.getPai() == self.__none:
            self.setRaiz(v)
        elif u == u.getPai().getFilhoEsquerdo():
            u.getPai().setFilhoEsquerdo(v)
        else:
            u.getPai().setFilhoDireito(v)
        if v != self.__none:
            v.setPai(u.getPai())
    def deletar(self,z):
        if z.getFilhoEsquerdo() == self.__none:
            self.transplant(z, z.getFilhoDireito())
        elif z.getFilhoDireito() == self.__none:
            self.transplant(z, z.getFilhoEsquerdo())
        else:
            y = self.tree_Minimum(z.getFilhoDireito())
            if y.getPai() != z:
                self.transplant(y, y.getFilhoDireito())
                y.setFilhoDireito(z.getFilhoDireito())
                y.getFilhoDireito().setPai(y)
            self.transplant(z, y)
            y.setFilhoEsquerdo(z.getFilhoEsquerdo())
            y.getFilhoEsquerdo().setPai(y)
    
    def rightRotate(self,nodo):
        y = nodo.getFilhoEsquerdo()
        nodo.setFilhoEsquerdo(y.getFilhoDireito())
        if y.getFilhoDireito() != self.__none:
            y.getFilhoDireito().setPai(nodo)
        y.setPai(nodo.getPai())
        if nodo.getPai() == self.__none:
            self.setRaiz(y)
        elif nodo == nodo.getPai().getFilhoDireito():
            nodo.getPai().setFilhoDireito(y)
        else:
            nodo.getPai().setFilhoEsquerdo(y)
        y.setFilhoDireito(nodo)
        nodo.setPai(y)
        
    def leftRotate(self,nodo):
        y = nodo.getFilhoDireito()
        nodo.setFilhoDireito(y.getFilhoEsquerdo())
        if y.getFilhoEsquerdo()!= self.__none:
            y.getFilhoEsquerdo().setPai(nodo)
        y.setPai(nodo.getPai())
        if nodo.getPai() == self.__none:
            self.setRaiz(y)
        elif nodo == nodo.getPai().getFilhoEsquerdo():
            nodo.getPai().setFilhoEsquerdo(y)
        else:
            nodo.getPai().setFilhoDireito(y)
        y.setFilhoEsquerdo(nodo)
        nodo.setPai(y)
        
  
    def altura(self,nodo):
        if nodo == self.__none:
            return -1
        h1 = self.altura(nodo.getFilhoEsquerdo())
        h2 = self.altura(nodo.getFilhoDireito())
        return 1+max(h1,h2)
    
    def BalanceVerify(self,nodo):
        Right= self.altura(nodo.getFilhoDireito())
        Left = self.altura(nodo.getFilhoEsquerdo())
        return Left - Right 
    
       
    def Balance(self,nodo):
        while nodo.getPai() != self.__none:
            if self.BalanceVerify(nodo.getPai()) == 2 and self.BalanceVerify(nodo) == 1:#reta direita
                self.rightRotate(nodo.getPai())
            if self.BalanceVerify(nodo.getPai()) == -2 and self.BalanceVerify(nodo) == -1:#reta esquerda
                self.leftRotate(nodo.getPai())
            if self.BalanceVerify(nodo.getPai()) == 2 and self.BalanceVerify(nodo) == -1: #joelho direito
                self.leftRotate(nodo)
                self.rightRotate(nodo.getPai().getPai())
            if self.BalanceVerify(nodo.getPai()) == -2 and self.BalanceVerify(nodo) == 1:# joelho esquerdo
                self.rightRotate(nodo)
                self.leftRotate(nodo.getPai().getPai())
            nodo = nodo.getPai()
        
                       
    def nivel(self,nodo):
        if nodo == self.__raiz:
            nivel = 1
        else:            
            nivel = self.nivel(nodo.getPai()) + 1
        return nivel
    

            
        
    