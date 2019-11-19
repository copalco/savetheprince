import typing

from savetheprince.position import Position
from savetheprince.size import Size

AreaId = typing.NewType('AreaId', str)


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
        return Position(
            round(half_width - half_other_width) + self._position.x,
            round(half_height - half_other_height) + self._position.y,
        )
