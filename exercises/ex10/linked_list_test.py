"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730510654"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_out() -> None:
    """Value_at of an empty Linked List should raise a IndexError."""
    with pytest.raises(IndexError):
        value_at(Node(10, Node(20, Node(30, None))), 3)


def test_value_at_non_empty() -> None:
    """Value_at of a non-empty list should return the data of the Node at the given index."""
    assert value_at(Node(10, Node(20, Node(30, None))), 2) == 30


def test_max_empty() -> None:
    """Max of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        max(None)


def test_max_non_empty() -> None:
    """Max of a non-empty list should return the maximum data value in the linked list."""
    assert max(Node(10, Node(30, Node(20, None)))) == 30


def test_linkify_empty() -> None:
    """Linkify of an empty list should raise a ValueError."""
    with pytest.raises(ValueError):
        linkify([])


def test_linkify_non_empty() -> None:
    """Linkify of a non-empty list should return a Linked List of Nodes with the same values."""
    assert linkify([1, 2, 3]) == "1 -> 2 -> 3 -> None"


def test_scale_empty() -> None:
    """Scale of an empty list should raise a ValueError."""
    with pytest.raises(ValueError):
        scale(None, 0)


def test_scale_non_empty() -> None:
    """Scale of a non-empty list should return a new linked list of Nodes where each value in the original list is scaled by the factor."""
    assert scale(linkify([1, 2, 3]), 2) == "2 -> 4 -> 6 -> None"
