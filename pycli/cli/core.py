import typer

app = typer.Typer()


@app.command()
def ls():
    print("Result")


@app.command()
def hello_world():
    print("Hello World!")


def init():
    app()
