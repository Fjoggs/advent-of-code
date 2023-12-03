import pytest
from day_one import (
    part_one,
    part_two,
    find_numbers,
    calculate_sum,
    find_numbers_part_two,
)


def test_part_one():
    actual = part_one("1/test_input.txt")
    expected = 142
    assert actual == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("1/test_input_2.txt", 281),
        ("1/test_input_3.txt", 371),
        ("1/input.txt", 55652),
    ],
)
def test_part_two_part_two(input, expected):
    actual = part_two(input)
    assert actual == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7chet", 77),
        ("219", 29),
        ("8wo3", 83),
        ("abc123xyz", 13),
        ("x2ne34", 24),
        ("49872", 42),
        ("z1ight234", 14),
        ("7pqrst6teen", 76),
        ("24", 24),
        ("123456789", 19),
        ("995vnbrrfrfj52", 92),
        ("1ight", 11),
        ("abc2x31ight", 21),
    ],
)
def test_find_numbers(input, expected):
    actual = find_numbers(input)
    assert actual == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
        ("twofour", 24),
        ("onetwothreefourfivesixseveneightnine", 19),
        ("9ninefivevnbrrfrfjfivetwo", 92),
        ("oneight", 18),
        ("2oneight", 28),
        ("abc2x3oneight", 28),
        ("fivethreeonezblqnsfk1", 51),
        ("two74119onebtqgnine", 29),
        ("jrjh5vsrxbhsfour3", 53),
        ("tn5eightfncnzcdtthree8", 58),
        ("kpmrk5flx", 55),
        ("fkxxqxdfsixgthreepvzjxrkcfk6twofour", 64),
        ("dqbx6six5twoone", 61),
        ("treb7uchet", 77),
        ("foursixtwoninevtzzgntnlg6oneightbxp", 48),
        ("sevenine", 79),
        ("sevenineseven", 77),
        ("797", 77),
        ("asdfoneight", 18),
        ("oneone", 11),
        ("fiveight", 58),
        ("1threegkhpq7nfrksvm69nxpvgvthfzoneighttc", 18),
        ("seightninepjr3mjkgq3ckxzlqkkxpxdpkk", 83),
        ("nsmlqsixfiveng65jjblflfone", 61),
    ],
)
def test_find_numbers_part_two_part_two(input, expected):
    actual = find_numbers_part_two(input)
    assert actual == expected


def test_calculate_sum():
    input = [12, 38, 15, 77]
    expected = 142
    actual = calculate_sum(input)
    assert actual == expected
