from savetheprince.size import Size


class MapHero:

    def __init__(self, size: Size) -> None:
        self._size = size

    @property
    def size(self) -> Size:
        return self._size
