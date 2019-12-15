import unittest

from savetheprince.circle import Circle
from savetheprince.game import Game
from savetheprince.hero import Hero
from tests.factories.area_factory import AreaFactory


class TestGame(unittest.TestCase):

    def test_changes_hero_position(self) -> None:
        starting_area = AreaFactory.create()
        hero = Hero(location=starting_area.id)
        area_to_the_left = AreaFactory.create()
        game = Game(Circle(starting_area, area_to_the_left), hero)
        game.move_playing_hero_left()
