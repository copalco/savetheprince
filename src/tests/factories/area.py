from savetheprince.maparea import MapArea
from tests.factories.area_id import AreaIdFactory
from tests.factories.position import PositionFactory
from tests.factories.size import SizeFactory


class AreaFactory:

    @staticmethod
    def create() -> MapArea:
        return MapArea(
            id=AreaIdFactory.create(),
            size=SizeFactory.create(),
            position= PositionFactory.create(),
        )