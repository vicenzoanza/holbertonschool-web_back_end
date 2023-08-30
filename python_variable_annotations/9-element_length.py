#!/usr/bin/env python3
""" task 9 """
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return values with the appropriate types """
    return [(i, len(i)) for i in lst]
