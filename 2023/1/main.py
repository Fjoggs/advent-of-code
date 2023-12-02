import regex


def part_one(file_name):
    file = open(file_name, "r")
    lines = file.readlines()

    numbers = []
    for line in lines:
        if line:
            number = find_numbers(line)
            if number:
                numbers.append(number)

    return calculate_sum(numbers)


def part_two(file_name):
    file = open(file_name, "r")
    lines = file.readlines()

    numbers = []
    for line in lines:
        if line:
            number = find_numbers_part_two(line)
            if number:
                numbers.append(number)

    return calculate_sum(numbers)


def find_numbers(line):
    numbers = ""
    first_number = ""
    last_number = ""
    for char in line:
        if char.isdigit():
            if first_number == "":
                first_number = char
            else:
                last_number = char

    if not last_number:
        last_number = first_number

    numbers = first_number + last_number
    return int(numbers) if numbers.isdigit() else None


def find_numbers_part_two(line):
    mapping_table = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
    }
    regex_statement = r"\d|one|two|three|four|five|six|seven|eight|nine"
    matches = regex.findall(regex_statement, line, overlapped=True)
    first_number = None
    last_number = None

    if matches:
        first_number = mapping_table.get(matches[0])
        last_number = mapping_table.get(matches[matches.__len__() - 1])
        numbers = first_number + last_number

    return int(numbers)


def calculate_sum(numbers):
    sum = 0
    for number in numbers:
        sum += number

    return sum


if __name__ == "__main__":
    sum_part_one = part_one("input.txt")
    sum_part_two = part_two("input.txt")
    print(f"Sum part one: {sum_part_one}, Sum part two: {sum_part_two}")
