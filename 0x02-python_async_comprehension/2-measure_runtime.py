#!/usr/bin/env python3
"""
measures execution time
"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine measures runtime of executing async_comprehension 4 times

    Returns:
        float: total runtime in secs
    """
    start_time = asyncio.get_event_loop().time()
    task = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*task)
    end_time = asyncio.get_event_loop().time()
    return (end_time - start_time)
