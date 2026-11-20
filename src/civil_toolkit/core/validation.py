"""Reusable validation helpers for physical quantities and calculations."""

import math


def validate_number(value: float, name: str) -> float:
    """Return a finite float, rejecting booleans and non-numeric values."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a real number.")
    try:
        number = float(value)
    except OverflowError as exc:
        raise ValueError(f"{name} must be a finite, representable number.") from exc
    if not math.isfinite(number):
        raise ValueError(f"{name} must be finite (not NaN or infinity).")
    return number


def require_positive(value: float, name: str) -> float:
    """Return a positive finite value; zero and negatives are invalid."""
    number = validate_number(value, name)
    if number <= 0:
        raise ValueError(f"{name} must be greater than zero.")
    return number


def require_non_negative(value: float, name: str) -> float:
    """Return a non-negative finite value; zero is allowed."""
    number = validate_number(value, name)
    if number < 0:
        raise ValueError(f"{name} cannot be negative.")
    return number


def require_finite_result(value: float, name: str) -> float:
    """Reject arithmetic overflow that produces a non-finite result."""
    return validate_number(value, name)
