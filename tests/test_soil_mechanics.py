import pytest
from civil_toolkit.calculators.soil_mechanics import *

def test_phase_relationships_and_unit_weights():
    assert water_content(20,100)==pytest.approx(20)
    assert void_ratio(.5,1)==pytest.approx(.5)
    assert porosity(.5,1.5)==pytest.approx(1/3)
    assert degree_of_saturation(.25,.5)==pytest.approx(50)
    assert bulk_unit_weight(18,1.5)==pytest.approx(12)
    assert dry_unit_weight(15,1.5)==pytest.approx(10)
    bulk,dry=phase_unit_weights(2.65,.65,50)
    assert bulk==pytest.approx(9.81*(2.65+.5*.65)/1.65)
    assert dry==pytest.approx(9.81*2.65/1.65)

def test_zero_boundaries():
    assert water_content(0,10)==pytest.approx(0)
    assert void_ratio(0,1)==pytest.approx(0)
    assert porosity(0,1)==pytest.approx(0)
    assert degree_of_saturation(0,1)==pytest.approx(0)
    assert bulk_unit_weight(0,1)==pytest.approx(0)

@pytest.mark.parametrize("call",[lambda:water_content(1,0),lambda:void_ratio(1,0),lambda:porosity(2,1),lambda:degree_of_saturation(2,1),lambda:bulk_unit_weight(1,0),lambda:dry_unit_weight(-1,1),lambda:phase_unit_weights(2,.5,101),lambda:phase_unit_weights(0,.5,50)])
def test_physically_invalid_soil_inputs(call):
    with pytest.raises(ValueError): call()

def test_phase_dictionary():
    r=phase_relationships(.5,80)
    assert r["porosity"]==pytest.approx(1/3)
    assert r["water_to_solids_volume_ratio"]==pytest.approx(.4)
