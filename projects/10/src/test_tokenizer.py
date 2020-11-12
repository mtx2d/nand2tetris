import pathlib
import unittest
from tokenizer import Tokenizer

TEST_FILE = pathlib.Path(__file__).parent.joinpath("TestTokenMain.jack")


class TestTokenizer(unittest.TestCase):
    def test_parse(self):
        file_without_comments = Tokenizer.parse(TEST_FILE)


        self.assertEqual("class", next(file_without_comments))
        self.assertEqual("Main", next(file_without_comments))
        self.assertEqual("{", next(file_without_comments))
        self.assertEqual("static", next(file_without_comments))
        self.assertEqual("boolean", next(file_without_comments))
        self.assertEqual("test", next(file_without_comments))
        self.assertEqual(";", next(file_without_comments))

        self.assertTrue(False)