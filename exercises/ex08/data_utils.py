"""Dictionary related utility functions."""

__author__ = "730510654"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the files
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N row of data for each column."""
    result: dict[str, list[str]] = {}
    for x in table:
        column: list[str] = []
        i = 0
        while i < N:
            column.append(table[x][i])
            i += 1
            if N > len(table[x]):
                return table
        result[x] = column
    return result


def select(x: dict[str, list[str]], y: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for i in y:
        result[i] = x[i]
    return result


def concat(x: dict[str, list[str]], y: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for i in x:
        result[i] = x[i]

    for i in y:
        if i in result:
            number = 0
            for j in y[i]:
                result[i].append(y[i][number])
                number += 1
        else:
            result[i] = y[i]
    return result


def count(x: list[str]) -> dict[str, int]:
    """Given a `list[str]`, this function will produce a `dict[str, int]` where each key is a unique value in the given list and each value associated is the _count_ of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for i in x:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result


def percentage(input: list[str], total: int) -> dict[str, float]:
    """Given a list[str], produce a new table (dict[str, float]) where each key is a unique value in the given list and each value associated is the percentage of the number of times that value appeared."""
    result: dict[str, float] = {}
    table = count(input)
    for i in table:
        percent = table[i] / total * 100
        result[i] = percent
    return result