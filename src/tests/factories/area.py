from savetheprince.main import Area
from tests.factories.position import PositionFactory
from tests.factories.size import SizeFactory


class AreaFactory:

    @staticmethod
    def create() -> Area:
        return Area(
            size=SizeFactory.create(),
            position= PositionFactory.create(),
        )