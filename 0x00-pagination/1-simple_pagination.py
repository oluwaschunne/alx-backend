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

    @staticmethod
    def index_range(page: int, page_size: int) -> tuple:
        """Return a tuple of start and end indices for a given page & page size
        """
        if page <= 0 or page_size <= 0:
            raise ValueError("Page and page_size must be positive integers.")

        start_index = (page - 1) * page_size
        end_index = page * page_size

        return start_index, end_index

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a specific page of the dataset
        """
        assert isinstance(
            page, int) and page > 0, "Page must be an integer greater than 0"
        assert isinstance(
            page_size, int) and page_size > 0, "Page size an integer > 0"

        total_pages = math.ceil(len(self.dataset()) / page_size)

        if page > total_pages:
            return []

        start_index, end_index = self.index_range(page, page_size)
        return self.dataset()[start_index:end_index]
