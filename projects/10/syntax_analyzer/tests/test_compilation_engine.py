import sys
import unittest
from unittest import mock
from more_itertools import peekable
from lib.jack_token import Keyword, Symbol, Identifier, IntegerConstant, StringConstant
from lib.compilation_engine import CompilationEngine


class TestCompilationEngine(unittest.TestCase):
    def test_compile_statments(self):
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
                    None
                ]
            )
        )
        mock_output_file = mock.Mock()
        CompilationEngine.compile_statements(mock_tokens, mock_output_file)
        mock_output_file.assert_has_calls(
            [
                mock.call.write(Keyword("if").to_xml(1)),
                mock.call.write("\n"),
                mock.call.write(Symbol("(").to_xml(1)),
                mock.call.write("\n"),
                mock.call.write(Identifier("x").to_xml(3)),
                mock.call.write("\n"),
                mock.call.write(Symbol("<").to_xml(2)),
                mock.call.write("\n"),
                mock.call.write(IntegerConstant("153").to_xml(3)),
                mock.call.write("\n"),
                mock.call.write(Symbol(")").to_xml(1)),
                mock.call.write("\n"),
                mock.call.write(Symbol("{").to_xml(1)),
                mock.call.write("\n"),
                mock.call.write(Keyword("let").to_xml(2)),
                mock.call.write("\n"),
                mock.call.write(Identifier("city").to_xml(2)),
                mock.call.write("\n"),
                mock.call.write(Symbol("=").to_xml(2)),
                mock.call.write("\n"),
                mock.call.write(StringConstant("Paris").to_xml(4)),
                mock.call.write("\n"),
                mock.call.write(Symbol(";").to_xml(2)),
                mock.call.write("\n"),
                mock.call.write(Symbol("}").to_xml(1)),
                mock.call.write("\n"),
            ]
        )
