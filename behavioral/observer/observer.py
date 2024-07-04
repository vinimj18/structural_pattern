"""
O padrão Observer tem a intenção de
definir uma dependência de um-para-muitos entre
objetos, de maneira que quando um objeto muda de
estado, todo os seus dependentes são notificados
e atualizados automaticamente.

Um observer é um objeto que gostaria de ser
informado, um observable (subject) é a entidade
que gera as informações.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class IObservable(ABC):
    """Observable"""

    @property
    @abstractmethod
    def state(self): pass

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def notify_observers(self) -> None: pass


class WeartherStation(IObservable):
    """Observable"""

    def __init__(self) -> None:
        self._observers: list[IObserver] = []
        self._state: dict = {}

    @property
    def state(self) -> dict:
        return self._state

    @state.setter
    def state(self, state_update: dict) -> None:
        new_state: dict = {**self._state, **state_update}

        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self) -> None:
        self._state = {}
        self.notify_observers()

    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if observer not in self._observers:
            return
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()
        print()


class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: pass


class Smartphone(IObserver):
    def __init__(self, nome, observable: IObservable) -> None:
        self.name = nome
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(f'{self.name}: o objeto {observable_name} '
              f'acabou de ser atualizado => {self.observable.state}')


class Notebook(IObserver):
    def __init__(self, observable: IObservable) -> None:
        self.observable = observable

    def show(self) -> None:
        state = self.observable.state
        print('Sou o Notebook e vou fazer outra coisa com esses dados', state)

    def update(self) -> None:
        self.show()


if __name__ == '__main__':
    weather_station = WeartherStation()

    smartphone_1 = Smartphone('iPhone', weather_station)
    smartphone_2 = Smartphone('Galaxy S', weather_station)
    notebook = Notebook(weather_station)

    weather_station.add_observer(smartphone_1)
    weather_station.add_observer(smartphone_2)
    weather_station.add_observer(notebook)

    weather_station.state = {'temperature': '25'}
    weather_station.state = {'temperature': '30'}
    weather_station.state = {'humidity': '75%'}

    weather_station.remove_observer(smartphone_1)
    weather_station.reset_state()
