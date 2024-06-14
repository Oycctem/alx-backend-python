#!/usr/bin/env python3
"""Contains a method that measures the total execution time of a function"""

from time import perf_counter
import asyncio
wait_n = __import__('wait_n').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time of wait_n(n, max_delay).
    Args:
        n (int): The number of coroutines to launch.
        max_delay (int): The maximum amount of time to wait for each coroutine.
    Returns:
        float: The average elapsed time in seconds.
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = perf_counter() - start
    return elapsed / n
