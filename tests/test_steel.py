import pytest
from civil_toolkit.calculators.steel import bar_weight,total_bar_weight,multiple_bar_weights

def test_bar_weight_documented_formula():
    assert bar_weight(12,12)==pytest.approx((12**2/162)*12)
    assert bar_weight(12,0)==pytest.approx(0)
    assert total_bar_weight(12,12,5)==pytest.approx(5*(144/162)*12)

def test_multiple_bar_sizes_and_lengths():
    r=multiple_bar_weights([(10,4,6),(16,2,12)])
    assert r[0].total_length_m==pytest.approx(24)
    assert r[0].theoretical_weight_kg==pytest.approx(10**2/162*24)
    assert r[1].theoretical_weight_kg==pytest.approx(16**2/162*24)

@pytest.mark.parametrize("d,L",[(0,1),(-1,2),(12,-1)])
def test_invalid_bar_dimensions(d,L):
    with pytest.raises(ValueError): bar_weight(d,L)

@pytest.mark.parametrize("count",[-1,1.5,True])
def test_invalid_bar_count(count):
    with pytest.raises(ValueError): total_bar_weight(12,6,count)
