"""Theoretical reinforcement bar weight estimates."""
from dataclasses import dataclass
from civil_toolkit.core.validation import require_finite_result, require_non_negative, require_positive

@dataclass(frozen=True)
class BarBatch:
    diameter_mm: float
    count: int
    length_each_m: float
    total_length_m: float
    theoretical_weight_kg: float

def bar_weight(diameter_mm: float, length_m: float) -> float:
    """Approximate theoretical mass: d²/162 × L, d in mm and L in m."""
    d=require_positive(diameter_mm,"diameter_mm")
    length=require_non_negative(length_m,"length_m")
    return require_finite_result((d*d/162.0)*length,"theoretical_weight_kg")

def total_bar_weight(diameter_mm: float, length_m: float, number_of_bars: int = 1) -> float:
    if isinstance(number_of_bars,bool) or not isinstance(number_of_bars,int) or number_of_bars<0:
        raise ValueError("number_of_bars must be a non-negative integer.")
    return require_finite_result(bar_weight(diameter_mm,length_m)*number_of_bars,"theoretical_weight_kg")

def multiple_bar_weights(specifications: list[tuple[float,int,float]]) -> list[BarBatch]:
    """Calculate batches supplied as (diameter_mm, count, length_each_m)."""
    batches=[]
    for d,count,length in specifications:
        if isinstance(count,bool) or not isinstance(count,int) or count<0:
            raise ValueError("bar count must be a non-negative integer.")
        each=require_non_negative(length,"length_each_m")
        total=require_finite_result(count*each,"total_length_m")
        batches.append(BarBatch(d,count,each,total,total_bar_weight(d,each,count)))
    return batches
