import random

from savetheprince.main import AreaId


class AreaIdFactory:

    @staticmethod
    def create() -> AreaId:
        return AreaId(random.choices('abcdefghijklmnopqrstuvwxyz', k=6))