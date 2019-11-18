from savetheprince.maparea import MapArea


class Presenter:

    def __init__(self, current_area: MapArea) -> None:
        self._current_hero_location: MapArea = current_area

    def store_hero_location(self, area: MapArea) -> None:
        self._current_hero_location = area

    def locate_hero(self) -> MapArea:
        return self._current_hero_location
