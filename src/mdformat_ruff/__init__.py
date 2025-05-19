import subprocess

__version__ = "0.1.0"


def format_python(unformatted: str, _info_str: str) -> str:
    return subprocess.check_output(
        ["ruff", "format", "-"],
        input=unformatted.encode(),
        stderr=subprocess.DEVNULL,
    ).decode()
