"""
Chain of responsibility (COR) é um padrão comportamental
que tem a intenção de evitar o acoplamento do remetente de
uma solicitação ao seu receptor, ao dar a mais de um objeto
a oportunidade de tratar a solicitação.
Encadear os objetos receptores passando a solicitação
ao longo da cadeia até que um objeto a trate.
"""

# Implementando com funções


def handler_abc(letter: str) -> str:
    letters = ['A', 'B', 'C']

    if letter in letters:
        return f'Handler ABC conseguiu tratar o valor "{letter}"'
    return handler_def(letter)


def handler_def(letter: str) -> str:
    letters = ['D', 'E', 'F']

    if letter in letters:
        return f'Handler DEF conseguiu tratar o valor "{letter}"'
    return handler_fail(letter)


def handler_fail(letter: str) -> str:
    return f'Handler Fail não conseguiu tratar o valor "{letter}"'


if __name__ == '__main__':
    print(handler_abc('A'))
    print(handler_abc('B'))
    print(handler_abc('C'))
    print(handler_abc('D'))
    print(handler_abc('E'))
    print(handler_abc('F'))
    print(handler_abc('G'))
    print(handler_abc('H'))
    print(handler_abc('I'))
