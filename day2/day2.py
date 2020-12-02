"""
Day 2 of 2020 Advent of Code
"""

import sys
import re
from validator import CountValidator, PositionValidator


def pass_from_line(line: str):
    regex = re.compile(r'^\d+-\d+\s+\w:\s+(?P<password>\w+)$')
    match = regex.match(line)

    return match.group('password')


def count_valid(validators, passwords):
    return sum([1 for validator, password in zip(validators, passwords)
                if validator.validate(password)])


def silver(input_lines):
    validators = [CountValidator.from_string(line) for line in input_lines]
    passwords = [pass_from_line(line) for line in input_lines]

    return count_valid(validators, passwords)


def gold(input_lines):
    validators = [PositionValidator.from_string(line) for line in input_lines]
    passwords = [pass_from_line(line) for line in input_lines]

    return count_valid(validators, passwords)


def read_file(filename):
    with open(filename, 'r') as file:
        content = file.readlines()

    return content


def main():
    try:
        input_lines = read_file(
            input('Input file[input.txt]: ') or 'input.txt')
    except FileNotFoundError:
        print("Invalid input file")
        sys.exit(1)

    print(f'Silver star: {silver(input_lines)}')
    print(f'Gold star: {gold(input_lines)}')


if __name__ == '__main__':
    main()
