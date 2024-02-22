from pycli.cli.commands.ls import handle


def test_hello_world(capfd):
    handle()
    out, _ = capfd.readouterr()
    assert "Result\n" == out
