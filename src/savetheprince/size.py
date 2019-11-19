import math

from dataclasses import dataclass


@dataclass(frozen=True)
class Size:
    width: int
    height: int

    def half_width(self) -> int:
        return self._half_of(self.width)

    def half_height(self) -> int:
        return self._half_of(self.height)

    def _half_of(self, value: int) -> int:
        return math.ceil(value / 2)
