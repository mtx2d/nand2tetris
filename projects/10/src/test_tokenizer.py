import pathlib
import unittest
from tokenizer import Tokenizer
from jack_token import Token, Keyword, Symbol, Identifier

TEST_FILE = pathlib.Path(__file__).parent.joinpath("TestTokenMain.jack")


class TestTokenizer(unittest.TestCase):
    def test_parse(self):
        file_without_comments = Tokenizer.parse(TEST_FILE)

        self.assertEqual(Keyword("class"), next(file_without_comments))
        self.assertEqual(Identifier("Main"), next(file_without_comments))
        self.assertEqual(Symbol("{"), next(file_without_comments))
        self.assertEqual("static", next(file_without_comments))
        self.assertEqual("boolean", next(file_without_comments))
        self.assertEqual("test", next(file_without_comments))
        self.assertEqual(";", next(file_without_comments))
        self.assertEqual("function", next(file_without_comments))
        self.assertEqual("void", next(file_without_comments))
        self.assertEqual("main", next(file_without_comments))
        self.assertEqual("(", next(file_without_comments))
        self.assertEqual(")", next(file_without_comments))
        self.assertEqual("{", next(file_without_comments))
        self.assertEqual("var", next(file_without_comments))
        self.assertEqual("SquareGame", next(file_without_comments))
        self.assertEqual("game", next(file_without_comments))
        self.assertEqual(";", next(file_without_comments))
        self.assertEqual("let", next(file_without_comments))
        self.assertEqual("game", next(file_without_comments))
        self.assertEqual("=", next(file_without_comments))
        self.assertEqual("SquareGame", next(file_without_comments))
        self.assertEqual(".", next(file_without_comments))
        self.assertEqual("new", next(file_without_comments))