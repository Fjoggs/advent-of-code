import pytest
from unittest import TestCase
from day_two import (
    part_one,
    part_two,
    parse_game_line,
    is_game_possible,
    calculate_sum,
    calculate_power,
)


def test_part_one():
    actual = part_one(
        "2/test_input.txt", num_of_blue=14, num_of_red=12, num_of_green=13
    )
    expected = 8
    assert actual == expected


@pytest.mark.parametrize(
    "input, expected", [("2/test_input.txt", 2286), ("2/input.txt", 86036)]
)
def test_part_two(input, expected):
    actual = part_two(input)
    assert actual == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            dict({"id": 1, "blue": 6, "red": 4, "green": 2}),
        ),
        (
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            dict({"id": 2, "blue": 4, "red": 1, "green": 3}),
        ),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            dict({"id": 3, "blue": 6, "red": 20, "green": 13}),
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            dict({"id": 4, "blue": 15, "red": 14, "green": 3}),
        ),
        (
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            dict({"id": 5, "blue": 2, "red": 6, "green": 3}),
        ),
        (
            "Game 6: 6 red, 1 blue, 3 green; 2 blue, 1 red; 4 green",
            dict({"id": 6, "blue": 2, "red": 6, "green": 4}),
        ),
    ],
)
def test_parse_game_line(input, expected):
    actual = parse_game_line(input)
    TestCase().assertDictEqual(actual, expected)


@pytest.mark.parametrize(
    "num_of_blue, num_of_red, num_of_green, game, expected",
    [
        (14, 12, 13, dict({"id": 1, "blue": 6, "red": 4, "green": 2}), 1),
        (14, 12, 13, dict({"id": 2, "blue": 4, "red": 1, "green": 3}), 2),
        (14, 12, 13, dict({"id": 3, "blue": 6, "red": 20, "green": 13}), None),
        (14, 12, 13, dict({"id": 4, "blue": 15, "red": 14, "green": 3}), None),
        (14, 12, 13, dict({"id": 5, "blue": 2, "red": 6, "green": 3}), 5),
        (14, 12, 13, dict({"id": 10, "blue": 2, "red": 6, "green": 3}), 10),
        (14, 12, 13, dict({"id": 100, "blue": 2, "red": 6, "green": 3}), 100),
    ],
)
def test_is_game_possible(num_of_blue, num_of_red, num_of_green, game, expected):
    actual = is_game_possible(num_of_blue, num_of_red, num_of_green, game)
    assert actual == expected


@pytest.mark.parametrize(
    "game, expected",
    [
        (dict({"id": 1, "blue": 6, "red": 4, "green": 2}), 48),
        (dict({"id": 2, "blue": 4, "red": 1, "green": 3}), 12),
        (dict({"id": 3, "blue": 6, "red": 20, "green": 13}), 1560),
        (dict({"id": 4, "blue": 15, "red": 14, "green": 3}), 630),
        (dict({"id": 5, "blue": 2, "red": 6, "green": 3}), 36),
    ],
)
def test_calculate_power(game, expected):
    actual = calculate_power(game)
    assert actual == expected


def test_calculate_sum():
    input = [1, 2, 5]
    expected = 8
    actual = calculate_sum(input)
    assert actual == expected
