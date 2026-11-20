import pytest
from civil_toolkit.cli.interface import run_cli

@pytest.mark.parametrize("args,expected",[
 (["slab","--length","5","--width","4","--thickness",".15","--allowance","5"],"3.150 m³"),
 (["beam","--length","6","--width",".3","--depth",".5"],"0.900 m³"),
 (["column","--height","3","--width",".3","--depth",".3"],"0.270 m³"),
 (["brickwork","--length","4","--height","3","--thickness",".1"],"bricks to order: 630"),
 (["steel","--diameter","12","--length","12","--count","5"],"Theoretical steel weight: 53.333 kg"),
 (["steel-batch","--bar","10,4,6","--bar","16,2,12"],"16 mm × 2 × 12 m: 24.000 m"),
 (["survey-horizontal","--slope-distance","10","--angle","30"],"Horizontal distance: 8.660 m"),
 (["survey-slope","--horizontal","3","--vertical","4"],"5.000 m"),
 (["survey-coordinate","--easting1","0","--northing1","0","--easting2","3","--northing2","4"],"5.000 m"),
 (["survey-bearing","--ns","N","--angle","30","--ew","W"],"Azimuth: 330.000°"),
 (["survey-azimuth","--azimuth","330"],"Bearing: N 30.000° W"),
 (["survey-level","--rl","100","--bs","1.5","--fs","1.2"],"100.300 m"),
 (["survey-elevation-difference","--bs","1.5","--fs","1.2"],"0.300 m"),
 (["math-linear","--a","2","--b","-6"],"x = 3"),
 (["math-quadratic","--a","1","--b","-5","--c","6"],"Roots:"),
 (["math-trig","--value","30"],"0.5"),
 (["math-percent","--value","200","--percent","15"],"30"),
 (["math-ratio","--total","70","--first","1","--second","6"],"(10.0, 60.0)"),
 (["math-convert","--value","2","--from-unit","MPa","--to-unit","kPa"],"2000 kPa"),
 (["math-matrix-add","--matrix-a","1,2;3,4","--matrix-b","5,6;7,8"],"[[6.0, 8.0], [10.0, 12.0]]"),
 (["math-matrix-multiply","--matrix-a","1,2;3,4","--matrix-b","5,6;7,8"],"[[19.0, 22.0], [43.0, 50.0]]"),
 (["math-matrix-inverse","--matrix","1,2;3,4"],"1.5"),
 (["soil-water","--water-mass","20","--dry-soil-mass","100"],"20.000 %"),
 (["soil-void","--void-volume",".5","--solids-volume","1"],"0.5"),
 (["soil-porosity","--void-volume",".5","--total-volume","1.5"],"0.33333"),
 (["soil-saturation","--water-volume",".25","--void-volume",".5"],"50.000 %"),
 (["soil-bulk","--weight","18","--volume","1.5"],"12.000 kN/m³"),
 (["soil-dry","--dry-weight","15","--volume","1.5"],"10.000 kN/m³"),
 (["soil-phase","--gs","2.65","--void-ratio",".65","--saturation","50"],"Bulk unit weight:"),
])
def test_cli_commands(args,expected,capsys):
 assert run_cli(args)==0
 assert expected in capsys.readouterr().out

def test_cli_invalid_new_command_exits_without_traceback(capsys):
 with pytest.raises(SystemExit) as err: run_cli(["steel","--diameter","12","--length","-2"])
 assert err.value.code==2
 captured=capsys.readouterr()
 assert "length_m cannot be negative" in captured.err
 assert "Traceback" not in captured.err

def test_cli_rejects_singular_matrix(capsys):
 with pytest.raises(SystemExit) as err: run_cli(["math-matrix-inverse","--matrix","1,2;2,4"])
 assert err.value.code==2
 assert "Matrix is singular" in capsys.readouterr().err
