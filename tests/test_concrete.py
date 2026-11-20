import math

import pytest

from civil_toolkit.calculators.concrete import (
    beam_volume, column_volume, slab_volume, volume_with_allowance,
)


@pytest.mark.parametrize(("function", "dimensions", "expected"), [
    (slab_volume, (5, 4, 0.15), 3.0),
    (beam_volume, (6, 0.3, 0.5), 0.9),
    (column_volume, (3, 0.3, 0.3), 0.27),
])
def test_concrete_element_volumes(function, dimensions, expected):
    assert function(*dimensions) == pytest.approx(expected)


@pytest.mark.parametrize("function", [slab_volume, beam_volume, column_volume])
@pytest.mark.parametrize("dimensions", [(0, 2, 1), (-1, 2, 1), (1, 2, -0.1)])
def test_concrete_rejects_zero_or_negative_dimensions(function, dimensions):
    with pytest.raises(ValueError):
        function(*dimensions)


@pytest.mark.parametrize("function", [slab_volume, beam_volume, column_volume])
@pytest.mark.parametrize("invalid", ["1", None, True, object()])
def test_concrete_rejects_non_numeric_dimensions(function, invalid):
    with pytest.raises(TypeError):
        function(invalid, 2, 1)


@pytest.mark.parametrize("function", [slab_volume, beam_volume, column_volume])
@pytest.mark.parametrize("invalid", [math.nan, math.inf, -math.inf])
def test_concrete_rejects_non_finite_dimensions(function, invalid):
    with pytest.raises(ValueError, match="finite"):
        function(invalid, 2, 1)


def test_allowance_and_zero_edges():
    assert volume_with_allowance(3, 5) == pytest.approx(3.15)
    assert volume_with_allowance(3, 0) == pytest.approx(3)
    assert volume_with_allowance(0, 5) == pytest.approx(0)
    assert volume_with_allowance(0, 0) == pytest.approx(0)


@pytest.mark.parametrize("volume, allowance", [(-1, 0), (1, -1)])
def test_allowance_rejects_negative_quantities(volume, allowance):
    with pytest.raises(ValueError):
        volume_with_allowance(volume, allowance)


@pytest.mark.parametrize("invalid", ["3", None, True, object()])
def test_allowance_rejects_non_numeric_inputs(invalid):
    with pytest.raises(TypeError):
        volume_with_allowance(invalid, 0)


@pytest.mark.parametrize("invalid", [math.nan, math.inf, -math.inf])
def test_allowance_rejects_non_finite_inputs(invalid):
    with pytest.raises(ValueError, match="finite"):
        volume_with_allowance(invalid, 0)
    with pytest.raises(ValueError, match="finite"):
        volume_with_allowance(1, invalid)


def test_concrete_calculation_rejects_overflow_result():
    with pytest.raises(ValueError, match="finite"):
        slab_volume(1e308, 1e308, 1)


def test_allowance_rejects_overflow_result():
    with pytest.raises(ValueError, match="finite"):
        volume_with_allowance(1e308, 1e308)
