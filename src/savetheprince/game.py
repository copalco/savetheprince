from savetheprince.circle import Circle
from savetheprince.hero import Hero


class Game:

    def __init__(self, circle: Circle, hero: Hero) -> None:
        self._circle = circle
        self._hero = hero

    def move_left(self) -> None:
        pass
