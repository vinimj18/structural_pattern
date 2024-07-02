"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantindo o
baixo acoplamento entre classes.
"""

from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def chama_veiculo(self) -> None: pass


class CarroLuxo(Veiculo):
    def chama_veiculo(self) -> None:
        print('Carro de luxo está a caminho.')


class CarroPopular(Veiculo):
    def chama_veiculo(self) -> None:
        print('Carro popular está a caminho.')


class MotoPopular(Veiculo):
    def chama_veiculo(self) -> None:
        print('Moto popular está a caminho.')


class MotoLuxo(Veiculo):
    def chama_veiculo(self) -> None:
        print('Moto de luxo está a caminho.')


class VeiculoFactory(ABC):
    def __init__(self, tipo) -> None:
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo:  # type: ignore
        pass

    def chama_veiculo(self):
        self.carro.chama_veiculo()


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:  # type: ignore
        if tipo == 'carro_luxo':
            return CarroLuxo()
        if tipo == 'carro_popular':
            return CarroPopular()
        if tipo == 'moto_popular':
            return MotoPopular()
        if tipo == 'moto_luxo':
            return MotoLuxo()
        assert 0, 'Veículo Inexistente'


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:  # type: ignore
        if tipo == 'carro_popular':
            return CarroPopular()
        assert 0, 'Veículo Inexistente'


if __name__ == '__main__':
    from random import choice
    carros_disponiveis_zn = [
        'carro_luxo',
        'carro_popular',
        'moto_popular',
        'moto_luxo'
    ]
    carros_disponiveis_zs = ['carro_popular']

    print('ZONA NORTE:')
    for i in range(10):
        carro = ZonaNorteVeiculoFactory(choice(carros_disponiveis_zn))
        carro.chama_veiculo()
    print()
    print('ZONA SUL:')
    for i in range(10):
        carro2 = ZonaSulVeiculoFactory(choice(carros_disponiveis_zs))
        carro2.chama_veiculo()
