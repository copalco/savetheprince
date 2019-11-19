import typing

from savetheprince.position import Position
from savetheprince.size import Size
from savetheprince.vector import Vector

AreaId = typing.NewType('AreaId', str)


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
        return self._position.moved_by(vector)
