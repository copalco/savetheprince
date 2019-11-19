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
        half_width = self._size.half_width()
        half_height = self._size.half_height()
        half_other_width = size.half_width()
        half_other_height = size.half_height()
        vector_width = half_width - half_other_width
        vector_height = half_height - half_other_height
        vector = Vector(vector_width, vector_height)
        return Position(
            vector.width + self._position.x,
            vector.height + self._position.y,
        )
