from fractions import Fraction
from typing import List, Union, Tuple


def sum(arg: Union[List, Tuple]) -> Union[int, Fraction]:
    total: int = 0

    for val in arg:
        total += val

    return abs(total)
