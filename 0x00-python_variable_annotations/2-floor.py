#!/usr/bin/env python3
"""
Type-annotated function
"""
# Import math library
import math


def floor(n: float) -> int:
    """
    Round number down to the nearest integer

    Args:
        n: (float)

    Return:
        int: floor of n
    """
    return math.floor(n)
