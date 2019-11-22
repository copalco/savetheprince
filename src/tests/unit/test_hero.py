import unittest

from savetheprince.hero import Hero
from tests.factories.area_id import AreaIdFactory


class TestHero(unittest.TestCase):

    def test_is_aware_of_location(self) -> None:
        area_id = AreaIdFactory.create()
        Hero(location=area_id)
