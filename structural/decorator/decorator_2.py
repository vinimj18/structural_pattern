"""
Decorator é um padrão de projeto estrutural que permite que você
adicione novos comportamentos em objetos ao colocá-los dentro de
um "wrapper" (decorador) de objetos.
Decoradores fornecem uma alternativa flexível ao uso de subclasses
para a extensão de funcionalidades.

Decorator (padrão de projeto) != Decorator em Python

Python decorator -> Um decorator é um callable que aceita outra
função como argumento (a função decorada). O decorator pode
realizar algum processamento com a função decorada e devolvê-la
ou substituí-la por outra função ou objeto invocável.
Do livro "Python Fluente", por Luciano Ramalho (pág. 223)
"""
from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

# Ingredients


@dataclass
class Ingredient:
    price: float


@dataclass
class Bread(Ingredient):
    price: float = 1.0


@dataclass
class Sausage(Ingredient):
    price: float = 2.3


@dataclass
class Bacon(Ingredient):
    price: float = 3.15


@dataclass
class Egg(Ingredient):
    price: float = 1.5


@dataclass
class Cheese(Ingredient):
    price: float = 2.30


@dataclass
class MashedPotato(Ingredient):
    price: float = 2.0


@dataclass
class PotatoSticks(Ingredient):
    price: float = 1.5


# Hot Dogs

class HotDog:
    _name: str
    _ingredients: list[Ingredient]

    @property
    def price(self) -> float:
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> str:
        return self._name

    @property
    def ingredients(self) -> list[Ingredient]:
        return self._ingredients

    def __repr__(self) -> str:
        return f'{self.name}({self.price}) -> {self.ingredients}'


class SimpleHotDog(HotDog):
    def __init__(self) -> None:
        self._name: str = 'SimpleHotDog'
        self._ingredients: list[Ingredient] = [
            Bread(),
            Sausage(),
            PotatoSticks()
        ]


class SpecialHotDog(HotDog):
    def __init__(self) -> None:
        self._name: str = 'SpecialHotDog'
        self._ingredients: list[Ingredient] = [
            Bread(),
            Sausage(),
            Bacon(),
            Egg(),
            Cheese(),
            MashedPotato(),
            PotatoSticks()
        ]

# Decorators


class HotdogDecorator(HotDog):
    def __init__(self, hotdog: HotDog, ingredient: Ingredient) -> None:
        self.hotdog = hotdog
        self._ingredient = ingredient

        self._ingredients = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self._ingredient)

    @property
    def name(self) -> str:
        return f'{self.hotdog.name} +{self._ingredient.__class__.__name__}'


if __name__ == '__main__':
    simple_hotdog = SimpleHotDog()
    print(simple_hotdog)

    bacon_simple_hotdog = HotdogDecorator(simple_hotdog, Bacon())
    print(bacon_simple_hotdog)

    egg_bacon_simple_hotdog = HotdogDecorator(bacon_simple_hotdog, Egg())
    print(egg_bacon_simple_hotdog)

    mashedpotato_egg_bacon_simple_hotdog = HotdogDecorator(
        egg_bacon_simple_hotdog,
        MashedPotato()
    )
    print(mashedpotato_egg_bacon_simple_hotdog)
