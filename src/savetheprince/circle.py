from savetheprince.area import Area
from savetheprince.area import Area
from savetheprince.area import Area
from savetheprince.area import Area
from savetheprince.area import Area


class UnknownArea(Exception):

    pass


class Circle(object):

    def __init__(self, *areas: Area) -> None:
        self._areas = areas

    def next(self, current_area: Area) -> Area:
        for index, area in enumerate(self._areas):
            if area == current_area:
                try:
                    return self._areas[index + 1]
                except IndexError:
                    return self._areas[0]
        raise UnknownArea()

    def previous(self, current_area: Area) -> Area:
        for index, area in enumerate(self._areas):
            if area == current_area:
                return self._areas[index - 1]
        raise UnknownArea()