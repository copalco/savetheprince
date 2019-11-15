import unittest

from savetheprince.main import get_center



class TestCenteringRectangles(unittest.TestCase):

    def test_finds_position_to_center_one_area_on_another(self) -> None:
        first_area = (100, 100)
        second_area = (10, 10)
        self.assertEqual(get_center(first_area, second_area), (45, 45))
