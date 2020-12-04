from toboggan import *
import unittest
from unittest.mock import MagicMock, patch, mock_open
from pytest import fixture, mark


@fixture(scope='class')
def fake_trees(request):
    return [
        [False, False, True, False],
        [False, False, False, False],
        [True, False, False, False],
        [True, True, False, True]
    ]


@fixture(scope='class')
def fake_tree_string(request):
    request.cls.fake_tree_string = "..#.\n....\n#...\n##.#\n"


class TestTobogganWhenConstructorIsCalled(unittest.TestCase):

    def test_it_instantiates_correctly(self):
        t = Toboggan()

        self.assertIsInstance(t, Toboggan)

    def test_its_coordinates_are_zero(self):
        t = Toboggan()

        self.assertEqual(t.pos, Coordinates(0, 0))

    def test_it_has_default_step(self):
        t = Toboggan()

        self.assertEqual(t.step, (1, 3))


class TestTobogganWhenAdvancing(unittest.TestCase):

    def test_its_position_changes_by_the_step(self):
        t = Toboggan()
        t.advance()

        self.assertEqual(t.pos, Coordinates(1, 3))


@mark.usefixtures("fake_trees", "fake_tree_string")
class TestFieldWhenConstructorIsCalled(unittest.TestCase):

    def test_the_trees_are_placed_correctly(self):
        mock_content = mock_open(read_data=self.fake_tree_string)

        with patch('__main__.open', mock_content) as fake_open:
            with fake_open('fake_file') as f:
                field = Field.from_string(f.read())

        self.assertListEqual(
            field.trees,
            self.fake_trees
        )

    def test_accessing_a_point_to_the_right_repeats_the_pattern(self):
        field = Field(self.fake_trees)

        self.assertTrue(field.has_tree_at(Coordinates(0, 6)))
