#!/usr/bin/env python3
""" Hypermedia Pagination """
import csv
from math import ceil
from typing import Any, Dict, List, Tuple


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return the appropriate page of the dataset
           (i.e. the correct list of rows).
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        ranges: Tuple = index_range(page, page_size)
        pag: List = self.dataset()

        return (pag[ranges[0]:ranges[1]])

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """returns a dictionary with key-value pairs"""
        data = []
        try:
            data = self.get_page(page, page_size)
        except AssertionError:
            return {}

        dataset: List = self.dataset()
        total: int = len(dataset) if dataset else 0
        total = ceil(total / page_size)
        prevs: int = (page - 1) if (page - 1) >= 1 else None
        nexts: int = (page + 1) if (page + 1) <= total else None

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': nexts,
            'prev_page': prevs,
            'total_pages': total,
        }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.
    """
    end_index: int = page * page_size
    start_index: int = end_index - page_size

    return (start_index, end_index)
