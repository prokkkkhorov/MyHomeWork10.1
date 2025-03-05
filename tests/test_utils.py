import json
import pytest
from dotenv import load_dotenv
from unittest.mock import patch, mock_open
from src.utils import parse_data

@patch("builtins.open")
@patch("json.load")
def test_parse_data_ok(mock_load, mock_open_file):
    mock_open_file.new = mock_open()
    mock_load.return_value = [{}]
    result = parse_data("")
    assert result == [{}]


@patch("builtins.open")
def test_parse_data_file_not_found(mock_open_file):
    mock_open_file.new = mock_open()
    mock_open_file.side_effect = FileNotFoundError

    result = parse_data("")
    assert result == []


@patch("builtins.open")
@patch("json.load")
def test_parse_data_json_decode(mock_load, mock_open_file):
    mock_open_file.new = mock_open()
    mock_load.side_effect = json.JSONDecodeError("ERROR", "", 1)
    result = parse_data("")
    assert result == []



