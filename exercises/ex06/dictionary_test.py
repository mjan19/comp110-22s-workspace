"""Testing the Dictionary Functions."""


__author__ = "730510654"


from dictionary import invert, favorite_color, count 


def test_invert_empty() -> None:
    """Tests invert function with empty dictionary."""
    assert invert({}) == {}


def test_invert_stuff() -> None:
    """Tests invert function with stuff in dictionary."""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_multiple() -> None:
    """Tests invert function with multiple stuff in dictionary."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_favorite_color_empty() -> None:
    """Tests favorite color functions with empty dictionary."""
    assert favorite_color({}) == ""


def test_favorite_color_stuff() -> None:
    """Tests favorite colors function with stuff in dictionary."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_favorite_color_tied() -> None:
    """Tests favorite colors function with a tie."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Jan": "yellow"}) == "yellow"


def test_count_empty() -> None:
    """Tests count function with an empty list."""
    assert count([]) == {}


def test_count_stuff() -> None:
    """Tests count function with stuff in list."""
    assert count(["tar", "heels"]) == {"tar": 1, "heels": 1}


def test_count_multiples() -> None:
    """Tests count function with multiple of the same keys in list."""
    assert count(["tar", "heels", "tar", "heels"]) == {"tar": 2, "heels": 2}