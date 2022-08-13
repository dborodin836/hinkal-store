import io
from contextlib import redirect_stdout


def hide_stdout(function):
    """Removes stdout output."""

    def wrapper(*args, **kwargs):
        with redirect_stdout(io.StringIO()):
            return function(*args, **kwargs)

    return wrapper
