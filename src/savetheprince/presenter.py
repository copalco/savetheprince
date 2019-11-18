from savetheprince.area import Area


class Presenter:

    def __init__(self, current_area: Area) -> None:
        self._current_hero_location: Area = current_area

    def store_hero_location(self, area: Area) -> None:
        self._current_hero_location = area

    def locate_hero(self) -> Area:
        return self._current_hero_location
