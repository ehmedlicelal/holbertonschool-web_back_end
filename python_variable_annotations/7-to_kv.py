#!/usr/bin/env python3

"""Module that defines to_kv function."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with the string k and the square of v as a float."""
    return (k, float(v ** 2))
