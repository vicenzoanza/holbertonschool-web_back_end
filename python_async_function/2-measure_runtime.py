#!/usr/bin/env python3
""" task 2 """
import asyncio
import random
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """"""
    start = time.time()

    processs = asyncio.run(wait_n(n, max_delay))

    end = time.time()
    finish = end - start

    return finish / n
