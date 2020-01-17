from savetheprince.size import Size


class MapHero:

    def __init__(self, size: Size) -> None:
        self._size = size

    def size(self) -> Size:
        return self._size
