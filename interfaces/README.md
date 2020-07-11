# Program to an interface

## Exercise

*Recommended Python version 3.4 or above.*

A program to calculate the cost of an order is included in `bad.py`, tests can be found in `tests_bad.py`. This approach does
not make use of an interface and comes with some issues:
- Strong coupling between `Order`, `Shipper` and `ShippingCost`
- Long `if/else` clause

Rewrite the program `bad.py` as `strategy.py` where an interface will be used to solve the issues mentioned. The tests
in `test_strategy.py` should pass for a correct solution.

### More information

- [Formal interfaces in Python](https://github.com/CrossLangNV/python-for-java-devs/blob/master/session-01.md#formal-interfaces-abcs)
- [Strategy pattern](https://en.wikipedia.org/wiki/Strategy_pattern)
