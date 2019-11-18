import random

from savetheprince.area import AreaId


class AreaIdFactory:

    @staticmethod
    def create() -> AreaId:
        return AreaId(random.choices('abcdefghijklmnopqrstuvwxyz', k=6))