"""
Password validator classes
"""
import re


class PassValidator:
    """
    Base class for validators
    """

    re_string = r'^(?P<n1>\d+)-(?P<n2>\d+)\s+(?P<char>\w):\s+\w+$'

    @staticmethod
    def from_string(string: str):
        """
        Construct and return an instance from a line read from the input file
        """

    @staticmethod
    def match_line(string):
        """
        Match a line passed as argument with the input regex
        """
        regex = re.compile(PassValidator.re_string)
        return regex.match(string)

    def validate(self, password: str) -> bool:
        """
        Check if a password is valid
        """


class CountValidator(PassValidator):
    """
    Class that checks if a pasword has between N and M appearences of a given
    character.
    """
    @staticmethod
    def from_string(string: str):
        match = PassValidator.match_line(string)

        return CountValidator(
            int(match.group('n1')),
            int(match.group('n2')),
            match.group('char')
        )

    def __init__(self, min_appearences: int, max_appearences: int, letter: str):
        self._min_appearences = min_appearences
        self._max_appearences = max_appearences
        self._required_char = letter
        super().__init__()

    def _count_in_password(self, password: str) -> int:
        return password.count(self._required_char)

    def _validate_count(self, count: int) -> bool:
        return (
            self._min_appearences <= count <= self._max_appearences
        )

    def validate(self, password: str):
        number_of_times = self._count_in_password(password)
        is_valid = self._validate_count(number_of_times)
        return is_valid


class PositionValidator(PassValidator):
    """
    Class that checks if the given character appears in one, and only one, of
    a pair of positions
    """

    @staticmethod
    def from_string(string: str):
        match = PassValidator.match_line(string)

        return PositionValidator(
            int(match.group('n1')),
            int(match.group('n2')),
            match.group('char')
        )

    def __init__(self, position1: int, position2: int, letter: str):
        self._first_position = position1-1
        self._second_position = position2-1
        self._required_char = letter

    def validate(self, password: str):
        return ((password[self._first_position] == self._required_char)
                != (password[self._second_position] == self._required_char))
