#!/usr/bin/env python3
""" Task 0 """


def index_range(page, page_size):
    if page <= 0 or page_size <= 0:
        return (0, 0)

    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)