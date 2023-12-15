#!/usr/bin/env python3
"""
Asynchronous generator coroutine
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    generates random nums btwn 0 & 10 after waiting for 1 sec

    Results:
        float: A random float between 0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
