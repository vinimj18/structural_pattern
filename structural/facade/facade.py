"""
Façade (Fachada) é um padrão de projeto estrutural
que tem a intenção de fornecer uma interface
unificada para um conjunto de interfaces em um
subsistema. Façade define uma interface de nível
mais alto que torna o subsistema mais fácil de ser
usado.
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


class WeatherStationFacade:
    """ A Facade está aqui """

    def __init__(self) -> None:
        self.weather_station = WeartherStation()

        self.smartphone_1 = Smartphone('iPhone', self.weather_station)
        self.smartphone_2 = Smartphone('Galaxy S', self.weather_station)
        self.notebook = Notebook(self.weather_station)

        self.weather_station.add_observer(self.smartphone_1)
        self.weather_station.add_observer(self.smartphone_2)
        self.weather_station.add_observer(self.notebook)

    def add_observer(self, observer: IObserver) -> None:
        self.weather_station.add_observer(observer)

    def remove_observer(self, observer: IObserver) -> None:
        self.weather_station.remove_observer(observer)

    def change_state(self, state: dict) -> None:
        self.weather_station.state = state

    def remove_smartphone(self) -> None:
        self.weather_station.remove_observer(self.smartphone_1)

    def reset_state(self) -> None:
        self.weather_station.reset_state()


if __name__ == '__main__':
    weather_station = WeatherStationFacade()

    weather_station.change_state({'temperature': '25'})
    weather_station.change_state({'temperature': '30'})
    weather_station.change_state({'humidity': '75%'})

    weather_station.remove_smartphone()
    weather_station.reset_state()

    weather_station.change_state({'temperature': '25'})
    weather_station.change_state({'temperature': '30'})
    weather_station.change_state({'humidity': '75%'})
