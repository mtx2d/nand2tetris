import pathlib
import unittest
from tokenizer import Tokenizer

TEST_FILE = pathlib.Path(__file__).parent.joinpath("TestTokenMain.jack")


class TestTokenizer(unittest.TestCase):
    def test_parse(self):
        file_without_comments = Tokenizer.parse(TEST_FILE)

        token = next(file_without_comments)

        print("token is:", token)
        print("token is:", next(file_without_comments))

        self.assertTrue(False)