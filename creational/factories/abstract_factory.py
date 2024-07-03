from abc import ABC, abstractmethod


class VeiculoPopular(ABC):
    @abstractmethod
    def chama_veiculo(self) -> None: pass


class VeiculoLuxo(ABC):
    @abstractmethod
    def chama_veiculo(self) -> None: pass


class ZNCarroLuxo(VeiculoLuxo):
    def chama_veiculo(self) -> None:
        print('Carro de luxo está a caminho da Zona Norte.')


class ZNCarroPopular(VeiculoPopular):
    def chama_veiculo(self) -> None:
        print('Carro popular está a caminho da Zona Norte.')


class ZNMotoPopular(VeiculoPopular):
    def chama_veiculo(self) -> None:
        print('Moto popular está a caminho da Zona Norte.')


class ZNMotoLuxo(VeiculoLuxo):
    def chama_veiculo(self) -> None:
        print('Moto de luxo está a caminho da Zona Norte.')


class ZSCarroLuxo(VeiculoLuxo):
    def chama_veiculo(self) -> None:
        print('Carro de luxo está a caminho da Zona Sul.')


class ZSCarroPopular(VeiculoPopular):
    def chama_veiculo(self) -> None:
        print('Carro popular está a caminho da Zona Sul.')


class ZSMotoPopular(VeiculoPopular):
    def chama_veiculo(self) -> None:
        print('Moto popular está a caminho da Zona Sul.')


class ZSMotoLuxo(VeiculoLuxo):
    def chama_veiculo(self) -> None:
        print('Moto de luxo está a caminho da Zona Sul.')


class VeiculoFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_carro_popular() -> VeiculoPopular:
        pass

    @staticmethod
    @abstractmethod
    def get_carro_luxo() -> VeiculoLuxo:
        pass

    @staticmethod
    @abstractmethod
    def get_moto_popular() -> VeiculoPopular:
        pass

    @staticmethod
    @abstractmethod
    def get_moto_luxo() -> VeiculoLuxo:
        pass


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return ZNCarroPopular()

    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return ZNCarroLuxo()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return ZNMotoPopular()

    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return ZNMotoLuxo()


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return ZSCarroPopular()

    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return ZSCarroLuxo()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return ZSMotoPopular()

    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return ZSMotoLuxo()


class Cliente:
    def buscar_clientes(self):
        for factory in [ZonaNorteVeiculoFactory(), ZonaSulVeiculoFactory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.chama_veiculo()

            carro_luxo = factory.get_carro_luxo()
            carro_luxo.chama_veiculo()

            moto_popular = factory.get_moto_popular()
            moto_popular.chama_veiculo()

            moto_luxo = factory.get_moto_luxo()
            moto_luxo.chama_veiculo()


if __name__ == '__main__':
    cliente = Cliente()
    cliente.buscar_clientes()
