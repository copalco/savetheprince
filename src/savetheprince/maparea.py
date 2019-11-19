import typing

from savetheprince.position import Position
from savetheprince.size import Size

AreaId = typing.NewType('AreaId', str)


class Vector:

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height


class MapArea:

    def __init__(self, id: AreaId, size: Size, position: Position):
        self.id = id
        self._size = size
        self._position = position

    def centered(self, size: Size) -> Position:
        vector = Vector(
            self._size.half_width() - size.half_width(),
            self._size.half_height() - size.half_height(),
        )
        return Position(
            vector.width + self._position.x,
            vector.height + self._position.y,
        )
