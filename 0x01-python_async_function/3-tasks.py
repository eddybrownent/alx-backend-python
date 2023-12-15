#!/usr/bin/env python3
"""
Creates an asyncio.Task for the wait_random func
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Args:
        max_delay (int): maxi delay for wait_random

    Returns:
        asyncio.Task[Union[int, float]]: asyncio.Task for wait_random
    """
    async_task = asyncio.create_task(wait_random(max_delay))
    return async_task
