#!/usr/bin/env python3
"""
Augment the code with correct duck-typed annotations
"""
from typing import Union, Any, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Gets the first element from a sequence

    Args:
        lst (Sequence[Any]): the input

    Returns:
        Optional[Any]: The first element if the sequence otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
