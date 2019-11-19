import unittest

from savetheprince.game import Game


class TestGame(unittest.TestCase):

    def test_raises_movement_event(self) -> None:
        game = Game()
        game.move_left()
