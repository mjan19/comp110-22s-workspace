"""Testing the list utility functions."""


__author__ = 730510654


from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    assert only_evens([]) == []


def test_only_evens_one_number() -> None:
    assert only_evens([2]) == [2]


def test_only_evens_multiple_numbers() -> None:
    assert only_evens([1, 2, 3, 4, 6, 4, 2]) == [2, 4, 6, 4, 2]


def test_sub_empty() -> None:
    assert sub([], 0, 0) == []


def test_sub_one_number() -> None:
    assert sub([1, 2], 0, 1) == [1]


def test_sub_multiple_numbers() -> None:
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_concat_empty() -> None:
    assert concat([], []) == []


def test_concat_one_list() -> None:
    assert concat([1, 2, 3], []) == [1, 2, 3]


def test_concat_both_lists() -> None:
    assert concat([10, 15, 20], [0, 5, 10]) == [10, 15, 20, 0, 5, 10]