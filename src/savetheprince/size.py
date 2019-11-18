from dataclasses import dataclass


@dataclass(frozen=True)
class Size:
    width: int
    height: int
