from enum import Enum


class Shipper(Enum):
    FEDEX = 1
    UPS = 2
    POSTAL = 3


class Order:
    def __init__(self, shipper):
        self.shipper = shipper


class ShippingCost:
    def calculate(self, order):
        if order.shipper == Shipper.FEDEX:
            return self._fedex_cost(order)
        elif order.shipper == Shipper.UPS:
            return self._ups_cost(order)
        elif order.shipper == Shipper.POSTAL:
            return self._postal_cost(order)
        else:
            raise ValueError('Invalid shipper %s ', order.shipper)

    def _fedex_cost(self, order):
        return 3.0

    def _ups_cost(self, order):
        return 4.0

    def _postal_cost(self, order):
        return 5.0
