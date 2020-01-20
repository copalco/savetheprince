import unittest

from savetheprince.displaying import ScaleRatio
from savetheprince.displaying import calculate_scale_ratio
from savetheprince.size import Size


class TestDisplay(unittest.TestCase):

    def test_calculates_scale_ratio(self) -> None:
        cases = (
            (Size(20, 10), Size(10, 5), ScaleRatio(0.5, 0.5)),
            (Size(30, 10), Size(10, 5), ScaleRatio(0.3333333333333333, 0.5)),
            (Size(20, 4), Size(20, 15), ScaleRatio(1, 3.75)),
        )
        for initial_size, final_size, scale_ratio in cases:
            with self.subTest(
                    initial_size=initial_size,
                    final_size=final_size,
                    scale_ratio=scale_ratio):
                self.assertEqual(
                    calculate_scale_ratio(initial_size, final_size),
                    scale_ratio,
                )
