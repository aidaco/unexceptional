import subprocess
from tempfile import NamedTemporaryFile
from pathlib import Path


def test_exec_file():
    wd = Path.cwd()
    file = NamedTemporaryFile(dir=wd, delete=False)
    fp = wd / file.name
    file.write(b"val = 1/0\n")
    file.close()
    result = subprocess.run(["python", fp], capture_output=True)
    fp.unlink()
    assert result.stderr == b""


def test_exec_str():
    result = subprocess.run(["python", "-c", "raise Exception()"], capture_output=True)
    assert result.stderr == b""


def test_exec_repl():
    result = subprocess.run(["python"], input=b'1+"1"\n', capture_output=True)
    assert result.stderr == b""


def test_exec_ipy():
    proc = subprocess.Popen(
        ["ipython"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
    )
    res = proc.communicate(b"abcd\n")
    proc.kill()
    assert b"Error" not in res[1]
