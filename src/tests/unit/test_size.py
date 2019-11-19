import unittest

from savetheprince.size import Size


class TestSize(unittest.TestCase):

    def test_tells_the_half_of_its_width(self) -> None:
        self.assertEqual(Size(50, 20).half_width(), 25)

    def test_rounds_the_half_width(self) -> None:
        self.assertEqual(Size(5, 20).half_width(), 3)

    def test_tells_the_half_of_its_height(self) -> None:
        self.assertEqual(Size(20, 50).half_height(), 25)

    def test_rounds_the_half_height(self) -> None:
        self.assertEqual(Size(20, 5).half_height(), 3)
