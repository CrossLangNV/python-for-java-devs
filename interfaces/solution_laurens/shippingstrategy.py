from abc import ABC, abstractmethod


class Order(object):
    pass


class ShippingStrategy(ABC):
    @abstractmethod
    def cost(self, order: Order) -> float:
        pass


class FedExStrategy(ShippingStrategy):
    def cost(self, order):
        return 3.0


class UPSStrategy(ShippingStrategy):
    def cost(self, order):
        return 4.0


class PostalStrategy(ShippingStrategy):
    def cost(self, order):
        return 5.0


class ShippingCost(object):
    def __init__(self, strategy: ShippingStrategy):
        assert isinstance(strategy, ShippingStrategy)

        self.strategy = strategy

    def calculate(self, order: Order):
        cost = self.strategy.cost(order)
        return cost
