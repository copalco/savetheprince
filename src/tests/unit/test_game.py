import unittest

from savetheprince.circle import Circle
from savetheprince.game import Game
from tests.factories.area_factory import AreaFactory


class TestGame(unittest.TestCase):

    def test_raises_movement_event(self) -> None:
        area_to_the_left = AreaFactory.create()
        game = Game(Circle(AreaFactory.create(), area_to_the_left))
        game.move_left()
