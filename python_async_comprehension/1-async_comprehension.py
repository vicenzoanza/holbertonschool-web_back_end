#!/usr/bin/env python3
""" Task 1 """
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Will collect 10 random numbers using an async comprehensing """
    number = [n async for n in async_generator()]
    return number