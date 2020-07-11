from abc import ABC, abstractmethod


class Order:
    pass


class ShippingStrategy(ABC):
    @abstractmethod
    def calculate(self, order):
        pass


class FedExStrategy(ShippingStrategy):
    def calculate(self, order):
        return 3.0


class UPSStrategy(ShippingStrategy):
    def calculate(self, order):
        return 4.0


class PostalStrategy(ShippingStrategy):
    def calculate(self, order):
        return 5.0


class ShippingCost:
    def __init__(self, strategy):
        self.strategy = strategy

    def calculate(self, order):
        return self.strategy.calculate(order)
