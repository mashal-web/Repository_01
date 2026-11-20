"""Small, explicit unit-conversion helpers."""

MM_PER_M = 1000.0
CM_PER_M = 100.0
LITRES_PER_CUBIC_METRE = 1000.0


def mm_to_m(value: float) -> float:
    return value / MM_PER_M


def cm_to_m(value: float) -> float:
    return value / CM_PER_M


def m_to_mm(value: float) -> float:
    return value * MM_PER_M


def cubic_metres_to_litres(value: float) -> float:
    return value * LITRES_PER_CUBIC_METRE
