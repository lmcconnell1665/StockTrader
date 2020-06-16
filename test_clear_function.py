from click.testing import CliRunner
from stonk import clear

def test_grab_function():
    runner = CliRunner()
    result = runner.invoke(clear, ["--ticker", "SNAP"])
    assert result.exit_code == 0 # tests to make sure function returns an exit code of 0