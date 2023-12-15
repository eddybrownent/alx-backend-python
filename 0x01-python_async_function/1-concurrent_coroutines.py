#!/usr/bin/env python3
"""
Async spawns wait_random n times with a max_delay
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: float = 10) -> list[float]:
    """
    Args:
        n (int): num of time to spawn wait_random.
        max_delay (float, optional): max delay in secs Defaults 10

    Returns:
        list[float]: List of delays in ascending order
    """
    values = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(values)]
