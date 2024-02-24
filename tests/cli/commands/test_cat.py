import pytest
from io import TextIOWrapper
from unittest import mock
from pycli.cli.commands.cat import handle


@pytest.fixture
def mocks():
    mock_file = mock.create_autospec(TextIOWrapper)
    file_content = '''
        First Line
        Second Line
        Third Line
    '''
    mock_file.__enter__.return_value.read.return_value = file_content
    return mock_file, file_content


def test_cat(capfd, mocks):
    mock_file, file_content = mocks
    with mock.patch(
        "pycli.cli.commands.cat.open_file",
        return_value=mock_file
    ) as open_file:
        handle("test_folder/file")
        open_file.assert_called_with("test_folder/file")
    out, _ = capfd.readouterr()
    assert file_content in out
