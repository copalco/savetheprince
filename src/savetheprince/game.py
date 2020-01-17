from savetheprince.circle import Circle
from savetheprince.hero import Hero


class Game:

    def __init__(self, circle: Circle, hero: Hero) -> None:
        self._circle = circle
        self._hero = hero

    def move_playing_hero_left(self) -> None:
        area = self._circle.previous(self._hero.location())
        self._hero.move(area.id)
