#!/usr/bin/env python3
"""A Python module to measure the runtime of
async_comprehension executed four times in parallel."""

import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime - Coroutine to execute async_comprehension
    four times in parallel and measure the total runtime.
    Returns:
        Total runtime of executing async_comprehension four times in parallel.
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time
    return total_runtime
