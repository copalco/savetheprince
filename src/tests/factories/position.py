import random

from savetheprince.main import Position


class PositionFactory:

    @staticmethod
    def create() -> Position:
        return Position(x=random.randint(0, 10), y=random.randint(0, 10))