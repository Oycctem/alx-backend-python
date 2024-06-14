#!/usr/bin/env python3
"""Contains a method that returns a task"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns a task that waits for a random number of seconds
    Args:
        max_delay (int): Maximum number of seconds that the task will wait.
    Returns:
        asyncio.Task: An asyncio.Task object.
    """
    return asyncio.create_task(wait_random(max_delay))
