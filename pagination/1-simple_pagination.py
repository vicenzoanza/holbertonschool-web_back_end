#!/usr/bin/env python3
""" Task 1 """

import csv
from typing import List


def index_range(page, page_size):
    """ Write a function named index_range that takes two integer arguments """
    if page <= 0 or page_size <= 0:
        return (0, 0)

    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()
        start_index, end_index = index_range(page, page_size)
        if start_index >= len(data):
            return []

        return data[start_index:end_index]
