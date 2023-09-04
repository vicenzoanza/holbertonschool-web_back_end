#!/usr/bin/env python3
""" task 4 """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Take the code and alter it into a new function  """
    tasks = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    delays = await asyncio.gather(*tasks)

    return delays
