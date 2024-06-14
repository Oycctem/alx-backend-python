#!/usr/bin/env python3
"""executes multiple coroutines at the same time with async"""

import asyncio
import random
from typing import List
wait_random = __import__('wait_random').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Call wait_random n times with max_delay and return
    the list of all the delays in ascending order.
    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for wait_random.
    Returns:
        List[float]: List of delays in ascending order.
    """
    result = []

    delays = [wait_random(max_delay) for time in range(n)]

    for coroutine in asyncio.as_completed(delays):
        val = await coroutine
        result.append(val)

    return result
