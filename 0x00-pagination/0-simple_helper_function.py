#!/usr/bin/env python3

"""
Module describes a function that takes two integer arguments.

The function should return a tuple of size two containing a start index
and an end index corresponing to the range of indexes to return in a list
for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """Returns a tuple of size two containing a start index and end index."""

    return (page - 1) * page_size, page * page_size
