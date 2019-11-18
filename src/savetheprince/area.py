import typing

from savetheprince.position import Position
from savetheprince.size import Size

AreaId = typing.NewType('AreaId', str)


class Area:

    def __init__(self, id: AreaId, size: Size, position: Position):
        self.id = id
        self._size = size
        self._position = position

    def centered(self, size: Size) -> Position:
        half_width = self._size.width / 2.0
        half_height = self._size.height / 2.0
        half_other_width = size.width / 2.0
        half_other_height = size.height / 2.0
        return Position(
            round(half_width - half_other_width) + self._position.x,
            round(half_height - half_other_height) + self._position.y,
        )
