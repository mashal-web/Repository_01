import pytest
from civil_toolkit.calculators.materials import estimate_brickwork

def test_standard_wall_estimate_independent_example():
    r=estimate_brickwork(4,3,.1)
    assert r.wall_volume_m3==pytest.approx(1.2)
    assert r.theoretical_bricks==pytest.approx(600)
    assert r.bricks_to_order==630
    assert r.mortar_wet_volume_m3==pytest.approx(1.2-600*.19*.09*.09)
    assert r.cement_volume_m3+r.sand_volume_m3==pytest.approx(r.mortar_dry_volume_m3)
    assert r.cement_bags==pytest.approx(r.cement_mass_kg/50)

def test_custom_dimensions_zero_joint_and_zero_wastage():
    r=estimate_brickwork(2,2,.2,200,100,100,0,0,1,4)
    assert r.bricks_to_order==400
    assert r.mortar_wet_volume_m3==pytest.approx(0)

@pytest.mark.parametrize("kwargs",[{"length_m":0},{"height_m":-1},{"thickness_m":0},{"brick_length_mm":0},{"joint_mm":-1},{"wastage_percent":-1},{"cement_parts":0},{"sand_parts":-1},{"dry_volume_factor":0},{"cement_density_kg_m3":0},{"bag_mass_kg":0}])
def test_invalid_material_inputs(kwargs):
    args=dict(length_m=4,height_m=3,thickness_m=.1); args.update(kwargs)
    with pytest.raises((TypeError,ValueError)): estimate_brickwork(**args)

def test_non_numeric_and_non_finite_material_inputs():
    with pytest.raises(TypeError): estimate_brickwork(4,3,.1,brick_length_mm="190")
    with pytest.raises(ValueError): estimate_brickwork(4,3,.1,wastage_percent=float("nan"))
