import random

from savetheprince.maparea import AreaId


class AreaIdFactory:

    @staticmethod
    def create() -> AreaId:
        return AreaId(
            ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=6))
        )
