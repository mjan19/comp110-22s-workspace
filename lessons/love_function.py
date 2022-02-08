"""Example of tender, loving function definition."""


def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}!"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = ""
    m: int = 0
    while m < n:
        m += 1
        love_note += love(to) + "\n"
    return love_note


def mystery(n: int) -> str:
    """A useless function."""
    i: int = 0
    while i < n:
        if i % 2 == 1:
            return "ooh"
        i += 1
    return "aah"


print(mystery(4))