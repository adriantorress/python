class PilhaVazia(Exception):
    pass


class Pilha:
    def __init__(self):
        self._pilha = []

    def top(self):
        if self.is_empty():
            raise PilhaVazia('A pilha está vazia')
        return self._pilha[-1]

    def is_empty(self):
        return len(self._pilha) == 0

    def pop(self):
        if self.is_empty():
            raise PilhaVazia('A pilha está vazia')
        return self._pilha.pop()

    def push(self, e):
        self._pilha.append(e)

    def size(self):
        return self.__len__()

    def __len__(self):
        return len(self.pilha)


def checkPassword(senha: str):
    if senha[0].islower() or senha[-1].isupper():
        return "Inválida"

    p1 = Pilha()
    for char in senha:
        p1.push(char)

    p2 = Pilha()
    for i in range(len(senha)):
        if p1.top().islower():
            p2.push(p1.pop())
        elif p2.pop().upper() == p1.pop():
            pass
        else:
            return "Inválida"

    return "Válida"


print(checkPassword("Aa"))
print(checkPassword("aA"))
print(checkPassword("AB"))
print(checkPassword("Ab"))
print(checkPassword("ABba"))
print(checkPassword("ABab"))
print(checkPassword("ABbCca"))
print(checkPassword("ABCcDEedba"))
print(checkPassword("BRrAba"))
