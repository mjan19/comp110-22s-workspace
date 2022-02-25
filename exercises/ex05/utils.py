"""Creating list utility functions."""


__author__ = 730510654


def only_evens(x: list[int]) -> list[int]:
    """Only returns the even numbers from a list."""
    result: list[int] = list()
    for i in x:
        if i % 2 == 0:
            result.append(i)
    print(result)
    return result


def sub(x: list[int], start: int, end: int) -> list[int]:
    """Only returns a subset from a list."""
    result: list[int] = list()
    while start < end:
        result.append(x[start])
        start += 1
    print(result)
    return result


def concat(first: list[int], second: list[int]) -> list[int]:
    result: list[int] = list()
    for i in first:
        result.append(i)
    for i in second:
        result.append(i)
    print(result)
    return result