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


class Pizza(ABC):
    def make_pizza(self) -> None:
        self.make_dough()
        self.hook_dough_type()
        self.hook_topping_prep()
        self.add_toppings()
        self.bake()
        self.cut()
        self.serve()
        self.ready()

    def make_dough(self) -> None:
        print('1 - Preparing the dough.')

    def bake(self) -> None:
        print('3 - Baking in the oven for 15 min or until crispy.')

    def cut(self) -> None:
        print('4 - Cutting in 8 slices.')

    def serve(self) -> None:
        print('5 - Putting it in the pizza box and giving it to customer.')

    def ready(self) -> None:
        print(f'Pizza {self.__class__.__name__} is ready! Enjoy!')

    def hook_topping_prep(self) -> None: pass

    def hook_dough_type(self) -> None: pass

    @abstractmethod
    def add_toppings(self) -> None: pass


class Margherita(Pizza):
    def hook_topping_prep(self) -> None:
        print('Slicing the tomatoes...')

    def add_toppings(self) -> None:
        print('2 - Adding the toppings: sauce, cheese, tomatoes, basil...')


class QuattroFormaggioGF(Pizza):
    def hook_dough_type(self) -> None:
        print('Making it Gluten-Free...')

    def add_toppings(self) -> None:
        print(
            '2 - Adding the toppings: cheese, cheese, cheese and MORE CHEESE!'
        )


if __name__ == '__main__':
    pizza1 = Margherita()
    pizza1.make_pizza()

    print()

    pizza2 = QuattroFormaggioGF()
    pizza2.make_pizza()
