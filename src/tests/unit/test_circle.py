import unittest

from savetheprince.main import Circle
from savetheprince.main import Area
from savetheprince.main import Position
from savetheprince.main import Size
from savetheprince.main import UnknownArea


class TestCircle(unittest.TestCase):

    def test_returns_next_area(self) -> None:
        first_area = Area(Size(10, 10), Position(0, 0)),
        last_area = Area(Size(10, 10), Position(10, 0)),
        circle = Circle(
            first_area,
            last_area,
        )
        self.assertEqual(circle.next(first_area), last_area)

    def test_if_last_area_return_first_as_next(self) -> None:
        first_area = Area(Size(10, 10), Position(0, 0)),
        last_area = Area(Size(10, 10), Position(10, 0)),
        circle = Circle(
            first_area,
            last_area
        )
        self.assertEqual(circle.next(last_area), first_area)

    def test_next_raises_unknown_area_error_if_area_not_within_cicle(
            self) -> None:
        circle = Circle(
            Area(Size(10, 10), Position(0, 0)),
        )
        with self.assertRaises(UnknownArea):
            circle.next(Area(Size(10, 10), Position(10, 0)))

    def test_previous_returns_area_previous_to_the_given(self) -> None:
        first_area = Area(Size(10, 10), Position(0, 0)),
        last_area = Area(Size(10, 10), Position(10, 0)),
        circle = Circle(
            first_area,
            last_area
        )
        self.assertEqual(circle.previous(last_area), first_area)

    def test_previous_returns_last_area_if_first_is_given(self) -> None:
        first_area = Area(Size(10, 10), Position(0, 0)),
        last_area = Area(Size(10, 10), Position(10, 0)),
        circle = Circle(
            first_area,
            last_area,
        )
        self.assertEqual(circle.previous(first_area), last_area)

    def test_previous_raises_unknown_area_error_if_area_not_within_cicle(
            self) -> None:
        circle = Circle(
            Area(Size(10, 10), Position(0, 0)),
        )
        with self.assertRaises(UnknownArea):
            circle.previous(Area(Size(10, 10), Position(10, 0)))
