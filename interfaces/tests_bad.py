from unittest import TestCase

from bad import Order, Shipper, ShippingCost


class TestsBad(TestCase):

    def test_shipping_costs(self):
        # test FedEx shipping
        order = Order(Shipper.FEDEX)
        shipping_cost = ShippingCost()
        cost = shipping_cost.calculate(order)
        assert cost == 3.0

        # test UPS shipping
        order = Order(Shipper.UPS)
        shipping_cost = ShippingCost()
        cost = shipping_cost.calculate(order)
        assert cost == 4.0

        # test Postal Service shipping
        # test UPS shipping
        order = Order(Shipper.POSTAL)
        shipping_cost = ShippingCost()
        cost = shipping_cost.calculate(order)
        assert cost == 5.0
