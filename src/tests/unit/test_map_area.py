import unittest

from savetheprince.maparea import MapArea
from savetheprince.maparea import AreaId
from savetheprince.position import Position
from savetheprince.size import Size


class TestMapArea(unittest.TestCase):

    def test_finds_position_of_an_item_in_the_center(self) -> None:
        area = MapArea(AreaId('test-area'), Size(100, 100), Position(0, 0))
        self.assertEqual(area.centered(Size(10, 10)), Position(45, 45))

    def test_finds_absolute_position(self) -> None:
        area = MapArea(AreaId('test-area'), Size(100, 100), Position(15, 100))
        self.assertEqual(area.centered(Size(10, 10)), Position(60, 145))

