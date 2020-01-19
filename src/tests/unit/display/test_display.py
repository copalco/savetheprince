import unittest

from savetheprince.displaying import ScaleRatio
from savetheprince.displaying import calculate_scale_ratio
from savetheprince.size import Size


class TestDisplay(unittest.TestCase):

    def test_calculates_scale_ratio(self) -> None:
        initial_size = Size(20, 10)
        final_size = Size(10, 5)
        self.assertEqual(
            calculate_scale_ratio(initial_size, final_size),
            ScaleRatio(0.5, 0.5)
        )
