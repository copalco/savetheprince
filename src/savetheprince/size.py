from dataclasses import dataclass


@dataclass(frozen=True)
class Size:
    width: int
    height: int

    def half_width(self) -> int:
        return 25
