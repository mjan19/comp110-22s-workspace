"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730510654"


class Simpy:
    """Like Numpy, but more simple."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize the `values` attribute of the newly constructed `Simpy` object to the argument passed in."""
        self.values = values

    def __str__(self) -> str:
        """Returns a str representation."""
        return f"Simpy({self.values})"

    def fill(self, filling: float, amount: int) -> None:
        """_fill_ a `Simpy`'s `values` with a specific number of repeating values."""
        i = 0
        self.values = []
        while i < amount:
            self.values.append(filling)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the `values` attribute with range of values, like the `range` built-in function, but in terms of `float`s."""
        assert step != 0.0
        self.values = []
        while abs(start) < abs(stop):
            self.values.append(start)
            start += step

    def sum(self) -> float:
        """Compute and return the sum of all items in the `values` attribute."""
        total = 0.0
        for values in self.values:
            total += values
        return total

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Create a new Simpy object that adds either two Simpy objects or a Simpy object and a float."""
        result = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        elif isinstance(rhs, float):
            for item in self.values:
                result.values.append(item + rhs)
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add the ability to use the _power operator_ (`**`) in conjunction with `Simpy` objects and floats."""
        result = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        elif isinstance(rhs, float):
            for item in self.values:
                result.values.append(item ** rhs)
        return result
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produce a _mask_, or a `list[bool]`, based on the equality of each item in the `values` attribute with some other `Simpy` object or a `float` value."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i = 0
            while i < len(self.values):
                result.append(self.values[i] == rhs.values[i])
                i += 1
        elif isinstance(rhs, float):
            for item in self.values:
                result.append(item == rhs)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produce a _mask_, or a `list[bool]`, based on the greater than relationship between each item in the `values` attribute with some other `Simpy` object or a `float` value."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i = 0
            while i < len(self.values):
                result.append(self.values[i] > rhs.values[i])
                i += 1
        elif isinstance(rhs, float):
            for item in self.values:
                result.append(item > rhs)
        return result        

    def __getitem__(self, index: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overload the subscription notation."""
        if isinstance(index, int):
            return self.values[index]
        else:
            i = 0
            result: Simpy = Simpy([])
            while i < len(self.values):
                if index[i]:
                    result.values.append(self.values[i])
                i += 1
            return result