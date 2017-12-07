class Node():
    def __init__(self, value, ponteiro=None):
        self.__value = value
        self.__ponteiro = ponteiro

    def __str__(self):
        return str(self.__value)

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def get_ponteiro(self):
        return self.__ponteiro

    def set_ponteiro(self, value):
        self.__ponteiro = value

class Lista():
    def __init__(self):
        self.__inicio = None
        self.__fim = None

    def __str__(self):
        if self.lista_esta_vazia():
            return ''
        node_atual = self.__inicio
        string = ''
        while node_atual is not None:
            string += str(node_atual.get_value())
            node_atual = node_atual.get_ponteiro()
        return string

    def lista_esta_vazia(self):
        return self.__inicio is None

    def add_no_fim(self, value):
        novo_node = Node(value)
        if self.lista_esta_vazia():
            self.__inicio = self.__fim = novo_node
        else:
            self.__fim.set_ponteiro(novo_node)
            self.__fim = novo_node

    def add_no_inicio(self, value):
        novo_node = Node(value)
        if self.lista_esta_vazia():
            self.__inicio = self.__fim = novo_node
        else:
            novo_node.set_ponteiro(self.__inicio)
            self.__inicio = novo_node

    def remove_do_inicio(self):
        if self.lista_esta_vazia():
            return 'Remocao de Lista vazia nao permitida'
        valor_primeiro_node = self.__inicio.get_value()
        if self.__inicio is self.__fim:
            self.__inicio = self.__fim = None
        else:
            self.__inicio = self.__inicio.get_ponteiro()
        return valor_primeiro_node

    def remove_do_fim(self):
        if self.lista_esta_vazia():
            return 'Remocao de Lista vazia nao permitida'
        valor_ultimo_node = self.__fim.get_value()
        if self.__inicio is self.__fim:
            self.__inicio = self.__fim = None
        else:
            node_atual = self.__inicio
            while node_atual is not self.__fim:
                node_atual = node_atual.get_ponteiro()
            node_atual.set_ponteiro(None)
            self.__fim = node_atual
        return valor_ultimo_node

    def get_inicio(self):
        return self.__inicio

    def get_fim(self):
        return self.__fim

    def set_inicio(self, value):
        self.__inicio = value

    def set_fim(self, value):
        self.__fim = value

class Pilha(Lista):

    def colocar_na_pilha(self, value):
        self.add_no_inicio(value)

    def tirar_da_pilha(self):
        return self.remove_do_inicio()

def fib(n):
    if n == 1 or n == 2:
        return 1
    fib = 2
    pilha = Pilha()
    #pilha inicia com [1, 1]
    pilha.colocar_na_pilha(1)
    pilha.colocar_na_pilha(1)
    while fib != n:
        u = pilha.tirar_da_pilha()
        p = pilha.tirar_da_pilha()
        r = p + u
        pilha.colocar_na_pilha(p)
        pilha.colocar_na_pilha(u)
        pilha.colocar_na_pilha(r)
        fib += 1
    return pilha.tirar_da_pilha()

print(fib(3))
