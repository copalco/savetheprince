import unittest

from savetheprince.hero import Hero
from tests.factories.area_id import AreaIdFactory


class TestHero(unittest.TestCase):

    def test_is_aware_of_location(self) -> None:
        area_id = AreaIdFactory.create()
        hero = Hero(location=area_id)
        self.assertEqual(hero.location(), area_id)

    def test_hero_moves_to_another_location(self) -> None:
        area_id = AreaIdFactory.create()
        destination_area_id = AreaIdFactory.create()
        hero = Hero(location=area_id)
        hero.move(destination=destination_area_id)
        self.assertEqual(hero.location(), area_id)
