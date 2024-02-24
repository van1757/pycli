import sys
from rich.console import Console

ERROR_TYPES = {
    FileNotFoundError: "No such file or directory: '{filename}'",
    IsADirectoryError: "Is a directory: '{filename}'"
}


def handle(path: str):
    try:
        with open(path) as file:
            console = Console(markup=False)
            console.print(file.read())
    except OSError as err:
        __handleError__(err)


def __handleError__(err: OSError):
    err_console = Console(stderr=True, style="bold red")
    err_console.print(
        ERROR_TYPES[err.__class__].format(filename=err.filename),
    )
    sys.exit(err.errno)
