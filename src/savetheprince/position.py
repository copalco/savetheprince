import typing

from savetheprince.vector import Vector


class Position(typing.NamedTuple):
    x: int
    y: int

    def moved_by(self, vector: Vector) -> 'Position':
        return Position(self.x + vector.width, self.y + vector.height)
