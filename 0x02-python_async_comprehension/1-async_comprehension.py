#!/usr/bin/env python3
"""
Coroutine collecting 10 random nums using an async comprehension
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collects 10 random numbers using an async comprehension
    Returns:
        List[float]: list of 10 random nums
    """
    rslt = [_ async for _ in async_generator()]
    return rslt
