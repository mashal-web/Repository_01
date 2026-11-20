import pytest
from civil_toolkit.cli.interface import run_cli

@pytest.mark.parametrize("args,expected",[
 (["slab","--length","5","--width","4","--thickness",".15","--allowance","5"],"3.150 m³"),
 (["beam","--length","6","--width",".3","--depth",".5"],"0.900 m³"),
 (["column","--height","3","--width",".3","--depth",".3"],"0.270 m³"),
 (["brickwork","--length","4","--height","3","--thickness",".1"],"bricks to order: 630"),
 (["steel","--diameter","12","--length","12","--count","5"],"Theoretical steel weight: 53.333 kg"),
 (["survey-horizontal","--slope-distance","10","--angle","30"],"Horizontal distance: 8.660 m"),
 (["survey-coordinate","--easting1","0","--northing1","0","--easting2","3","--northing2","4"],"5.000 m"),
 (["survey-bearing","--ns","N","--angle","30","--ew","W"],"Azimuth: 330.000°"),
 (["survey-level","--rl","100","--bs","1.5","--fs","1.2"],"100.300 m"),
 (["math-linear","--a","2","--b","-6"],"x = 3"),
 (["math-trig","--value","30"],"0.5"),
 (["math-percent","--value","200","--percent","15"],"30"),
 (["math-convert","--value","2","--from-unit","MPa","--to-unit","kPa"],"2000 kPa"),
 (["soil-water","--water-mass","20","--dry-soil-mass","100"],"20.000 %"),
 (["soil-phase","--gs","2.65","--void-ratio",".65","--saturation","50"],"Bulk unit weight:"),
])
def test_cli_commands(args,expected,capsys):
 assert run_cli(args)==0
 assert expected in capsys.readouterr().out

def test_cli_invalid_new_command_exits_without_traceback(capsys):
 with pytest.raises(SystemExit) as err:
  run_cli(["steel","--diameter","12","--length","-2"])
 assert err.value.code==2
 captured=capsys.readouterr()
 assert "length_m cannot be negative" in captured.err
 assert "Traceback" not in captured.err
