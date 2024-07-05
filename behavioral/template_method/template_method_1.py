"""
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template method permite
que subclasses redefinam certos passos de um algoritmo
sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses
utilizem caso necessário.

The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC - Inversão de controle)
"""
from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.operation1()
        self.base_class_method()
        self.operation2()

    def hook(self) -> None: pass

    def base_class_method(self) -> None:
        print('SOU DA CLASSE ABSTRATA E SEREI EXECUTADO TAMBÉM!')

    @abstractmethod
    def operation1(self) -> None: pass

    @abstractmethod
    def operation2(self) -> None: pass


class ConcreteClass1(Abstract):
    def hook(self) -> None:
        print('Utilizando o hook na classe concreta 1.')

    def operation1(self) -> None:
        print('Essa é a operação 1.')

    def operation2(self) -> None:
        print('Essa é a operação 2.')


class ConcreteClass2(Abstract):
    def operation1(self) -> None:
        print('Essa é a operação 1. Similar mas diferente.')

    def operation2(self) -> None:
        print('Essa é a operação 2. Similar mas diferente.')


if __name__ == '__main__':
    c1 = ConcreteClass1()
    c1.template_method()

    print()

    c2 = ConcreteClass2()
    c2.template_method()
