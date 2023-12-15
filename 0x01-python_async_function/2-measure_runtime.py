#!/usr/bin/env python3
"""
Script that Measures total execution time
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Args:
        n (int): number of times to spawn wait_random
        max_delay (float, optional): Max delay in secs. Defaults 10

    Returns:
        float: Average time per execute
    """
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    all_time = end_time - start_time

    return all_time / n
