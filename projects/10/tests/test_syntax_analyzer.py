from pathlib import Path
import unittest
from unittest import mock

from src.syntax_analyzer import get_files


class TestSyntaxAnalyzer(unittest.TestCase):
    def test_get_files_for_non_exists_file(self):
        NON_EXISTS_FILE_PATH = "/non/exists/file/path"
        self.assertRaises(FileNotFoundError, get_files, Path(NON_EXISTS_FILE_PATH))

    def test_get_files_for_non_jack_file(self):
        NON_JACK_FILE_PATH = "../../ArrayTest/Main.xml"
        self.assertRaises(Exception, get_files, Path(NON_JACK_FILE_PATH))

    def test_get_files_for_file(self):
        FILE_PATH = "../../ArrayTest/Main.jack"
        abs_path = Path(__file__).joinpath(Path(FILE_PATH))
        expected = [abs_path]
        self.assertListEqual(expected, get_files(abs_path))

    def test_get_files_for_dir(self):
        DIR_PATH = "../../ExpressionLessSquare"
        abs_dir_path = Path(__file__).joinpath(DIR_PATH)
        expected = [
            abs_dir_path.joinpath("Main.xml"),
            abs_dir_path.joinpath("Square.xml"),
            abs_dir_path.joinpath("SquareGame.xml"),
        ]
        self.assertListEqual(sorted(expected), sorted(get_files(abs_dir_path)))
