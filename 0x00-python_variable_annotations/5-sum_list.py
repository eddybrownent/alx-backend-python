#!/usr/bin/env python3
"""
Type-annotated function
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Args:
        inpu_list : (List[float])

    Returns:
        float: sum of input_list
    """
    return sum(input_list)
