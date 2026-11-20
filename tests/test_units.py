import pytest

from civil_toolkit.core.units import (
    cm_to_m,
    cubic_metres_to_litres,
    m_to_mm,
    mm_to_m,
)


def test_length_conversions():
    assert mm_to_m(150) == pytest.approx(0.15)
    assert cm_to_m(25) == pytest.approx(0.25)
    assert m_to_mm(1.2) == pytest.approx(1200)


def test_volume_conversion():
    assert cubic_metres_to_litres(2.5) == pytest.approx(2500)
