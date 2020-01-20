import unittest

from savetheprince.displaying import ScaleRatio
from savetheprince.displaying import calculate_scale_ratio
from savetheprince.size import Size


class TestDisplay(unittest.TestCase):

    def test_calculates_scale_ratio(self) -> None:
        self.assertEqual(
            calculate_scale_ratio(Size(20, 10), Size(10, 5)),
            ScaleRatio(0.5, 0.5)
        )
        self.assertEqual(
            calculate_scale_ratio(Size(30, 10), Size(10, 5)),
            ScaleRatio(0.3333333333333333, 0.5)
        )
        self.assertEqual(
            calculate_scale_ratio(Size(20, 4), Size(20, 15)),
            ScaleRatio(1, 3.75)
        )
