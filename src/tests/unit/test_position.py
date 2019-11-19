import unittest

from savetheprince.position import Position
from savetheprince.vector import Vector


class TestPosition(unittest.TestCase):

    def test_can_be_moved_by_vector(self) -> None:
        self.assertEqual(
            Position(10, 20).moved_by(Vector(5, 6)),
            Position(15, 26),
        )