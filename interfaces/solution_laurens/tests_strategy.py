from unittest import TestCase

from shippingstrategy import Order, FedExStrategy, UPSStrategy, PostalStrategy, ShippingCost


class TestsStrategy(TestCase):

    def test_shipping_costs(self):
        # test FedEx shipping
        strategy = FedExStrategy()
        assert test_shipping_costs_shared(strategy) == 3.0

        # test UPS shipping
        strategy = UPSStrategy()
        assert test_shipping_costs_shared(strategy) == 4.0

        # test Postal Service shipping
        strategy = PostalStrategy()
        assert test_shipping_costs_shared(strategy) == 5.0


def test_shipping_costs_shared(strategy):
    order = Order()
    shipping_cost = ShippingCost(strategy)
    cost = shipping_cost.calculate(order)

    return cost
