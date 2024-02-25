import pytest
from io import TextIOWrapper
from unittest import mock
from pycli.cli.commands.wc import handle


@pytest.fixture
def mocks():
    mock_file = mock.create_autospec(TextIOWrapper)
    file_content = ["First Line", "Second Line", "Third Line"]
    mock_file.__enter__.return_value.__iter__.return_value = file_content
    mock_file.__enter__.return_value.name = "test_file"
    return mock_file


@mock.patch("pycli.cli.commands.wc.open_file")
def test_cat(mock_open, capfd, mocks):
    mock_file = mocks
    mock_open.return_value = mock_file
    handle("test_folder/file")
    out, _ = capfd.readouterr()
    mock_open.assert_called_with("test_folder/file")
    assert "6" in out
    assert "3" in out
    assert "test_file" in out
