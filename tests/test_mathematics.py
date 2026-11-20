import math
import pytest
from civil_toolkit.calculators.mathematics import *

def test_linear_and_quadratic_solutions():
    assert solve_linear(2,-6)==pytest.approx(3)
    roots=solve_quadratic(1,-5,6)
    assert sorted(x.real for x in roots)==pytest.approx([2,3])
    assert solve_quadratic(1,0,1)[0].imag==pytest.approx(1)

def test_matrix_operations_and_inverse():
    A=[[1,2],[3,4]]; B=[[5,6],[7,8]]
    assert matrix_add(A,B)==[[6,8],[10,12]]
    assert matrix_multiply(A,B)==[[19,22],[43,50]]
    inv=matrix_inverse(A)
    assert inv[0][0]==pytest.approx(-2); assert inv[1][1]==pytest.approx(-.5)

@pytest.mark.parametrize("M",[[[1,2],[2,4]],[[1,2,3],[4,5,6]]])
def test_singular_or_non_square_inverse_rejected(M):
    with pytest.raises(ValueError): matrix_inverse(M)

def test_trigonometry_percent_ratio_and_conversion():
    assert trig(30)==pytest.approx(.5)
    assert trig(math.pi/2,"cos","radians")==pytest.approx(0,abs=1e-12)
    assert percentage(200,15)==pytest.approx(30)
    assert ratio_parts(70,1,6)==pytest.approx((10,60))
    assert convert_engineering(2,"MPa","kPa")==pytest.approx(2000)
    assert convert_engineering(1000,"mm","m")==pytest.approx(1)

def test_undefined_or_invalid_math():
    with pytest.raises(ValueError): solve_linear(0,2)
    with pytest.raises(ValueError): solve_quadratic(0,2,1)
    with pytest.raises(ValueError): matrix_multiply([[1,2]],[[1,2]])
    with pytest.raises(ValueError): trig(90,"tan")
    with pytest.raises(ValueError): ratio_parts(5,0,0)
    with pytest.raises(ValueError): convert_engineering(1,"m","kPa")
