#!/usr/bin/env python3
""" task 6 """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ integers and floats and returns their sum as a float """
    return sum(mxd_lst)
