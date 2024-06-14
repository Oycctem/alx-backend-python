#!/usr/bin/env python3
"""A Python module to return 10 random numbers using async comprehension."""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_comprehension - function to return 10 random numbers asynchronously.
    Returns:
        List of 10 random numbers.
    """
    result = [i async for i in async_generator()]
    return result
