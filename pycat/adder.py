#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pycat.monoid import Monoid


class Adder(Monoid):
    """As an example of the abstract `Monoid` class."""

    def mappend(self, n):
        return lambda _: _ + n


if __name__ == '__main__':

    """Test."""

    from pycat.monoid import compose

    adder = Adder()

    f5 = compose(adder.mappend(2), adder.mappend(3))
    assert f5(10) == 15
    assert f5(120) == 125

    f21 = compose(adder.mappend(100), adder.mappend(-79))
    assert f21(10) == 31
    assert f21(120) == 141

    f10 = compose(adder.mappend(10), adder.mempty)
    assert f10(10) == 20
    assert f10(120) == 130
