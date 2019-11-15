import unittest

from src.savetheprince.main import Area
from src.savetheprince.main import Position
from src.savetheprince.main import Size


class TestArea(unittest.TestCase):

    def test_get_center_returns_position_of_item_centered_inside(
            self) -> None:
        area = Area(Size(100, 100), Position(0, 0))
        self.assertEqual(area.get_centered(Size(10, 10)), Position(45, 45))

    def test_get_center_returns_absolute_position(self) -> None:
        area = Area(Size(100, 100), Position(15, 100))
        self.assertEqual(area.get_centered(Size(10, 10)), Position(60, 145))
