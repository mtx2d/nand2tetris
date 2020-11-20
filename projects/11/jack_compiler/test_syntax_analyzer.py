from pathlib import Path
import unittest
from unittest import mock

from syntax_analyzer import get_files


class TestSyntaxAnalyzer(unittest.TestCase):
    def test_get_files_for_non_exists_file(self):
        NON_EXISTS_FILE_PATH = "/non/exists/file/path"
        self.assertRaises(FileNotFoundError, get_files, Path(NON_EXISTS_FILE_PATH))

    def test_get_files_for_non_jack_file(self):
        NON_JACK_FILE_PATH = "tests/ArrayTest/Main.xml"
        self.assertRaises(Exception, get_files, Path(NON_JACK_FILE_PATH))

    def test_get_files_for_file(self):
        FILE_PATH = "tests/ArrayTest/Main.jack"
        abs_path = Path(__file__).parent.absolute().joinpath(Path(FILE_PATH))
        expected = [abs_path]
        self.assertListEqual(expected, get_files(abs_path))

    def test_get_files_for_dir(self):
        DIR_PATH = "tests/ExpressionLessSquare"
        abs_dir_path = Path(__file__).parent.absolute().joinpath(Path(DIR_PATH))
        expected = [
            abs_dir_path.joinpath("Main.jack"),
            abs_dir_path.joinpath("Square.jack"),
            abs_dir_path.joinpath("SquareGame.jack"),
        ]
        self.assertListEqual(sorted(expected), sorted(get_files(abs_dir_path)))
