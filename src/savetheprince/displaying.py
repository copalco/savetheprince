from dataclasses import dataclass
from savetheprince.size import Size


@dataclass
class ScaleRatio:
    width_ratio: float
    height_ratio: float


def calculate_scale_ratio(initial: Size, final: Size) -> ScaleRatio:
    width_ratio = final.width / initial.width
    return ScaleRatio(width_ratio, 0.5)
