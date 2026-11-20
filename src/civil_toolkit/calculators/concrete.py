"""Basic concrete quantity calculations.

These are quantity-estimation helpers, not structural design calculations.
"""

from civil_toolkit.core.validation import require_non_negative, require_positive


def slab_volume(length_m: float, width_m: float, thickness_m: float) -> float:
    """Calculate a rectangular slab's geometric volume in cubic metres."""
    length = require_positive(length_m, "length_m")
    width = require_positive(width_m, "width_m")
    thickness = require_positive(thickness_m, "thickness_m")
    return length * width * thickness


def beam_volume(length_m: float, width_m: float, depth_m: float) -> float:
    """Calculate a rectangular beam's geometric volume in cubic metres."""
    length = require_positive(length_m, "length_m")
    width = require_positive(width_m, "width_m")
    depth = require_positive(depth_m, "depth_m")
    return length * width * depth


def column_volume(height_m: float, width_m: float, depth_m: float) -> float:
    """Calculate a rectangular column's geometric volume in cubic metres."""
    height = require_positive(height_m, "height_m")
    width = require_positive(width_m, "width_m")
    depth = require_positive(depth_m, "depth_m")
    return height * width * depth


def volume_with_allowance(volume_m3: float, allowance_percent: float = 0.0) -> float:
    """Add a user-selected percentage allowance to a geometric volume."""
    volume = require_non_negative(volume_m3, "volume_m3")
    allowance = require_non_negative(allowance_percent, "allowance_percent")
    return volume * (1.0 + allowance / 100.0)
