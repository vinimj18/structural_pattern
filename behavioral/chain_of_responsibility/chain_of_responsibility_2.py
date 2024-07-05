"""
Chain of responsibility (COR) é um padrão comportamental
que tem a intenção de evitar o acoplamento do remetente de
uma solicitação ao seu receptor, ao dar a mais de um objeto
a oportunidade de tratar a solicitação.
Encadear os objetos receptores passando a solicitação
ao longo da cadeia até que um objeto a trate.
"""
from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self) -> None:
        self.successor: Handler

    @abstractmethod
    def handle(self, letter: str) -> str: pass


class HandlerABC(Handler):
    def __init__(self, successor: Handler) -> None:
        self.letters = ['A', 'B', 'C']
        self.successor = successor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'Handler ABC conseguiu tratar o valor "{letter}"'
        return self.successor.handle(letter)


class HandlerDEF(Handler):
    def __init__(self, successor: Handler) -> None:
        self.letters = ['D', 'E', 'F']
        self.successor = successor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'Handler DEF conseguiu tratar o valor "{letter}"'
        return self.successor.handle(letter)


class HandlerFail(Handler):
    def handle(self, letter: str) -> str:
        return f'Handler Fail não conseguiu tratar o valor "{letter}"'


if __name__ == '__main__':
    handler_fail = HandlerFail()
    handler_def = HandlerDEF(handler_fail)
    handler_abc = HandlerABC(handler_def)

    print(handler_abc.handle('A'))
    print(handler_abc.handle('B'))
    print(handler_abc.handle('C'))
    print(handler_abc.handle('D'))
    print(handler_abc.handle('E'))
    print(handler_abc.handle('F'))
    print(handler_abc.handle('G'))
    print(handler_abc.handle('H'))
    print(handler_abc.handle('I'))
