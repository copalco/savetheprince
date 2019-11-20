from savetheprince.area import Area
from tests.factories.area_id import AreaIdFactory


class AreaFactory:

    @staticmethod
    def create():
        return Area(AreaIdFactory.create())