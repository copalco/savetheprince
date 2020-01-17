import unittest

from savetheprince.map_hero import MapHero
from savetheprince.size import Size


class TestMapHero(unittest.TestCase):

    def test_map_hero_size(self) -> None:
        hero = MapHero(Size(10, 20))
        self.assertEqual(hero.size(), Size(10, 20))
