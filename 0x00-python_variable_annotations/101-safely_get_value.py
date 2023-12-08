#!/usr/bin/env python3
"""
Add type annotations to the function
"""
from typing import Any, Mapping, Union, TypeVar

T = TypeVar("T")


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    gets a value from a dict
    Parameters:
        dct (Mapping[Any, T]): The input dict
        key (Any): The key to look for
        default (Union[T, None], optional): default value to return

    Returns:
    - Union[Any, ~T]: value of the key if it exists, else default
    """
    if key in dct:
        return dct[key]
    else:
        return default
