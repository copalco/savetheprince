from savetheprince.area import Area
from savetheprince.maparea import AreaId


class UnknownArea(Exception):

    pass


class Circle(object):

    def __init__(self, *areas: Area) -> None:
        self._areas = areas

    def next(self, area_id: AreaId) -> Area:
        for index, area in enumerate(self._areas):
            if area.id == area_id:
                try:
                    return self._areas[index + 1]
                except IndexError:
                    return self._areas[0]
        raise UnknownArea()

    def previous(self, area_id: AreaId) -> Area:
        for index, area in enumerate(self._areas):
            if area.id == area_id:
                return self._areas[index - 1]
        raise UnknownArea()
