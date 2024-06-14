#!/usr/bin/env python3
"""Contains a method that returns a list of delays"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay and returns
    the list of all the delays in ascending order.
    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay for task_wait_random.
    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
