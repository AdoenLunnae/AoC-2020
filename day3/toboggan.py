from typing import Tuple


class Coordinates:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    def __iadd__(self, tup: Tuple[int]) -> 'Coordinates':
        return self + tup

    def __add__(self, tup: Tuple[int]) -> 'Coordinates':
        return Coordinates(self.x+tup[0], self.y+tup[1])

    def __eq__(self, coord: 'Coordinates') -> bool:
        return self.x == coord.x and self.y == coord.y


class Field:

    def __init__(self, trees):
        self.trees = trees
        self.height = len(self.trees)
        self.width = len(self.trees[0])

    @staticmethod
    def from_string(string) -> 'Field':
        content = [line for line in string.split('\n') if line]

        trees = [
            [(point == "#") for point in row]
            for row in content
        ]

        return Field(trees)

    def __getitem__(self, coord: Coordinates) -> bool:
        return self.trees[coord.x][coord.y % self.width]

    def has_tree_at(self, coord: Coordinates) -> bool:
        return self[coord]

    def is_at_bottom(self, coord: Coordinates) -> bool:
        return coord.x >= self.height


class Toboggan:

    def __init__(self, v_step: int = None, h_step: int = None):
        self.__v_step = v_step or 1
        self.__h_step = h_step or 3
        self._position = Coordinates(0, 0)

    @property
    def step(self) -> tuple:
        return (self.__v_step, self.__h_step)

    @property
    def pos(self) -> Coordinates:
        return self._position

    def advance(self):
        self._position += self.step

    def check_field(self, field):
        return field.has_tree_at(self.pos)

    def arrived(self, field):
        return field.is_at_bottom(self.pos)

    def traverse_and_count_trees(self, field):
        n_trees = 0

        while not self.arrived(field):
            n_trees += 1 if self.check_field(field) else 0
            self.advance()

        return n_trees
