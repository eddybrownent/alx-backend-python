#!/usr/bin/env python3
"""
async that takes in an int waits for random delay
& returns it
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for that duration
    Args:
        max_delay(float, optional): max delay secs. Defaults 10

    Returns:
        float: random delay

    """
    value = random.uniform(0, max_delay)
    await asyncio.sleep(value)
    return value
