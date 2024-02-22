import typer

from pycli.cli.commands import COMMANDS

app = typer.Typer()

for name, handler in COMMANDS.items():
    app.command(name)(handler)


def init():
    app()
