"""Input validation helpers shared by calculator modules."""

import math


def _validated_number(value: float, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number.")
    number = float(value)
    if not math.isfinite(number):
        raise ValueError(f"{name} must be finite.")
    return number


def require_positive(value: float, name: str) -> float:
    """Return a positive finite numeric value or raise ValueError."""
    number = _validated_number(value, name)
    if number <= 0:
        raise ValueError(f"{name} must be greater than zero.")
    return number


def require_non_negative(value: float, name: str) -> float:
    """Return a non-negative finite numeric value or raise ValueError."""
    number = _validated_number(value, name)
    if number < 0:
        raise ValueError(f"{name} cannot be negative.")
    return number
