#!/usr/bin/env python3
"""
Type-annotated function
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Args:
        mxd_list: list of ints and floats

    Returns:
        float: sum of mxd_list
    """
    return sum(mxd_lst)
