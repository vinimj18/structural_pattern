from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    def __init__(self, total: float, discount: DiscountStrategy) -> None:
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total

    @property
    def total_with_discount(self):
        return self._discount.calculate(self.total)


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float: pass


class NoDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value


class TwentyFivePercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value * 0.75


class FiftyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value * 0.5


class CustomDiscount(DiscountStrategy):
    def __init__(self, discount) -> None:
        self.discount = 1 - (discount/100)

    def calculate(self, value: float) -> float:
        return value * self.discount


if __name__ == '__main__':
    twentyfive = TwentyFivePercent()
    fifty = FiftyPercent()
    nodiscount = NoDiscount()
    custom = CustomDiscount(15)

    order = Order(1000, twentyfive)
    print(order.total, order.total_with_discount)

    order = Order(1000, fifty)
    print(order.total, order.total_with_discount)

    order = Order(1000, nodiscount)
    print(order.total, order.total_with_discount)

    order = Order(1000, custom)
    print(order.total, order.total_with_discount)

    order = Order(1000, CustomDiscount(12))
    print(order.total, order.total_with_discount)
