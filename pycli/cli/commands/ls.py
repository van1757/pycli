import typer
from pathlib import Path
from rich.console import Console
from rich.columns import Columns

from .constants import (
    WITH_HIDDEN_GLOB,
    WITHOUT_HIDDEN_GLOB,
    DIRECTORY_FORMAT,
    FILE_FORMAT
)


def handle(
    path: str = typer.Argument("."),
    show_hidden: bool = typer.Option(False)
):
    glob = WITH_HIDDEN_GLOB if show_hidden else WITHOUT_HIDDEN_GLOB
    files = [__format__(item) for item in Path(path).glob(glob)]
    columns = Columns(files, equal=True, expand=True)
    Console().print(columns)


def __format__(file: Path):
    format_string = DIRECTORY_FORMAT if file.is_dir() else FILE_FORMAT
    return format_string.format(file.name)
