"""Validated unit conversions for common length and volume units."""

from civil_toolkit.core.validation import require_finite_result, require_non_negative

MM_PER_M = 1000.0
CM_PER_M = 100.0
LITRES_PER_CUBIC_METRE = 1000.0


def mm_to_m(value: float) -> float:
    """Convert a non-negative length from millimetres to metres."""
    result = require_non_negative(value, "value") / MM_PER_M
    return require_finite_result(result, "converted value")


def cm_to_m(value: float) -> float:
    """Convert a non-negative length from centimetres to metres."""
    result = require_non_negative(value, "value") / CM_PER_M
    return require_finite_result(result, "converted value")


def m_to_mm(value: float) -> float:
    """Convert a non-negative length from metres to millimetres."""
    result = require_non_negative(value, "value") * MM_PER_M
    return require_finite_result(result, "converted value")


def cubic_metres_to_litres(value: float) -> float:
    """Convert a non-negative volume from cubic metres to litres."""
    result = require_non_negative(value, "value") * LITRES_PER_CUBIC_METRE
    return require_finite_result(result, "converted value")
