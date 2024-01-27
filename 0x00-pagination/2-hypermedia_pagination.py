#!/usr/bin/env python3

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(page: int, page_size: int) -> tuple:
        """Calculate start and end indexes for pagination
        """
        if page <= 0 or page_size <= 0:
            raise ValueError("Page and page_size must be positive integers.")

        start_index = (page - 1) * page_size
        end_index = page * page_size

        return start_index, end_index

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a specific page of the dataset
        """
        assert isinstance(page, int) and page > 0, "Page must be an integer > 0"
        assert isinstance(page_size, int) and page_size > 0, "Page size be an integer > 0"

        total_pages = math.ceil(len(self.dataset()) / page_size)

        if page > total_pages:
            return []

        start_index, end_index = self.index_range(page, page_size)
        return self.dataset()[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Get hypermedia information for pagination
        """
        data_page = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data_page),
            'page': page,
            'data': data_page,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
