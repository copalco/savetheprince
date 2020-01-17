import typing

from savetheprince.map_hero import MapHero
from savetheprince.maparea import AreaId
from savetheprince.maparea import MapArea
from savetheprince.position import Position


class MapAreaNotFound(Exception):

    pass


class Presenter:

    def __init__(self, *areas: MapArea) -> None:
        self._areas: typing.List[MapArea] = list(areas)

    def position_hero(self, hero: MapHero, area_id: AreaId) -> Position:
        return self._find_area(area_id).centered(hero.size())

    def _find_area(self, id: AreaId) -> MapArea:
        for area in self._areas:
            if area.id == id:
                return area
        raise MapAreaNotFound()
