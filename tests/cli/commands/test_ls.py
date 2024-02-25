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


@mock.patch("pathlib.Path.glob", return_value=files, autospec=True)
def test_ls(mock_glob, capfd, files):
    mock_glob.return_value = files
    handle()
    out, _ = capfd.readouterr()
    assert files[0].name in out
    assert files[1].name in out


@mock.patch("pathlib.Path.glob", return_value=[], autospec=True)
def test_ls_with_empty_results(_, capfd):
    handle()
    out, _ = capfd.readouterr()
    assert not out
