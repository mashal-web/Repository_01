import pytest

from civil_toolkit.cli.interface import run_cli


@pytest.mark.parametrize(("args", "expected"), [
    (["slab", "--length", "5", "--width", "4", "--thickness", "0.15", "--allowance", "5"], "3.150 m³"),
    (["beam", "--length", "6", "--width", "0.3", "--depth", "0.5"], "0.900 m³"),
    (["column", "--height", "3", "--width", "0.3", "--depth", "0.3"], "0.270 m³"),
])
def test_cli_valid_calculations(args, expected, capsys):
    assert run_cli(args) == 0
    output = capsys.readouterr().out
    assert expected in output
    assert "m³" in output


def test_cli_invalid_physical_input_exits_cleanly(capsys):
    args = ["slab", "--length", "-5", "--width", "4", "--thickness", "0.15"]
    with pytest.raises(SystemExit) as error:
        run_cli(args)
    assert error.value.code == 2
    captured = capsys.readouterr()
    assert "length_m must be greater than zero" in captured.err
    assert "Traceback" not in captured.err


def test_cli_non_numeric_input_is_argparse_error(capsys):
    args = ["beam", "--length", "x", "--width", "0.3", "--depth", "0.5"]
    with pytest.raises(SystemExit) as error:
        run_cli(args)
    assert error.value.code == 2
    assert "invalid float value" in capsys.readouterr().err


def test_cli_non_finite_input_is_validation_error(capsys):
    args = ["column", "--height", "nan", "--width", "0.3", "--depth", "0.3"]
    with pytest.raises(SystemExit) as error:
        run_cli(args)
    assert error.value.code == 2
    assert "must be finite" in capsys.readouterr().err
