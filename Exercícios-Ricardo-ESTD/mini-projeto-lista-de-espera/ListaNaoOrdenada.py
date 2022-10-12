from Noh import *


class ListaVazia(Exception):
    pass


class ListaNaoOrdenada:
    def __init__(self):
        self.head = None
        self.tail = Noh(self.head)
        self.tamanho = 0

    def __str__(self): return f'{self.head}'

    def is_empty(self): return self.head == None

    def primeiro(self):
        if self.head != None:
            return self.head.getData()
        return None

    def add(self, item):
        temp = Noh(item)
        temp.setNext(self.head)
        self.head = temp
        self.tamanho += 1
        if self.tamanho < 1:
            self.tail = temp

    def append(self, item):
        temp = Noh(item)
        self.tail.setNext(temp)
        self.tail = temp
        if self.tamanho == 0:
            self.head = temp
        self.tamanho += 1

    def size(self):
        return self.tamanho

    def remove_primeiro(self):
        if self.is_empty():
            raise ListaVazia('A Fila está vazia')
        if self.head.getNext() != None:
            self.head = self.head.getNext()
        elif self.head.getNext() == None:
            self.head = None
        self.tamanho -= 1

    def search(self, item):
        atual = self.head
        encontrou = False

        while atual != None and not encontrou:
            if atual.getData() == item:
                encontrou = True
            else:
                atual = atual.getNext()

        return encontrou

    def acessar(self, pos):
        atual = self.head
        cont = 0
        while atual != None:
            if cont == pos:
                result = atual.getData()
                return result
            else:
                cont += 1
                atual = atual.getNext()

        if self.is_empty() == True:
            return "A lista está vazia"
        return "Posicao não encontrada"

    def remove(self, item):
        try:
            atual = self.head
            anterior = None
            encontrou = False
            while not encontrou:  # percorre a lista
                if atual.getData() == item:
                    encontrou = True
                else:
                    anterior = atual
                    atual = atual.getNext()

            if anterior == None:
                self.head = atual.getNext()
            else:
                anterior.setNext(atual.getNext())
            self.tamanho -= 1
        except:
            print("Item não encontrado")


if __name__ == "__main__":
    lista = ListaNaoOrdenada()
    lista.append("Jose")
    lista.append("Adrian")
    lista.append("Torres")
    lista.append("Dos")
    lista.append("Santos")
    print(lista)
    lista.remove_primeiro()
    lista.remove_primeiro()
    lista.remove_primeiro()
    lista.remove_primeiro()
    lista.remove_primeiro()
    print(lista)
    lista.append("Jose")
    lista.append("Adrian")
    print(lista)
    lista.remove_primeiro()
    lista.remove_primeiro()
    print(lista)
