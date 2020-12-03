import sys
import unittest
from unittest import mock
from more_itertools import peekable
from lib.jack_token import Keyword, Symbol, Identifier, IntegerConstant, StringConstant
from lib.compilation_engine import CompilationEngine
from lib.symbol_table import SymbolTable


class TestCompilationEngine(unittest.TestCase):
    def test_compile_class_seven(self):
        mock_tokens = peekable(
            iter(
                [
                    Keyword("class"),
                    Identifier("Main"),
                    Symbol("{"),
                    Keyword("function"),
                    Keyword("void"),
                    Identifier("main"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("Output"),
                    Symbol("."),
                    Identifier("printInt"),
                    Symbol("("),
                    IntegerConstant("1"),
                    Symbol("+"),
                    Symbol("("),
                    IntegerConstant("2"),
                    Symbol("*"),
                    IntegerConstant("3"),
                    Symbol(")"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("return"),
                    Symbol(";"),
                    Symbol("}"),
                    Symbol("}"),
                ]
            )
        )

        engine = CompilationEngine("Main.jack")

        vm_insts = engine.compile_class(mock_tokens, SymbolTable())

        self.assertEqual(next(vm_insts), "function Main.main 0")
        self.assertEqual(next(vm_insts), "push constant 1")
        self.assertEqual(next(vm_insts), "push constant 2")
        self.assertEqual(next(vm_insts), "push constant 3")
        self.assertEqual(next(vm_insts), "call Math.multiply 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "call Output.printInt 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "return")

    def test_convert_to_bin(self):
        tokens = peekable(
            iter(
                [
                    Keyword("class"),
                    Identifier("Main"),
                    Symbol("{"),
                    Keyword("function"),
                    Keyword("void"),
                    Identifier("main"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("var"),
                    Keyword("int"),
                    Identifier("value"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Main"),
                    Symbol("."),
                    Identifier("fillMemory"),
                    Symbol("("),
                    IntegerConstant("8001"),
                    Symbol(","),
                    IntegerConstant("16"),
                    Symbol(","),
                    Symbol("-"),
                    IntegerConstant("1"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("value"),
                    Symbol("="),
                    Identifier("Memory"),
                    Symbol("."),
                    Identifier("peek"),
                    Symbol("("),
                    IntegerConstant("8000"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Main"),
                    Symbol("."),
                    Identifier("convert"),
                    Symbol("("),
                    Identifier("value"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("return"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("function"),
                    Keyword("void"),
                    Identifier("convert"),
                    Symbol("("),
                    Keyword("int"),
                    Identifier("value"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("var"),
                    Keyword("int"),
                    Identifier("mask"),
                    Symbol(","),
                    Identifier("position"),
                    Symbol(";"),
                    Keyword("var"),
                    Keyword("boolean"),
                    Identifier("loop"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("loop"),
                    Symbol("="),
                    Keyword("true"),
                    Symbol(";"),
                    Keyword("while"),
                    Symbol("("),
                    Identifier("loop"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("let"),
                    Identifier("position"),
                    Symbol("="),
                    Identifier("position"),
                    Symbol("+"),
                    IntegerConstant("1"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("mask"),
                    Symbol("="),
                    Identifier("Main"),
                    Symbol("."),
                    Identifier("nextMask"),
                    Symbol("("),
                    Identifier("mask"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("if"),
                    Symbol("("),
                    Symbol("~"),
                    Symbol("("),
                    Identifier("position"),
                    Symbol(">"),
                    IntegerConstant("16"),
                    Symbol(")"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("if"),
                    Symbol("("),
                    Symbol("~"),
                    Symbol("("),
                    Symbol("("),
                    Identifier("value"),
                    Symbol("&"),
                    Identifier("mask"),
                    Symbol(")"),
                    Symbol("="),
                    IntegerConstant("0"),
                    Symbol(")"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("Memory"),
                    Symbol("."),
                    Identifier("poke"),
                    Symbol("("),
                    IntegerConstant("8000"),
                    Symbol("+"),
                    Identifier("position"),
                    Symbol(","),
                    IntegerConstant("1"),
                    Symbol(")"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("else"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("Memory"),
                    Symbol("."),
                    Identifier("poke"),
                    Symbol("("),
                    IntegerConstant("8000"),
                    Symbol("+"),
                    Identifier("position"),
                    Symbol(","),
                    IntegerConstant("0"),
                    Symbol(")"),
                    Symbol(";"),
                    Symbol("}"),
                    Symbol("}"),
                    Keyword("else"),
                    Symbol("{"),
                    Keyword("let"),
                    Identifier("loop"),
                    Symbol("="),
                    Keyword("false"),
                    Symbol(";"),
                    Symbol("}"),
                    Symbol("}"),
                    Keyword("return"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("function"),
                    Keyword("int"),
                    Identifier("nextMask"),
                    Symbol("("),
                    Keyword("int"),
                    Identifier("mask"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("if"),
                    Symbol("("),
                    Identifier("mask"),
                    Symbol("="),
                    IntegerConstant("0"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("return"),
                    IntegerConstant("1"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("else"),
                    Symbol("{"),
                    Keyword("return"),
                    Identifier("mask"),
                    Symbol("*"),
                    IntegerConstant("2"),
                    Symbol(";"),
                    Symbol("}"),
                    Symbol("}"),
                    Keyword("function"),
                    Keyword("void"),
                    Identifier("fillMemory"),
                    Symbol("("),
                    Keyword("int"),
                    Identifier("startAddress"),
                    Symbol(","),
                    Keyword("int"),
                    Identifier("length"),
                    Symbol(","),
                    Keyword("int"),
                    Identifier("value"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("while"),
                    Symbol("("),
                    Identifier("length"),
                    Symbol(">"),
                    IntegerConstant("0"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("Memory"),
                    Symbol("."),
                    Identifier("poke"),
                    Symbol("("),
                    Identifier("startAddress"),
                    Symbol(","),
                    Identifier("value"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("length"),
                    Symbol("="),
                    Identifier("length"),
                    Symbol("-"),
                    IntegerConstant("1"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("startAddress"),
                    Symbol("="),
                    Identifier("startAddress"),
                    Symbol("+"),
                    IntegerConstant("1"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("return"),
                    Symbol(";"),
                    Symbol("}"),
                    Symbol("}"),
                ]
            )
        )

        compile_engine = CompilationEngine("Main.jack")
        vm_insts = compile_engine.compile_class(tokens, SymbolTable())

        self.assertEqual(next(vm_insts), "function Main.main 1"),
        self.assertEqual(next(vm_insts), "push constant 8001"),
        self.assertEqual(next(vm_insts), "push constant 16"),
        self.assertEqual(next(vm_insts), "push constant 1"),
        self.assertEqual(next(vm_insts), "neg"),
        self.assertEqual(next(vm_insts), "call Main.fillMemory 3"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "push constant 8000"),
        self.assertEqual(next(vm_insts), "call Memory.peek 1"),
        self.assertEqual(next(vm_insts), "pop local 0"),
        self.assertEqual(next(vm_insts), "push local 0"),
        self.assertEqual(next(vm_insts), "call Main.convert 1"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "return"),
        self.assertEqual(next(vm_insts), "function Main.convert 3"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "not"),
        self.assertEqual(next(vm_insts), "pop local 2"),
        self.assertEqual(next(vm_insts), "label WHILE_EXP0"),
        self.assertEqual(next(vm_insts), "push local 2"),
        self.assertEqual(next(vm_insts), "not"),
        self.assertEqual(next(vm_insts), "if-goto WHILE_END0"),
        self.assertEqual(next(vm_insts), "push local 1"),
        self.assertEqual(next(vm_insts), "push constant 1"),
        self.assertEqual(next(vm_insts), "add"),
        self.assertEqual(next(vm_insts), "pop local 1"),
        self.assertEqual(next(vm_insts), "push local 0"),
        self.assertEqual(next(vm_insts), "call Main.nextMask 1"),
        self.assertEqual(next(vm_insts), "pop local 0"),
        self.assertEqual(next(vm_insts), "push local 1"),
        self.assertEqual(next(vm_insts), "push constant 16"),
        self.assertEqual(next(vm_insts), "gt"),
        self.assertEqual(next(vm_insts), "not"),
        self.assertEqual(next(vm_insts), "if-goto IF_TRUE0"),
        self.assertEqual(next(vm_insts), "goto IF_FALSE0"),
        self.assertEqual(next(vm_insts), "label IF_TRUE0"),
        self.assertEqual(next(vm_insts), "push argument 0"),
        self.assertEqual(next(vm_insts), "push local 0"),
        self.assertEqual(next(vm_insts), "and"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "eq"),
        self.assertEqual(next(vm_insts), "not"),
        self.assertEqual(next(vm_insts), "if-goto IF_TRUE1"),
        self.assertEqual(next(vm_insts), "goto IF_FALSE1"),
        self.assertEqual(next(vm_insts), "label IF_TRUE1"),
        self.assertEqual(next(vm_insts), "push constant 8000"),
        self.assertEqual(next(vm_insts), "push local 1"),
        self.assertEqual(next(vm_insts), "add"),
        self.assertEqual(next(vm_insts), "push constant 1"),
        self.assertEqual(next(vm_insts), "call Memory.poke 2"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "goto IF_END1"),
        self.assertEqual(next(vm_insts), "label IF_FALSE1"),
        self.assertEqual(next(vm_insts), "push constant 8000"),
        self.assertEqual(next(vm_insts), "push local 1"),
        self.assertEqual(next(vm_insts), "add"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "call Memory.poke 2"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "label IF_END1"),
        self.assertEqual(next(vm_insts), "goto IF_END0"),
        self.assertEqual(next(vm_insts), "label IF_FALSE0"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "pop local 2"),
        self.assertEqual(next(vm_insts), "label IF_END0"),
        self.assertEqual(next(vm_insts), "goto WHILE_EXP0"),
        self.assertEqual(next(vm_insts), "label WHILE_END0"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "return"),
        self.assertEqual(next(vm_insts), "function Main.nextMask 0"),
        self.assertEqual(next(vm_insts), "push argument 0"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "eq"),
        self.assertEqual(next(vm_insts), "if-goto IF_TRUE0"),
        self.assertEqual(next(vm_insts), "goto IF_FALSE0"),
        self.assertEqual(next(vm_insts), "label IF_TRUE0"),
        self.assertEqual(next(vm_insts), "push constant 1"),
        self.assertEqual(next(vm_insts), "return"),
        self.assertEqual(next(vm_insts), "goto IF_END0"),
        self.assertEqual(next(vm_insts), "label IF_FALSE0"),
        self.assertEqual(next(vm_insts), "push argument 0"),
        self.assertEqual(next(vm_insts), "push constant 2"),
        self.assertEqual(next(vm_insts), "call Math.multiply 2"),
        self.assertEqual(next(vm_insts), "return"),
        self.assertEqual(next(vm_insts), "label IF_END0"),
        self.assertEqual(next(vm_insts), "function Main.fillMemory 0"),
        self.assertEqual(next(vm_insts), "label WHILE_EXP0"),
        self.assertEqual(next(vm_insts), "push argument 1"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "gt"),
        self.assertEqual(next(vm_insts), "not"),
        self.assertEqual(next(vm_insts), "if-goto WHILE_END0"),
        self.assertEqual(next(vm_insts), "push argument 0"),
        self.assertEqual(next(vm_insts), "push argument 2"),
        self.assertEqual(next(vm_insts), "call Memory.poke 2"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "push argument 1"),
        self.assertEqual(next(vm_insts), "push constant 1"),
        self.assertEqual(next(vm_insts), "sub"),
        self.assertEqual(next(vm_insts), "pop argument 1"),
        self.assertEqual(next(vm_insts), "push argument 0"),
        self.assertEqual(next(vm_insts), "push constant 1"),
        self.assertEqual(next(vm_insts), "add"),
        self.assertEqual(next(vm_insts), "pop argument 0"),
        self.assertEqual(next(vm_insts), "goto WHILE_EXP0"),
        self.assertEqual(next(vm_insts), "label WHILE_END0"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "return"),

    def test_compile_statements(self):
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
        mock_symbol_table = mock.Mock()
        vm_instructions = CompilationEngine.compile_statements(
            mock_tokens, mock_symbol_table
        )
        self.assertEqual(next(vm_instructions), f'{" " * 2 * 1}<statements>')
        self.assertEqual(next(vm_instructions), f'{" " * 2 * 2}<ifStatement>')
        self.assertEqual(next(vm_instructions), Keyword("if").to_xml(3))
        self.assertEqual(next(vm_instructions), Symbol("(").to_xml(3))
        self.assertEqual(next(vm_instructions), f'{" " * 2 * 3}<expression>')
        self.assertEqual(next(vm_instructions), f'{" " * 2 * 4}<term>')
        self.assertEqual(next(vm_instructions), Identifier("x").to_xml(5))
        self.assertEqual(next(vm_instructions), f'{" " * 2 * 4}</term>')
        self.assertEqual(next(vm_instructions), Symbol("<").to_xml(4))
        self.assertEqual(next(vm_instructions), f'{" " * 2 * 4}<term>')
        self.assertEqual(next(vm_instructions), IntegerConstant("153").to_xml(5))
        self.assertEqual(next(vm_instructions), f'{" " * 2 * 4}</term>')
        self.assertEqual(next(vm_instructions), f'{" " * 2 * 3}</expression>')
        self.assertEqual(next(vm_instructions), Symbol(")").to_xml(3))
        self.assertEqual(next(vm_instructions), Symbol("{").to_xml(3))
        self.assertEqual(next(vm_instructions), f'{" " * 2 * 4}<statements>')
        self.assertEqual(next(vm_instructions), f'{" " * 2 * 5}<letStatement>')
        self.assertEqual(next(vm_instructions), Keyword("let").to_xml(6))
        self.assertEqual(next(vm_instructions), Identifier("city").to_xml(6))
        self.assertEqual(next(vm_instructions), Symbol("=").to_xml(6))
        self.assertEqual(next(vm_instructions), f'{" " * 2 * 6}<expression>')
        self.assertEqual(next(vm_instructions), f'{" " * 2 * 7}<term>')
        self.assertEqual(next(vm_instructions), StringConstant("Paris").to_xml(8))
        self.assertEqual(next(vm_instructions), f'{" " * 2 * 7}</term>')
        self.assertEqual(next(vm_instructions), f'{" " * 2 * 6}</expression>')
        self.assertEqual(next(vm_instructions), Symbol(";").to_xml(6))
        self.assertEqual(next(vm_instructions), f'{" " * 2 * 5}</letStatement>')
        self.assertEqual(next(vm_instructions), f'{" " * 2 * 4}</statements>')
        self.assertEqual(next(vm_instructions), Symbol("}").to_xml(3))
        self.assertEqual(next(vm_instructions), f'{" " * 2 * 2}</ifStatement>')
        self.assertEqual(next(vm_instructions), f'{" " * 2 * 1}</statements>')

    def test_compile_class(self):
        mock_tokens = peekable(
            iter(
                [
                    Keyword("class"),
                    Identifier("Main"),
                    Symbol("{"),
                    Keyword("static"),
                    Keyword("boolean"),
                    Identifier("test"),
                    Symbol(";"),
                    Keyword("function"),
                    Keyword("void"),
                    Identifier("main"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("var"),
                    Identifier("SquareGame"),
                    Identifier("game"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("game"),
                    Symbol("="),
                    Identifier("SquareGame"),
                    Symbol("."),
                    Identifier("new"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("game"),
                    Symbol("."),
                    Identifier("run"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("game"),
                    Symbol("."),
                    Identifier("dispose"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("return"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("function"),
                    Keyword("void"),
                    Identifier("test"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("var"),
                    Keyword("int"),
                    Identifier("i"),
                    Symbol(","),
                    Identifier("j"),
                    Symbol(";"),
                    Keyword("var"),
                    Identifier("String"),
                    Identifier("s"),
                    Symbol(";"),
                    Keyword("var"),
                    Identifier("Array"),
                    Identifier("a"),
                    Symbol(";"),
                    Keyword("if"),
                    Symbol("("),
                    Keyword("false"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("let"),
                    Identifier("s"),
                    Symbol("="),
                    StringConstant("string constant"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("s"),
                    Symbol("="),
                    Keyword("null"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("a"),
                    Symbol("["),
                    IntegerConstant("1"),
                    Symbol("]"),
                    Symbol("="),
                    Identifier("a"),
                    Symbol("["),
                    IntegerConstant("2"),
                    Symbol("]"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("else"),
                    Symbol("{"),
                    Keyword("let"),
                    Identifier("i"),
                    Symbol("="),
                    Identifier("i"),
                    Symbol("*"),
                    Symbol("("),
                    Symbol("-"),
                    Identifier("j"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("j"),
                    Symbol("="),
                    Identifier("j"),
                    Symbol("/"),
                    Symbol("("),
                    Symbol("-"),
                    IntegerConstant("2"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("i"),
                    Symbol("="),
                    Identifier("i"),
                    Symbol("|"),
                    Identifier("j"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("return"),
                    Symbol(";"),
                    Symbol("}"),
                    Symbol("}"),
                ]
            )
        )

        mock_symbol_table = mock.Mock()
        vm_instructions = CompilationEngine.compile_class(
            mock_tokens, mock_symbol_table
        )
        self.assertEqual(next(vm_instructions), "<class>"),
        self.assertEqual(next(vm_instructions), "  <keyword> class </keyword>"),
        self.assertEqual(next(vm_instructions), "  <identifier> Main </identifier>"),
        self.assertEqual(next(vm_instructions), "  <symbol> { </symbol>"),
        self.assertEqual(next(vm_instructions), "    <classVarDec>"),
        self.assertEqual(next(vm_instructions), "      <keyword> static </keyword>"),
        self.assertEqual(next(vm_instructions), "        <keyword> boolean </keyword>"),
        self.assertEqual(
            next(vm_instructions), "      <identifier> test </identifier>"
        ),
        self.assertEqual(next(vm_instructions), "      <symbol> ; </symbol>"),
        self.assertEqual(next(vm_instructions), "    </classVarDec>"),
        self.assertEqual(next(vm_instructions), "  <subroutineDec>"),
        self.assertEqual(next(vm_instructions), "    <keyword> function </keyword>"),
        self.assertEqual(next(vm_instructions), "  <keyword> void </keyword>"),
        self.assertEqual(next(vm_instructions), "    <identifier> main </identifier>"),
        self.assertEqual(next(vm_instructions), "    <symbol> ( </symbol>"),
        self.assertEqual(next(vm_instructions), "      <parameterList>"),
        self.assertEqual(next(vm_instructions), "      </parameterList>"),
        self.assertEqual(next(vm_instructions), "    <symbol> ) </symbol>"),
        self.assertEqual(next(vm_instructions), "      <subroutineBody>"),
        self.assertEqual(next(vm_instructions), "        <symbol> { </symbol>"),
        self.assertEqual(next(vm_instructions), "          <varDec>"),
        self.assertEqual(next(vm_instructions), "            <keyword> var </keyword>"),
        self.assertEqual(
            next(vm_instructions), "              <identifier> SquareGame </identifier>"
        ),
        self.assertEqual(
            next(vm_instructions), "            <identifier> game </identifier>"
        ),
        self.assertEqual(next(vm_instructions), "            <symbol> ; </symbol>"),
        self.assertEqual(next(vm_instructions), "          </varDec>"),
        self.assertEqual(next(vm_instructions), "          <statements>"),
        self.assertEqual(next(vm_instructions), "            <letStatement>"),
        self.assertEqual(
            next(vm_instructions), "              <keyword> let </keyword>"
        ),
        self.assertEqual(
            next(vm_instructions), "              <identifier> game </identifier>"
        ),
        self.assertEqual(next(vm_instructions), "              <symbol> = </symbol>"),
        self.assertEqual(next(vm_instructions), "              <expression>"),
        self.assertEqual(next(vm_instructions), "                <term>"),
        self.assertEqual(
            next(vm_instructions),
            "                    <identifier> SquareGame </identifier>",
        ),
        self.assertEqual(
            next(vm_instructions), "                    <symbol> . </symbol>"
        ),
        self.assertEqual(
            next(vm_instructions), "                    <identifier> new </identifier>"
        ),
        self.assertEqual(
            next(vm_instructions), "                    <symbol> ( </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                    <expressionList>"),
        self.assertEqual(
            next(vm_instructions), "                    </expressionList>"
        ),
        self.assertEqual(
            next(vm_instructions), "                    <symbol> ) </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                </term>"),
        self.assertEqual(next(vm_instructions), "              </expression>"),
        self.assertEqual(next(vm_instructions), "              <symbol> ; </symbol>"),
        self.assertEqual(next(vm_instructions), "            </letStatement>"),
        self.assertEqual(next(vm_instructions), "            <doStatement>"),
        self.assertEqual(
            next(vm_instructions), "              <keyword> do </keyword>"
        ),
        self.assertEqual(
            next(vm_instructions), "                <identifier> game </identifier>"
        ),
        self.assertEqual(next(vm_instructions), "                <symbol> . </symbol>"),
        self.assertEqual(
            next(vm_instructions), "                <identifier> run </identifier>"
        ),
        self.assertEqual(next(vm_instructions), "                <symbol> ( </symbol>"),
        self.assertEqual(next(vm_instructions), "                <expressionList>"),
        self.assertEqual(next(vm_instructions), "                </expressionList>"),
        self.assertEqual(next(vm_instructions), "                <symbol> ) </symbol>"),
        self.assertEqual(next(vm_instructions), "              <symbol> ; </symbol>"),
        self.assertEqual(next(vm_instructions), "            </doStatement>"),
        self.assertEqual(next(vm_instructions), "            <doStatement>"),
        self.assertEqual(
            next(vm_instructions), "              <keyword> do </keyword>"
        ),
        self.assertEqual(
            next(vm_instructions), "                <identifier> game </identifier>"
        ),
        self.assertEqual(next(vm_instructions), "                <symbol> . </symbol>"),
        self.assertEqual(
            next(vm_instructions), "                <identifier> dispose </identifier>"
        ),
        self.assertEqual(next(vm_instructions), "                <symbol> ( </symbol>"),
        self.assertEqual(next(vm_instructions), "                <expressionList>"),
        self.assertEqual(next(vm_instructions), "                </expressionList>"),
        self.assertEqual(next(vm_instructions), "                <symbol> ) </symbol>"),
        self.assertEqual(next(vm_instructions), "              <symbol> ; </symbol>"),
        self.assertEqual(next(vm_instructions), "            </doStatement>"),
        self.assertEqual(next(vm_instructions), "            <returnStatement>"),
        self.assertEqual(
            next(vm_instructions), "            <keyword> return </keyword>"
        ),
        self.assertEqual(next(vm_instructions), "              <symbol> ; </symbol>"),
        self.assertEqual(next(vm_instructions), "            </returnStatement>"),
        self.assertEqual(next(vm_instructions), "          </statements>"),
        self.assertEqual(next(vm_instructions), "        <symbol> } </symbol>"),
        self.assertEqual(next(vm_instructions), "      </subroutineBody>"),
        self.assertEqual(next(vm_instructions), "  </subroutineDec>"),
        self.assertEqual(next(vm_instructions), "  <subroutineDec>"),
        self.assertEqual(next(vm_instructions), "    <keyword> function </keyword>"),
        self.assertEqual(next(vm_instructions), "  <keyword> void </keyword>"),
        self.assertEqual(next(vm_instructions), "    <identifier> test </identifier>"),
        self.assertEqual(next(vm_instructions), "    <symbol> ( </symbol>"),
        self.assertEqual(next(vm_instructions), "      <parameterList>"),
        self.assertEqual(next(vm_instructions), "      </parameterList>"),
        self.assertEqual(next(vm_instructions), "    <symbol> ) </symbol>"),
        self.assertEqual(next(vm_instructions), "      <subroutineBody>"),
        self.assertEqual(next(vm_instructions), "        <symbol> { </symbol>"),
        self.assertEqual(next(vm_instructions), "          <varDec>"),
        self.assertEqual(next(vm_instructions), "            <keyword> var </keyword>"),
        self.assertEqual(
            next(vm_instructions), "              <keyword> int </keyword>"
        ),
        self.assertEqual(
            next(vm_instructions), "            <identifier> i </identifier>"
        ),
        self.assertEqual(next(vm_instructions), "            <symbol> , </symbol>"),
        self.assertEqual(
            next(vm_instructions), "            <identifier> j </identifier>"
        ),
        self.assertEqual(next(vm_instructions), "            <symbol> ; </symbol>"),
        self.assertEqual(next(vm_instructions), "          </varDec>"),
        self.assertEqual(next(vm_instructions), "          <varDec>"),
        self.assertEqual(next(vm_instructions), "            <keyword> var </keyword>"),
        self.assertEqual(
            next(vm_instructions), "              <identifier> String </identifier>"
        ),
        self.assertEqual(
            next(vm_instructions), "            <identifier> s </identifier>"
        ),
        self.assertEqual(next(vm_instructions), "            <symbol> ; </symbol>"),
        self.assertEqual(next(vm_instructions), "          </varDec>"),
        self.assertEqual(next(vm_instructions), "          <varDec>"),
        self.assertEqual(next(vm_instructions), "            <keyword> var </keyword>"),
        self.assertEqual(
            next(vm_instructions), "              <identifier> Array </identifier>"
        ),
        self.assertEqual(
            next(vm_instructions), "            <identifier> a </identifier>"
        ),
        self.assertEqual(next(vm_instructions), "            <symbol> ; </symbol>"),
        self.assertEqual(next(vm_instructions), "          </varDec>"),
        self.assertEqual(next(vm_instructions), "          <statements>"),
        self.assertEqual(next(vm_instructions), "            <ifStatement>"),
        self.assertEqual(
            next(vm_instructions), "              <keyword> if </keyword>"
        ),
        self.assertEqual(next(vm_instructions), "              <symbol> ( </symbol>"),
        self.assertEqual(next(vm_instructions), "              <expression>"),
        self.assertEqual(next(vm_instructions), "                <term>"),
        self.assertEqual(
            next(vm_instructions), "                  <keyword> false </keyword>"
        ),
        self.assertEqual(next(vm_instructions), "                </term>"),
        self.assertEqual(next(vm_instructions), "              </expression>"),
        self.assertEqual(next(vm_instructions), "              <symbol> ) </symbol>"),
        self.assertEqual(next(vm_instructions), "              <symbol> { </symbol>"),
        self.assertEqual(next(vm_instructions), "                <statements>"),
        self.assertEqual(next(vm_instructions), "                  <letStatement>"),
        self.assertEqual(
            next(vm_instructions), "                    <keyword> let </keyword>"
        ),
        self.assertEqual(
            next(vm_instructions), "                    <identifier> s </identifier>"
        ),
        self.assertEqual(
            next(vm_instructions), "                    <symbol> = </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                    <expression>"),
        self.assertEqual(next(vm_instructions), "                      <term>"),
        self.assertEqual(
            next(vm_instructions),
            "                        <stringConstant> string constant </stringConstant>",
        ),
        self.assertEqual(next(vm_instructions), "                      </term>"),
        self.assertEqual(next(vm_instructions), "                    </expression>"),
        self.assertEqual(
            next(vm_instructions), "                    <symbol> ; </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                  </letStatement>"),
        self.assertEqual(next(vm_instructions), "                  <letStatement>"),
        self.assertEqual(
            next(vm_instructions), "                    <keyword> let </keyword>"
        ),
        self.assertEqual(
            next(vm_instructions), "                    <identifier> s </identifier>"
        ),
        self.assertEqual(
            next(vm_instructions), "                    <symbol> = </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                    <expression>"),
        self.assertEqual(next(vm_instructions), "                      <term>"),
        self.assertEqual(
            next(vm_instructions), "                        <keyword> null </keyword>"
        ),
        self.assertEqual(next(vm_instructions), "                      </term>"),
        self.assertEqual(next(vm_instructions), "                    </expression>"),
        self.assertEqual(
            next(vm_instructions), "                    <symbol> ; </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                  </letStatement>"),
        self.assertEqual(next(vm_instructions), "                  <letStatement>"),
        self.assertEqual(
            next(vm_instructions), "                    <keyword> let </keyword>"
        ),
        self.assertEqual(
            next(vm_instructions), "                    <identifier> a </identifier>"
        ),
        self.assertEqual(
            next(vm_instructions), "                    <symbol> [ </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                    <expression>"),
        self.assertEqual(next(vm_instructions), "                      <term>"),
        self.assertEqual(
            next(vm_instructions),
            "                        <integerConstant> 1 </integerConstant>",
        ),
        self.assertEqual(next(vm_instructions), "                      </term>"),
        self.assertEqual(next(vm_instructions), "                    </expression>"),
        self.assertEqual(
            next(vm_instructions), "                    <symbol> ] </symbol>"
        ),
        self.assertEqual(
            next(vm_instructions), "                    <symbol> = </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                    <expression>"),
        self.assertEqual(next(vm_instructions), "                      <term>"),
        self.assertEqual(
            next(vm_instructions),
            "                        <identifier> a </identifier>",
        ),
        self.assertEqual(
            next(vm_instructions), "                        <symbol> [ </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                        <expression>"),
        self.assertEqual(next(vm_instructions), "                          <term>"),
        self.assertEqual(
            next(vm_instructions),
            "                            <integerConstant> 2 </integerConstant>",
        ),
        self.assertEqual(next(vm_instructions), "                          </term>"),
        self.assertEqual(
            next(vm_instructions), "                        </expression>"
        ),
        self.assertEqual(
            next(vm_instructions), "                        <symbol> ] </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                      </term>"),
        self.assertEqual(next(vm_instructions), "                    </expression>"),
        self.assertEqual(
            next(vm_instructions), "                    <symbol> ; </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                  </letStatement>"),
        self.assertEqual(next(vm_instructions), "                </statements>"),
        self.assertEqual(next(vm_instructions), "              <symbol> } </symbol>"),
        self.assertEqual(
            next(vm_instructions), "              <keyword> else </keyword>"
        ),
        self.assertEqual(next(vm_instructions), "              <symbol> { </symbol>"),
        self.assertEqual(next(vm_instructions), "                <statements>"),
        self.assertEqual(next(vm_instructions), "                  <letStatement>"),
        self.assertEqual(
            next(vm_instructions), "                    <keyword> let </keyword>"
        ),
        self.assertEqual(
            next(vm_instructions), "                    <identifier> i </identifier>"
        ),
        self.assertEqual(
            next(vm_instructions), "                    <symbol> = </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                    <expression>"),
        self.assertEqual(next(vm_instructions), "                      <term>"),
        self.assertEqual(
            next(vm_instructions),
            "                        <identifier> i </identifier>",
        ),
        self.assertEqual(next(vm_instructions), "                      </term>"),
        self.assertEqual(
            next(vm_instructions), "                      <symbol> * </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                      <term>"),
        self.assertEqual(
            next(vm_instructions), "                        <symbol> ( </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                        <expression>"),
        self.assertEqual(next(vm_instructions), "                          <term>"),
        self.assertEqual(
            next(vm_instructions), "                            <symbol> - </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                            <term>"),
        self.assertEqual(
            next(vm_instructions),
            "                              <identifier> j </identifier>",
        ),
        self.assertEqual(next(vm_instructions), "                            </term>"),
        self.assertEqual(next(vm_instructions), "                          </term>"),
        self.assertEqual(
            next(vm_instructions), "                        </expression>"
        ),
        self.assertEqual(
            next(vm_instructions), "                        <symbol> ) </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                      </term>"),
        self.assertEqual(next(vm_instructions), "                    </expression>"),
        self.assertEqual(
            next(vm_instructions), "                    <symbol> ; </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                  </letStatement>"),
        self.assertEqual(next(vm_instructions), "                  <letStatement>"),
        self.assertEqual(
            next(vm_instructions), "                    <keyword> let </keyword>"
        ),
        self.assertEqual(
            next(vm_instructions), "                    <identifier> j </identifier>"
        ),
        self.assertEqual(
            next(vm_instructions), "                    <symbol> = </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                    <expression>"),
        self.assertEqual(next(vm_instructions), "                      <term>"),
        self.assertEqual(
            next(vm_instructions),
            "                        <identifier> j </identifier>",
        ),
        self.assertEqual(next(vm_instructions), "                      </term>"),
        self.assertEqual(
            next(vm_instructions), "                      <symbol> / </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                      <term>"),
        self.assertEqual(
            next(vm_instructions), "                        <symbol> ( </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                        <expression>"),
        self.assertEqual(next(vm_instructions), "                          <term>"),
        self.assertEqual(
            next(vm_instructions), "                            <symbol> - </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                            <term>"),
        self.assertEqual(
            next(vm_instructions),
            "                              <integerConstant> 2 </integerConstant>",
        ),
        self.assertEqual(next(vm_instructions), "                            </term>"),
        self.assertEqual(next(vm_instructions), "                          </term>"),
        self.assertEqual(
            next(vm_instructions), "                        </expression>"
        ),
        self.assertEqual(
            next(vm_instructions), "                        <symbol> ) </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                      </term>"),
        self.assertEqual(next(vm_instructions), "                    </expression>"),
        self.assertEqual(
            next(vm_instructions), "                    <symbol> ; </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                  </letStatement>"),
        self.assertEqual(next(vm_instructions), "                  <letStatement>"),
        self.assertEqual(
            next(vm_instructions), "                    <keyword> let </keyword>"
        ),
        self.assertEqual(
            next(vm_instructions), "                    <identifier> i </identifier>"
        ),
        self.assertEqual(
            next(vm_instructions), "                    <symbol> = </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                    <expression>"),
        self.assertEqual(next(vm_instructions), "                      <term>"),
        self.assertEqual(
            next(vm_instructions),
            "                        <identifier> i </identifier>",
        ),
        self.assertEqual(next(vm_instructions), "                      </term>"),
        self.assertEqual(
            next(vm_instructions), "                      <symbol> | </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                      <term>"),
        self.assertEqual(
            next(vm_instructions),
            "                        <identifier> j </identifier>",
        ),
        self.assertEqual(next(vm_instructions), "                      </term>"),
        self.assertEqual(next(vm_instructions), "                    </expression>"),
        self.assertEqual(
            next(vm_instructions), "                    <symbol> ; </symbol>"
        ),
        self.assertEqual(next(vm_instructions), "                  </letStatement>"),
        self.assertEqual(next(vm_instructions), "                </statements>"),
        self.assertEqual(next(vm_instructions), "              <symbol> } </symbol>"),
        self.assertEqual(next(vm_instructions), "            </ifStatement>"),
        self.assertEqual(next(vm_instructions), "            <returnStatement>"),
        self.assertEqual(
            next(vm_instructions), "            <keyword> return </keyword>"
        ),
        self.assertEqual(next(vm_instructions), "              <symbol> ; </symbol>"),
        self.assertEqual(next(vm_instructions), "            </returnStatement>"),
        self.assertEqual(next(vm_instructions), "          </statements>"),
        self.assertEqual(next(vm_instructions), "        <symbol> } </symbol>"),
        self.assertEqual(next(vm_instructions), "      </subroutineBody>"),
        self.assertEqual(next(vm_instructions), "  </subroutineDec>"),
        self.assertEqual(next(vm_instructions), "  <symbol> } </symbol>"),
        self.assertEqual(next(vm_instructions), "</class>"),
