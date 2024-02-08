import subprocess
import sys


def test_script_output(capfd):

    # Run the file under the same python interpreter
    subprocess.run([sys.executable, './main.py'])

    #capture process output
    captured = capfd.readouterr()

    assert captured.out == "hi\n"
