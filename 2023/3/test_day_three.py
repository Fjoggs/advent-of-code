import pytest
from day_three import (
    part_one,
    is_symbol,
)


@pytest.mark.parametrize(
    "input, expected",
    [
        ("3/test_input.txt", 4361),
        ("3/test_input_2.txt", 62),
        ("3/test_input_3.txt", 4),
        ("3/test_input_4.txt", 413),
        ("3/test_input_5.txt", 925),
        ("3/test_input_6.txt", 423),
        # ("3/input.txt", 531561),
    ],
)
def test_part_one(input, expected):
    actual = part_one(input)
    assert actual == expected


# @pytest.mark.parametrize("input, expected", [("3/test_input.txt", 2286)])
# def test_part_two(input, expected):
#     actual = part_two(input)
#     assert actual == expected


@pytest.mark.parametrize(
    "char, expected",
    [
        (".", False),
        ("1", False),
        ("$", True),
        ("#", True),
        ("*", True),
        ("+", True),
        ("", False),
        (" ", False),
        ("\n", False),
    ],
)
def test_is_symbol(char, expected):
    actual = is_symbol(char)
    assert actual == expected
