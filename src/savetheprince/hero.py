from savetheprince.maparea import AreaId


class Hero:

    def __init__(self, location: AreaId) -> None:
        self._location = location

    def location(self) -> AreaId:
        return self._location

    def move(self, destination: AreaId) -> None:
        pass
