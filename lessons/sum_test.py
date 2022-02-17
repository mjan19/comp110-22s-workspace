"""Tests for the sum function."""


from lessons.sum import sum


def test_sum_empty() -> None:
    assert sum([]) == 0


def test_sum_single_item() -> None:
    assert sum([110]) == 110


def test_sum_many_items() -> None:
    assert sum([1, 2, 3]) == 6


def test_sum_many_items_again() -> None:
    assert sum([-1, 1, -2, 2]) == 0