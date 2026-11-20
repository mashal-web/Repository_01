import pytest

from civil_toolkit.calculators.concrete import (
    beam_volume,
    column_volume,
    slab_volume,
    volume_with_allowance,
)


def test_slab_volume():
    assert slab_volume(5, 4, 0.15) == pytest.approx(3.0)


def test_beam_volume():
    assert beam_volume(6, 0.3, 0.5) == pytest.approx(0.9)


def test_column_volume():
    assert column_volume(3, 0.3, 0.3) == pytest.approx(0.27)


def test_volume_allowance():
    assert volume_with_allowance(3, 5) == pytest.approx(3.15)


@pytest.mark.parametrize(
    "dimensions",
    [(0, 2, 1), (-1, 2, 1), (1, 2, -0.1)],
)
def test_slab_rejects_non_positive_dimensions(dimensions):
    with pytest.raises(ValueError):
        slab_volume(*dimensions)


def test_allowance_rejects_negative_percentage():
    with pytest.raises(ValueError):
        volume_with_allowance(2, -1)
