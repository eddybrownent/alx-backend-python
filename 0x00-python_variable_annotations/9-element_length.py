#!/usr/bin/env python3
"""
Annotate the below function’s parameters &
return values with the appropriate types

"""
from typing import Sequence, List, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculates the length of each element in the input iterable

    Args:
        lst (Iterable[Sequence]): an iterable

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples
    """
    return [(i, len(i)) for i in lst]
