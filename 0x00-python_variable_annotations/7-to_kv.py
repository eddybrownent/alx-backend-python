#!/usr/bin/env python3
"""
Type-annotated function
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts string and int/float to tuple

    Args:
        k (str): the string
        v (Union[int, float]): The integer or float

    Returns:
        Tuple[str, float]: tuple string k and the square of v
    """
    result = (k, v ** 2)
    return result
