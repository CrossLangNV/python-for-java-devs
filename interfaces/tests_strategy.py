from unittest import TestCase

from strategy import Order, FedExStrategy, UPSStrategy, PostalStrategy, ShippingCost


class TestsStrategy(TestCase):

    def test_shipping_costs(self):
        # test FedEx shipping
        order = Order()
        strategy = FedExStrategy()
        shipping_cost = ShippingCost(strategy)
        cost = shipping_cost.calculate(order)
        assert cost == 3.0

        # test UPS shipping
        order = Order()
        strategy = UPSStrategy()
        shipping_cost = ShippingCost(strategy)
        cost = shipping_cost.calculate(order)
        assert cost == 4.0

        # test Postal Service shipping
        order = Order()
        strategy = PostalStrategy()
        shipping_cost = ShippingCost(strategy)
        cost = shipping_cost.calculate(order)
        assert cost == 5.0
