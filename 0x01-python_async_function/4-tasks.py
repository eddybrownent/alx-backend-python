#!/usr/bin/env python3
"""
Async spawns wait_random n times with a max_delay
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Args:
        n (int): num of time to spawn wait_random.
        max_delay (float, optional): max delay in secs Defaults 10

    Returns:
        list[float]: List of delays in ascending order
    """

    values = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(values)]
