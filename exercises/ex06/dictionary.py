"""Making Functions with Dictionaries."""


__author__ = "730510654"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Switches inputs to outputs and vice versa."""
    result = {}
    outputs = []
    for i in x:
        outputs.append(x[i])
    output_count = count(outputs)
    for i in output_count:
        if output_count[i] > 1:
            raise KeyError(f"{x[i]}")
    for i in x:
        result[x[i]] = i
    print(result)
    return result


def favorite_color(x: dict[str, str]) -> str:
    """Returns the color that appears most frequently in a dictionary."""
    favorite = ""
    colors = []
    for i in x:
        colors.append(x[i])
    # colors_count = count(colors)
    return favorite


def count(x: list[str]) -> dict[str, int]:
    """Produces a dictionary that counts the number of times a value appeared in the input list."""
    result = {}
    for i in x:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result