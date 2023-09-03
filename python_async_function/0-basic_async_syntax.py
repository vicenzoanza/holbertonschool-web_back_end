#!/usr/bin/env python3
""" task 0 """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ generate delay 0 to 10 """
    delay = random.uniform(0, max_delay)
    
    await asyncio.sleep(delay)
    
    return delay