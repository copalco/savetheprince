import unittest

from savetheprince.area import Area
from savetheprince.area import AreaId
from savetheprince.position import Position
from savetheprince.size import Size


class TestArea(unittest.TestCase):

    def test_center_returns_position_of_item_centered_inside(
            self) -> None:
        area = Area(AreaId('test-area'), Size(100, 100), Position(0, 0))
        self.assertEqual(area.centered(Size(10, 10)), Position(45, 45))

    def test_center_returns_absolute_position(self) -> None:
        area = Area(AreaId('test-area'), Size(100, 100), Position(15, 100))
        self.assertEqual(area.centered(Size(10, 10)), Position(60, 145))
