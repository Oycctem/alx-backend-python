#!/usr/bin/env python3
"""an asynchronous coroutine that takes in an integer argument """

import asyncio
from wait_random import wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Spawn wait_random n times with the specified max_delay and
    return the list of all the delays.
    The list of the delays should be in ascending order.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        list: List of delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
