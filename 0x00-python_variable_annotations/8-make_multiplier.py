#!/usr/bin/env python3
"""
Type-annotated function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function

    Args:
        multiplier (float): rthe multiplier value

    Returns:
        Callable[[float], float]: a function
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
