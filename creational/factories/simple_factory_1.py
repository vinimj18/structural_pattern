"""
Na programação POO, o termo factory (fábrica) refere-se a uma classe ou método
que é responsável por criar objetos.

Vantagens:
    Permitem criar um sistema com baixo acoplamento entre classes porque
    ocultam as classes que criam os objetos do código cliente.

    Facilitam a adição de novas classes ao código, porque o cliente não
    conhece e nem utiliza a implementação da classe (utiliza a factory).

    Podem facilitar o processo de "cache" ou criação de "singletons" porque a
    fábrica pode retornar um objeto já criado para o cliente, ao invés de criar
    novos objetos sempre que o cliente precisar.

Desvantagens:
    Podem introduzir muitas classes no código

Vamos ver 2 tipos de Factory da GoF: Factory method e Abstract Factory

Nessa aula:
Simple Factory <- Uma espécie de Factory Method parametrizado
Simple Factory pode não ser considerado um padrão de projeto por si só
Simple Factory pode quebrar princípios do SOLID
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


class VeiculoFactory:
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'carro_luxo':
            return CarroLuxo()
        if tipo == 'carro_popular':
            return CarroPopular()
        if tipo == 'moto_popular':
            return MotoPopular()
        assert 0, 'Veículo Inexistente'


if __name__ == '__main__':
    from random import choice

    tipos = ['carro_luxo', 'carro_popular', 'moto_popular']
    for i in range(10):
        carro = VeiculoFactory.get_carro(choice(tipos))
        carro.chama_veiculo()
