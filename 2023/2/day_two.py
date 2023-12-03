import re


def part_one(file_name, num_of_blue, num_of_red, num_of_green):
    file = open(file_name, "r")
    lines = file.readlines()
    games = []
    for line in lines:
        game = parse_game_line(line)
        if is_game_possible(num_of_blue, num_of_red, num_of_green, game):
            games.append(game.get("id"))

    return calculate_sum(games)


def part_two(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    sum = 0
    for line in lines:
        game = parse_game_line(line)
        sum += calculate_power(game)
    return sum


def parse_game_line(line: str):
    regex = r"Game (\d*):"
    game_id = int(re.split(regex, line)[1])
    line = re.sub(regex, "", line)
    rounds = line.split(";")
    info = {"id": game_id, "blue": 0, "red": 0, "green": 0}
    for round in rounds:
        stats = round.split(",")
        for stat in stats:
            stat = stat.strip()
            keys = stat.split(" ")
            value = int(keys[0])
            color = keys[1].strip()

            if info.get(color) < value:
                info.update({color: value})
    return info


def is_game_possible(num_of_blue, num_of_red, num_of_green, game: dict):
    if (
        game.get("blue") <= num_of_blue
        and game.get("red") <= num_of_red
        and game.get("green") <= num_of_green
    ):
        return game.get("id")
    return None


def calculate_power(game: dict):
    return game.get("blue") * game.get("red") * game.get("green")


def calculate_sum(ids: list):
    sum = 0
    for id in ids:
        sum += id

    return sum


if __name__ == "__main__":
    file_name = "input.txt"
    sum_part_one = part_one(file_name, num_of_blue=14, num_of_red=12, num_of_green=13)
    sum_part_two = part_two(file_name)
    print(f"Sum of part one: {sum_part_one}, Sum of part two: {sum_part_two}")
