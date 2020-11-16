import unittest
from unittest import mock
from more_itertools import peekable
from lib.jack_token import Keyword, Symbol, Identifier, IntegerConstant, StringConstant
from lib.compilation_engine import CompilationEngine


class TestCompilationEngine(unittest.TestCase):
    def test_compile_class(self):
        mock_tokens = peekable(
            iter(
                [
                    Keyword("if"),
                    Symbol("("),
                    Identifier("x"),
                    Symbol("<"),
                    IntegerConstant("153"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("let"),
                    Identifier("city"),
                    Symbol("="),
                    StringConstant("Paris"),
                    Symbol(";"),
                    Symbol("}"),
                ]
            )
        )
        mock_output_file = mock.Mock()
        CompilationEngine.compile_class(mock_tokens, mock_output_file)
        self.assertTrue(False)
