import pytest
from pathlib import Path
from unittest import mock
from pycli.cli.commands.ls import handle


@pytest.fixture
def files():
    dir_mock = mock.create_autospec(Path)
    file_mock = mock.create_autospec(Path)
    dir_mock.name = "directory"
    file_mock.name = "file"
    return [dir_mock, file_mock]


def test_ls(capfd, files):
    with mock.patch('pathlib.Path.glob', return_value=files, autospec=True):
        handle('.')
    out, _ = capfd.readouterr()
    assert files[0].name in out
    assert files[1].name in out


def test_ls_with_empty_results(capfd):
    with mock.patch('pathlib.Path.glob', return_value=[], autospec=True):
        handle('.')
    out, _ = capfd.readouterr()
    assert not out
