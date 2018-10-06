#!/usr/bin/env python
# -*- coding: utf-8 -*-


import abc


def identity(e):
    return e


def compose(*funcs):
    """Returns the mapping of composition f_0 o f_1 o ... o f_n,
    where `funcs = [f_0, ..., f_n]`.

    Args:
        fs: Iterable of compatible currified mappings.

    Returns:
        A currified mapping.
    """
    if not funcs:
        return identity
    else:
        f0 = funcs[0]
        def composed(_):
            # f_1 o f_2 o ... o f_n
            pre_composed = compose(*funcs[1:])
            return f0(pre_composed(_))
        return composed


class Monoid(abc.ABC):

    @property
    def mempty(self):
        """Returns the neutral map."""
        return identity

    @abc.abstractmethod
    def mappend(self, elem):
        """
        Args:
            elem: Element in the monoid-set.
            
        Returns:
            Mapping from the monoid-set to itself.
        """
        pass
