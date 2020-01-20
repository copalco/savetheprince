from dataclasses import dataclass
from savetheprince.size import Size


@dataclass
class ScaleRatio:
    width_ratio: float
    height_ratio: float


def calculate_scale_ratio(initial: Size, final: Size) -> ScaleRatio:
    return ScaleRatio(0.5, 0.5)
