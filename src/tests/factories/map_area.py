from savetheprince.maparea import MapArea
from savetheprince.position import Position
from savetheprince.size import Size
from tests.factories.area_id import AreaIdFactory
from tests.factories.position import PositionFactory
from tests.factories.size import SizeFactory


class MapAreaFactory:

    @staticmethod
    def create(size: Size = None, position: Position = None) -> MapArea:
        size = size or SizeFactory.create()
        position = position or PositionFactory.create()
        return MapArea(
            id=AreaIdFactory.create(),
            size=size,
            position=position,
        )
