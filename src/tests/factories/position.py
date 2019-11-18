import random

from savetheprince.position import Position


class PositionFactory:

    @staticmethod
    def create() -> Position:
        return Position(x=random.randint(0, 10), y=random.randint(0, 10))