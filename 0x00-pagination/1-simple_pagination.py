#!/usr/bin/env python3
"""Simple Pagination"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index
       and an end index corresponding to the range of indexes
       to return in a list for those particular pagination parameters.
    """
    end_index: int = page * page_size
    start_index: int = end_index - page_size

    return(start_index, end_index)


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
            pass

def get_page(page: int = 1, page_size: int = 10) -> List[List]:
    """ return the appropriate page of the dataset
       (i.e. the correct list of rows).
    """
    assert (page, int) and page > 0
    assert (page_size, int) and page > 0

    start_index: Tuple = index_range(page, page_size)
    end_index: Tuple = index_range(page, page_size)
    pages = self.dataset()

    return pages[start_index:end_index]
