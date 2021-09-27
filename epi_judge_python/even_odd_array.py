import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# [0, 1, 2, 3, 4, 5, 6, 7, 8]
def even_odd(A: List[int]) -> None:
    start: int = 0
    end: int = len(A)-1

    while start < end:
        if is_even(A[start]):
            start += 1

            if is_odd(A[end]):
                end -= 1
        
            continue

        if is_even(A[end]):
            A = swap_values(start, end, A)

            start += 1
            end -= 1
        else:
            end -= 1

    return

def is_odd(number: int) -> bool:
    return number % 2 != 0

def is_even(number: int) -> bool:
    return number % 2 == 0

def swap_values(a: int, b: int, arr: List[int]) -> List[int]:
    tmp: int = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

    return arr 

    

@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))
