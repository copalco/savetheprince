import unittest

from src.savetheprince.main import Circle
from src.savetheprince.main import Area
from src.savetheprince.main import Position
from src.savetheprince.main import Size


class TestCircle(unittest.TestCase):

    def test_returns_next_area(self) -> None:
        first_area = Area(Size(10, 10), Position(0, 0)),
        second_area = Area(Size(10, 10), Position(10, 0)),
        circle = Circle(
            first_area,
            second_area,
        )
        self.assertEqual(circle.next(first_area), second_area)