from pycli.cli.commands.hello_world import handle


def test_hello_world(capfd):
    handle()
    out, _ = capfd.readouterr()
    assert "Hello World!\n" == out
