from savetheprince.main import Area
from tests.factories.area_id import AreaIdFactory
from tests.factories.position import PositionFactory
from tests.factories.size import SizeFactory


class AreaFactory:

    @staticmethod
    def create() -> Area:
        return Area(
            id=AreaIdFactory.create(),
            size=SizeFactory.create(),
            position= PositionFactory.create(),
        )