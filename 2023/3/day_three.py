import re


def part_one(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    start_scan_position = None
    end_scan_position = None
    current_number = ""
    number_regex = r"(\d+)"
    numbers = []
    row = 1
    last_row = lines.__len__()
    for line in lines:
        line_length = line.__len__()
        for index, char in enumerate(line):
            print(f"{line[:index]}X{line[index + 1:]}")
            match = re.search(number_regex, char)
            if match:
                if not current_number:
                    start_scan_position = max(index - 1, 0)

                current_number += match.group()
                if index + 1 == line_length:
                    # start scanning
                    print(
                        f"time to scan {current_number}, {line[index - 1]} in pos {index - 1}"
                    )
                    end_scan_position = min(index, line_length)

                    # Check left
                    if is_symbol(line[start_scan_position]):
                        print(
                            f"found symbol left {line[start_scan_position]}, {current_number}"
                        )

                        numbers.append(current_number)
                        current_number = ""
                        continue

                    # Check above
                    if row > 1:
                        previous_line = lines[row - 2]
                        for position in range(
                            start_scan_position, min(end_scan_position + 1, line_length)
                        ):
                            if is_symbol(previous_line[position]):
                                print(
                                    f"found symbol above {previous_line[position]}, {current_number}"
                                )
                                numbers.append(current_number)
                                current_number = ""
                                break

                    # Check right
                    if is_symbol(line[end_scan_position]):
                        print(
                            f"found symbol right {line[start_scan_position]}, {current_number}"
                        )
                        numbers.append(current_number)
                        current_number = ""
                        continue

                    # Check below
                    if row != last_row:
                        next_line = lines[row]
                        # scan from right to left to make it a pretty circle
                        for position in range(
                            end_scan_position, start_scan_position - 1, -1
                        ):
                            if is_symbol(next_line[position]):
                                print(
                                    f"found symbol below {next_line[position]}, {current_number}"
                                )
                                numbers.append(current_number)
                                current_number = ""
                                break

                    current_number = ""

            elif current_number:
                # start scanning
                print(
                    f"time to scan {current_number}, {line[index - 1]} in pos {index - 1}"
                )
                end_scan_position = min(index, line_length)
                # Check left
                if is_symbol(line[start_scan_position]):
                    print(
                        f"found symbol left {line[start_scan_position]}, {current_number}"
                    )

                    numbers.append(current_number)
                    current_number = ""
                    continue

                # Check above
                if row > 1:
                    previous_line = lines[row - 2]
                    for position in range(
                        start_scan_position, min(end_scan_position + 1, line_length)
                    ):
                        if is_symbol(previous_line[position]):
                            print(
                                f"found symbol above {previous_line[position]}, {current_number}"
                            )
                            numbers.append(current_number)
                            current_number = ""
                            break

                # Check right
                if is_symbol(line[end_scan_position]):
                    print(
                        f"found symbol right {line[start_scan_position]}, {current_number}"
                    )
                    numbers.append(current_number)
                    current_number = ""
                    continue

                # Check below
                if row != last_row:
                    next_line = lines[row]
                    # scan from right to left to make it a pretty circle
                    for position in range(
                        end_scan_position, start_scan_position - 1, -1
                    ):
                        if is_symbol(next_line[position]):
                            print(
                                f"found symbol below {next_line[position]}, {current_number}"
                            )
                            numbers.append(current_number)
                            current_number = ""
                            break

                current_number = ""
        row += 1

    sum = 0
    print(f"Numbers: {numbers}")
    for number in numbers:
        sum += int(number)

    return sum


def part_two(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    return "something"


def is_symbol(char):
    symbols = r"[^.^\d^\s]"
    match = re.search(symbols, char)
    if match:
        return True
    else:
        return False


if __name__ == "__main__":
    file_name = "input.txt"
    sum_part_one = part_one(file_name)
    sum_part_two = part_two(file_name)
    print(f"Sum of part one: {sum_part_one}, Sum of part two: {sum_part_two}")
