import typer
from pathlib import Path
from rich.console import Console
from rich.columns import Columns

DIRECTORY_FORMAT = "[magenta][bold]{}"
FILE_FORMAT = "{}"

WITH_HIDDEN_GLOB_PATTERN = "*"
WITHOUT_HIDDEN_GLOB_PATTERN = "[!.]*"


def handle(
    path: str = typer.Argument("."),
    show_hidden: bool = typer.Option(False)
):
    glob_pattern = (
        WITH_HIDDEN_GLOB_PATTERN if show_hidden
        else WITHOUT_HIDDEN_GLOB_PATTERN
    )
    files = [__format__(item) for item in Path(path).glob(glob_pattern)]
    columns = Columns(files, equal=True, expand=True)
    Console().print(columns)


def __format__(file: Path):
    format_string = DIRECTORY_FORMAT if file.is_dir() else FILE_FORMAT
    return format_string.format(file.name)
