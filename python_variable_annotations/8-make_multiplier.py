#!/usr/bin/env python3
""" task 8 """
from typing import Callable


def make_multiplier(multiplier: float) ->  Callable[[float], float]:
    """ """
    def multiplier_function(x: float) -> float:
        """ """
        return x * multiplier
    return multiplier_function
