"""Basic concrete quantity calculations, not structural design checks."""

from civil_toolkit.core.validation import (
    require_finite_result,
    require_non_negative,
    require_positive,
)


def _rectangular_volume(
    first_m: float,
    second_m: float,
    third_m: float,
    first_name: str,
    second_name: str,
    third_name: str,
) -> float:
    """Calculate a rectangular-prism volume after validating its dimensions."""
    first = require_positive(first_m, first_name)
    second = require_positive(second_m, second_name)
    third = require_positive(third_m, third_name)
    return require_finite_result(first * second * third, "calculated volume_m3")


def slab_volume(length_m: float, width_m: float, thickness_m: float) -> float:
    """Calculate a rectangular slab's geometric volume in cubic metres."""
    return _rectangular_volume(
        length_m, width_m, thickness_m, "length_m", "width_m", "thickness_m"
    )


def beam_volume(length_m: float, width_m: float, depth_m: float) -> float:
    """Calculate a rectangular beam's geometric volume in cubic metres."""
    return _rectangular_volume(
        length_m, width_m, depth_m, "length_m", "width_m", "depth_m"
    )


def column_volume(height_m: float, width_m: float, depth_m: float) -> float:
    """Calculate a rectangular column's geometric volume in cubic metres."""
    return _rectangular_volume(
        height_m, width_m, depth_m, "height_m", "width_m", "depth_m"
    )


def volume_with_allowance(volume_m3: float, allowance_percent: float = 0.0) -> float:
    """Add a non-negative user-selected percentage allowance to a volume."""
    volume = require_non_negative(volume_m3, "volume_m3")
    allowance = require_non_negative(allowance_percent, "allowance_percent")
    result = volume * (1.0 + allowance / 100.0)
    return require_finite_result(result, "calculated volume_m3")
