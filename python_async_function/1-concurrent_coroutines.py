#!/usr/bin/env python3
""" task 1 """
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ should return the list of all the delays (float values). """
    delays = []

    async def wait_n2():
        delay = await wait_random(max_delay)
        delays.append(delay)

    await asyncio.gather(*[wait_n2() for _ in range(n)])

    delays.sort()

    return delays
