#!/usr/bin/env python3
"""A Python module to return 10 random numbers using async comprehension."""

from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    async_comprehension - function to return 10 random numbers asynchronously.
    Returns:
        List of 10 random numbers.
    """
    result = [i async for i in async_generator()]
    return result
