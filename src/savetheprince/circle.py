from savetheprince.maparea import MapArea


class UnknownArea(Exception):

    pass


class Circle(object):

    def __init__(self, *areas: MapArea) -> None:
        self._areas = areas

    def next(self, current_area: MapArea) -> MapArea:
        for index, area in enumerate(self._areas):
            if area == current_area:
                try:
                    return self._areas[index + 1]
                except IndexError:
                    return self._areas[0]
        raise UnknownArea()

    def previous(self, current_area: MapArea) -> MapArea:
        for index, area in enumerate(self._areas):
            if area == current_area:
                return self._areas[index - 1]
        raise UnknownArea()