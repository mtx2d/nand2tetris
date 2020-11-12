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
        self.assertEqual(Keyword("static"), next(file_without_comments))
        self.assertEqual(Keyword("boolean"), next(file_without_comments))
        self.assertEqual(Identifier("test"), next(file_without_comments))
        self.assertEqual(Symbol(";"), next(file_without_comments))
        self.assertEqual(Keyword("function"), next(file_without_comments))
        self.assertEqual(Keyword("void"), next(file_without_comments))
        self.assertEqual(Identifier("main"), next(file_without_comments))
        self.assertEqual(Symbol("("), next(file_without_comments))
        self.assertEqual(Symbol(")"), next(file_without_comments))
        self.assertEqual(Symbol("{"), next(file_without_comments))
        self.assertEqual(Keyword("var"), next(file_without_comments))
        self.assertEqual(Identifier("SquareGame"), next(file_without_comments))
        self.assertEqual(Identifier("game"), next(file_without_comments))
        self.assertEqual(Symbol(";"), next(file_without_comments))
        self.assertEqual("let", next(file_without_comments))
        self.assertEqual("game", next(file_without_comments))
        self.assertEqual("=", next(file_without_comments))
        self.assertEqual("SquareGame", next(file_without_comments))
        self.assertEqual(".", next(file_without_comments))
        self.assertEqual("new", next(file_without_comments))