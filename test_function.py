from click.testing import CliRunner
from stonk import grab, clear

def test_grab_function():
    runner = CliRunner()
    result = runner.invoke(grab, ["--ticker", "SNAP", "--api_token", "Z0XJ5BZAJ049UV97"])
    assert result.exit_code == 0 # tests to make sure function returns an exit code of 0
    # assert(result.output) == '200\n' # tests to make sure the function (which returns api status_code) returns 200
    
def test_clear_function():
    runner = CliRunner()
    result = runner.invoke(clear, ["--ticker", "SNAP"])
    assert result.exit_code == 0 # tests to make sure function returns an exit code of 0