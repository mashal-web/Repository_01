"""Input validation helpers shared by calculator modules."""


def require_positive(value: float, name: str) -> float:
    """Return a positive finite numeric value or raise ValueError."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number.")
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero.")
    return float(value)


def require_non_negative(value: float, name: str) -> float:
    """Return a non-negative finite numeric value or raise ValueError."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number.")
    if value < 0:
        raise ValueError(f"{name} cannot be negative.")
    return float(value)
