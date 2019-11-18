import random

from savetheprince.main import Size


class SizeFactory:

    @staticmethod
    def create():
        return Size(width=random.randint(0, 10), height=random.randint(0, 10))