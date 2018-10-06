#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import Any, Mapping
from pycat.monoid import Monoid, compose


class Writer(object):
    """Auxillary class."""

    def __init__(self, a: Any, log: str):
        self._a = a
        self._log = log

    @property
    def a(self):
        return self._a

    @property
    def log(self):
        return self._log


class WriterGetter(object):
    """Auxillary class."""

    def __init__(self, process: Mapping[Any, Any], log: str):
        self._process = process
        self._log = log

    def __call__(self, a: Any) -> Writer:
        return Writer(self.process(a), self.log)

    @property
    def process(self):
        return self._process

    @property
    def log(self):
        return self._log


class WriterMonoid(Monoid):
    """The monoid-set is the set of all `WriterGetter`s."""

    def mappend(self, writer_getter):
        """
        Args:
            writer_getter: An instance of `WriterGetter`.
        
        Returns:
            Mapping from `WriterGetter` to `WriterGetter`.
        """
        def f(writer_getter_1):
            process = compose(writer_getter.process,
                              writer_getter_1.process)
            log = writer_getter_1.log + writer_getter.log
            return WriterGetter(process, log)
        return f


if __name__ == '__main__':

    to_upper = WriterGetter(lambda s: s.upper(), 'Upper ')
    to_lower = WriterGetter(lambda s: s.lower(), 'Lower ')

    writer_monoid = WriterMonoid()

    writer_getter = writer_monoid.mappend(to_upper)(to_lower)
    writer = writer_getter('Hello, world!')

    assert writer.a == 'HELLO, WORLD!'
    assert writer.log == 'Lower Upper '
