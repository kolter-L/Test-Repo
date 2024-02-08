import subprocess
import sys

def test_script_output(capfd):

	subprocess.run(['python3', '../script.py'])

	captured = capfd.readouterr()

	assert captured.out == "hi\n"
