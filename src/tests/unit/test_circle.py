import unittest

from savetheprince.circle import Circle
from savetheprince.circle import UnknownArea
from tests.factories.map_area import MapAreaFactory


class TestCircle(unittest.TestCase):

    def test_returns_next_area(self) -> None:
        first_area = MapAreaFactory.create()
        last_area = MapAreaFactory.create()
        circle = Circle(
            first_area,
            last_area,
        )
        self.assertEqual(circle.next(first_area), last_area)

    def test_if_last_area_return_first_as_next(self) -> None:
        first_area = MapAreaFactory.create()
        last_area = MapAreaFactory.create()
        circle = Circle(
            first_area,
            last_area
        )
        self.assertEqual(circle.next(last_area), first_area)

    def test_next_raises_unknown_area_error_if_area_not_within_cicle(
            self) -> None:
        circle = Circle(
            MapAreaFactory.create(),
        )
        with self.assertRaises(UnknownArea):
            circle.next(MapAreaFactory.create())

    def test_previous_returns_area_previous_to_the_given(self) -> None:
        first_area = MapAreaFactory.create()
        last_area = MapAreaFactory.create()
        circle = Circle(
            first_area,
            last_area
        )
        self.assertEqual(circle.previous(last_area), first_area)

    def test_previous_returns_last_area_if_first_is_given(self) -> None:
        first_area = MapAreaFactory.create()
        last_area = MapAreaFactory.create()
        circle = Circle(
            first_area,
            last_area,
        )
        self.assertEqual(circle.previous(first_area), last_area)

    def test_previous_raises_unknown_area_error_if_area_not_within_cicle(
            self) -> None:
        circle = Circle(
            MapAreaFactory.create(),
        )
        with self.assertRaises(UnknownArea):
            circle.previous(MapAreaFactory.create())
