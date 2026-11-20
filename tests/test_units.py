import math

import pytest

from civil_toolkit.core.units import cm_to_m, cubic_metres_to_litres, m_to_mm, mm_to_m


@pytest.mark.parametrize(("function", "value", "expected"), [
    (mm_to_m, 150, 0.15),
    (cm_to_m, 25, 0.25),
    (m_to_mm, 1.2, 1200),
    (cubic_metres_to_litres, 2.5, 2500),
])
def test_unit_conversions(function, value, expected):
    assert function(value) == pytest.approx(expected)


@pytest.mark.parametrize("function", [mm_to_m, cm_to_m, m_to_mm, cubic_metres_to_litres])
def test_conversions_allow_zero(function):
    assert function(0) == pytest.approx(0)


@pytest.mark.parametrize("function", [mm_to_m, cm_to_m, m_to_mm, cubic_metres_to_litres])
@pytest.mark.parametrize("invalid", [-1, -0.01])
def test_conversions_reject_negative_physical_quantities(function, invalid):
    with pytest.raises(ValueError, match="negative"):
        function(invalid)


@pytest.mark.parametrize("function", [mm_to_m, cm_to_m, m_to_mm, cubic_metres_to_litres])
@pytest.mark.parametrize("invalid", ["1", None, True, object()])
def test_conversions_reject_non_numeric_values(function, invalid):
    with pytest.raises(TypeError):
        function(invalid)


@pytest.mark.parametrize("function", [mm_to_m, cm_to_m, m_to_mm, cubic_metres_to_litres])
@pytest.mark.parametrize("invalid", [math.nan, math.inf, -math.inf])
def test_conversions_reject_non_finite_values(function, invalid):
    with pytest.raises(ValueError, match="finite"):
        function(invalid)


def test_conversion_rejects_non_finite_arithmetic_result():
    with pytest.raises(ValueError, match="finite"):
        m_to_mm(1e308)
