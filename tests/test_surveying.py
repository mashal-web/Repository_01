import pytest
from civil_toolkit.calculators.surveying import *

def test_slope_components_and_reconstruction():
    assert horizontal_distance(10,30)==pytest.approx(10*3**.5/2)
    assert vertical_difference(10,30)==pytest.approx(5)
    assert slope_distance(horizontal_distance(10,30),vertical_difference(10,30))==pytest.approx(10)

def test_coordinate_distance_and_leveling():
    assert coordinate_distance(0,0,3,4)==pytest.approx(5)
    assert elevation_difference(1.5,1.2)==pytest.approx(.3)
    hi=height_of_instrument(100,1.5)
    assert hi==pytest.approx(101.5)
    assert reduced_level_from_h_i(hi,1.2)==pytest.approx(100.3)

@pytest.mark.parametrize("bearing,expected",[(("N",30,"E"),30),(("S",30,"E"),150),(("S",30,"W"),210),(("N",30,"W"),330)])
def test_bearing_azimuth_roundtrip(bearing,expected):
    az=bearing_to_azimuth(*bearing); assert az==pytest.approx(expected)
    ns,ang,ew=azimuth_to_bearing(az)
    assert (ns,ew)==(bearing[0],bearing[2]); assert ang==pytest.approx(bearing[1])

@pytest.mark.parametrize("angle",[-91,91,float("nan")])
def test_invalid_vertical_angle(angle):
    with pytest.raises(ValueError): horizontal_distance(10,angle)

@pytest.mark.parametrize("az",[-1,360,float("inf")])
def test_invalid_azimuth(az):
    with pytest.raises(ValueError): azimuth_to_bearing(az)

def test_zero_distance_and_invalid_bearing():
    assert horizontal_distance(0,0)==pytest.approx(0)
    with pytest.raises(ValueError): bearing_to_azimuth("N",91,"E")
