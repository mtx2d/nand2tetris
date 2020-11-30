import sys
import unittest
from unittest import mock
from more_itertools import peekable
from lib.jack_token import Keyword, Symbol, Identifier, IntegerConstant, StringConstant
from lib.compilation_engine import CompilationEngine


class TestCompilationEngine(unittest.TestCase):
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

        mock_output_file = mock.Mock()
        CompilationEngine.compile_class(mock_tokens, mock_output_file)
        mock_output_file.assert_has_calls(
            [
                mock.call.write("<class>"),
                mock.call.write("\n"),
                mock.call.write("  <keyword> class </keyword>"),
                mock.call.write("\n"),
                mock.call.write("  <identifier> Main </identifier>"),
                mock.call.write("\n"),
                mock.call.write("  <symbol> { </symbol>"),
                mock.call.write("\n"),
                mock.call.write("    <classVarDec>"),
                mock.call.write("\n"),
                mock.call.write("      <keyword> static </keyword>"),
                mock.call.write("\n"),
                mock.call.write("        <keyword> boolean </keyword>"),
                mock.call.write("\n"),
                mock.call.write("      <identifier> test </identifier>"),
                mock.call.write("\n"),
                mock.call.write("      <symbol> ; </symbol>"),
                mock.call.write("\n"),
                mock.call.write("    </classVarDec>"),
                mock.call.write("\n"),
                mock.call.write("  <subroutineDec>"),
                mock.call.write("\n"),
                mock.call.write("    <keyword> function </keyword>"),
                mock.call.write("\n"),
                mock.call.write("  <keyword> void </keyword>"),
                mock.call.write("\n"),
                mock.call.write("    <identifier> main </identifier>"),
                mock.call.write("\n"),
                mock.call.write("    <symbol> ( </symbol>"),
                mock.call.write("\n"),
                mock.call.write("      <parameterList>"),
                mock.call.write("\n"),
                mock.call.write("      </parameterList>"),
                mock.call.write("\n"),
                mock.call.write("    <symbol> ) </symbol>"),
                mock.call.write("\n"),
                mock.call.write("      <subroutineBody>"),
                mock.call.write("\n"),
                mock.call.write("        <symbol> { </symbol>"),
                mock.call.write("\n"),
                mock.call.write("          <varDec>"),
                mock.call.write("\n"),
                mock.call.write("            <keyword> var </keyword>"),
                mock.call.write("\n"),
                mock.call.write("              <identifier> SquareGame </identifier>"),
                mock.call.write("\n"),
                mock.call.write("            <identifier> game </identifier>"),
                mock.call.write("\n"),
                mock.call.write("            <symbol> ; </symbol>"),
                mock.call.write("\n"),
                mock.call.write("          </varDec>"),
                mock.call.write("\n"),
                mock.call.write("          <statements>"),
                mock.call.write("\n"),
                mock.call.write("            <letStatement>"),
                mock.call.write("\n"),
                mock.call.write("              <keyword> let </keyword>"),
                mock.call.write("\n"),
                mock.call.write("              <identifier> game </identifier>"),
                mock.call.write("\n"),
                mock.call.write("              <symbol> = </symbol>"),
                mock.call.write("\n"),
                mock.call.write("              <expression>"),
                mock.call.write("\n"),
                mock.call.write("                <term>"),
                mock.call.write("\n"),
                mock.call.write(
                    "                    <identifier> SquareGame </identifier>"
                ),
                mock.call.write("\n"),
                mock.call.write("                    <symbol> . </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                    <identifier> new </identifier>"),
                mock.call.write("\n"),
                mock.call.write("                    <symbol> ( </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                    <expressionList>"),
                mock.call.write("\n"),
                mock.call.write("                    </expressionList>"),
                mock.call.write("\n"),
                mock.call.write("                    <symbol> ) </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                </term>"),
                mock.call.write("\n"),
                mock.call.write("              </expression>"),
                mock.call.write("\n"),
                mock.call.write("              <symbol> ; </symbol>"),
                mock.call.write("\n"),
                mock.call.write("            </letStatement>"),
                mock.call.write("\n"),
                mock.call.write("            <doStatement>"),
                mock.call.write("\n"),
                mock.call.write("              <keyword> do </keyword>"),
                mock.call.write("\n"),
                mock.call.write("                <identifier> game </identifier>"),
                mock.call.write("\n"),
                mock.call.write("                <symbol> . </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                <identifier> run </identifier>"),
                mock.call.write("\n"),
                mock.call.write("                <symbol> ( </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                <expressionList>"),
                mock.call.write("\n"),
                mock.call.write("                </expressionList>"),
                mock.call.write("\n"),
                mock.call.write("                <symbol> ) </symbol>"),
                mock.call.write("\n"),
                mock.call.write("              <symbol> ; </symbol>"),
                mock.call.write("\n"),
                mock.call.write("            </doStatement>"),
                mock.call.write("\n"),
                mock.call.write("            <doStatement>"),
                mock.call.write("\n"),
                mock.call.write("              <keyword> do </keyword>"),
                mock.call.write("\n"),
                mock.call.write("                <identifier> game </identifier>"),
                mock.call.write("\n"),
                mock.call.write("                <symbol> . </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                <identifier> dispose </identifier>"),
                mock.call.write("\n"),
                mock.call.write("                <symbol> ( </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                <expressionList>"),
                mock.call.write("\n"),
                mock.call.write("                </expressionList>"),
                mock.call.write("\n"),
                mock.call.write("                <symbol> ) </symbol>"),
                mock.call.write("\n"),
                mock.call.write("              <symbol> ; </symbol>"),
                mock.call.write("\n"),
                mock.call.write("            </doStatement>"),
                mock.call.write("\n"),
                mock.call.write("            <returnStatement>"),
                mock.call.write("\n"),
                mock.call.write("            <keyword> return </keyword>"),
                mock.call.write("\n"),
                mock.call.write("              <symbol> ; </symbol>"),
                mock.call.write("\n"),
                mock.call.write("            </returnStatement>"),
                mock.call.write("\n"),
                mock.call.write("          </statements>"),
                mock.call.write("\n"),
                mock.call.write("        <symbol> } </symbol>"),
                mock.call.write("\n"),
                mock.call.write("      </subroutineBody>"),
                mock.call.write("\n"),
                mock.call.write("  </subroutineDec>"),
                mock.call.write("\n"),
                mock.call.write("  <subroutineDec>"),
                mock.call.write("\n"),
                mock.call.write("    <keyword> function </keyword>"),
                mock.call.write("\n"),
                mock.call.write("  <keyword> void </keyword>"),
                mock.call.write("\n"),
                mock.call.write("    <identifier> test </identifier>"),
                mock.call.write("\n"),
                mock.call.write("    <symbol> ( </symbol>"),
                mock.call.write("\n"),
                mock.call.write("      <parameterList>"),
                mock.call.write("\n"),
                mock.call.write("      </parameterList>"),
                mock.call.write("\n"),
                mock.call.write("    <symbol> ) </symbol>"),
                mock.call.write("\n"),
                mock.call.write("      <subroutineBody>"),
                mock.call.write("\n"),
                mock.call.write("        <symbol> { </symbol>"),
                mock.call.write("\n"),
                mock.call.write("          <varDec>"),
                mock.call.write("\n"),
                mock.call.write("            <keyword> var </keyword>"),
                mock.call.write("\n"),
                mock.call.write("              <keyword> int </keyword>"),
                mock.call.write("\n"),
                mock.call.write("            <identifier> i </identifier>"),
                mock.call.write("\n"),
                mock.call.write("            <symbol> , </symbol>"),
                mock.call.write("\n"),
                mock.call.write("            <identifier> j </identifier>"),
                mock.call.write("\n"),
                mock.call.write("            <symbol> ; </symbol>"),
                mock.call.write("\n"),
                mock.call.write("          </varDec>"),
                mock.call.write("\n"),
                mock.call.write("          <varDec>"),
                mock.call.write("\n"),
                mock.call.write("            <keyword> var </keyword>"),
                mock.call.write("\n"),
                mock.call.write("              <identifier> String </identifier>"),
                mock.call.write("\n"),
                mock.call.write("            <identifier> s </identifier>"),
                mock.call.write("\n"),
                mock.call.write("            <symbol> ; </symbol>"),
                mock.call.write("\n"),
                mock.call.write("          </varDec>"),
                mock.call.write("\n"),
                mock.call.write("          <varDec>"),
                mock.call.write("\n"),
                mock.call.write("            <keyword> var </keyword>"),
                mock.call.write("\n"),
                mock.call.write("              <identifier> Array </identifier>"),
                mock.call.write("\n"),
                mock.call.write("            <identifier> a </identifier>"),
                mock.call.write("\n"),
                mock.call.write("            <symbol> ; </symbol>"),
                mock.call.write("\n"),
                mock.call.write("          </varDec>"),
                mock.call.write("\n"),
                mock.call.write("          <statements>"),
                mock.call.write("\n"),
                mock.call.write("            <ifStatement>"),
                mock.call.write("\n"),
                mock.call.write("              <keyword> if </keyword>"),
                mock.call.write("\n"),
                mock.call.write("              <symbol> ( </symbol>"),
                mock.call.write("\n"),
                mock.call.write("              <expression>"),
                mock.call.write("\n"),
                mock.call.write("                <term>"),
                mock.call.write("\n"),
                mock.call.write("                  <keyword> false </keyword>"),
                mock.call.write("\n"),
                mock.call.write("                </term>"),
                mock.call.write("\n"),
                mock.call.write("              </expression>"),
                mock.call.write("\n"),
                mock.call.write("              <symbol> ) </symbol>"),
                mock.call.write("\n"),
                mock.call.write("              <symbol> { </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                <statements>"),
                mock.call.write("\n"),
                mock.call.write("                  <letStatement>"),
                mock.call.write("\n"),
                mock.call.write("                    <keyword> let </keyword>"),
                mock.call.write("\n"),
                mock.call.write("                    <identifier> s </identifier>"),
                mock.call.write("\n"),
                mock.call.write("                    <symbol> = </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                    <expression>"),
                mock.call.write("\n"),
                mock.call.write("                      <term>"),
                mock.call.write("\n"),
                mock.call.write(
                    "                        <stringConstant> string constant </stringConstant>"
                ),
                mock.call.write("\n"),
                mock.call.write("                      </term>"),
                mock.call.write("\n"),
                mock.call.write("                    </expression>"),
                mock.call.write("\n"),
                mock.call.write("                    <symbol> ; </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                  </letStatement>"),
                mock.call.write("\n"),
                mock.call.write("                  <letStatement>"),
                mock.call.write("\n"),
                mock.call.write("                    <keyword> let </keyword>"),
                mock.call.write("\n"),
                mock.call.write("                    <identifier> s </identifier>"),
                mock.call.write("\n"),
                mock.call.write("                    <symbol> = </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                    <expression>"),
                mock.call.write("\n"),
                mock.call.write("                      <term>"),
                mock.call.write("\n"),
                mock.call.write("                        <keyword> null </keyword>"),
                mock.call.write("\n"),
                mock.call.write("                      </term>"),
                mock.call.write("\n"),
                mock.call.write("                    </expression>"),
                mock.call.write("\n"),
                mock.call.write("                    <symbol> ; </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                  </letStatement>"),
                mock.call.write("\n"),
                mock.call.write("                  <letStatement>"),
                mock.call.write("\n"),
                mock.call.write("                    <keyword> let </keyword>"),
                mock.call.write("\n"),
                mock.call.write("                    <identifier> a </identifier>"),
                mock.call.write("\n"),
                mock.call.write("                    <symbol> [ </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                    <expression>"),
                mock.call.write("\n"),
                mock.call.write("                      <term>"),
                mock.call.write("\n"),
                mock.call.write(
                    "                        <integerConstant> 1 </integerConstant>"
                ),
                mock.call.write("\n"),
                mock.call.write("                      </term>"),
                mock.call.write("\n"),
                mock.call.write("                    </expression>"),
                mock.call.write("\n"),
                mock.call.write("                    <symbol> ] </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                    <symbol> = </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                    <expression>"),
                mock.call.write("\n"),
                mock.call.write("                      <term>"),
                mock.call.write("\n"),
                mock.call.write("                        <identifier> a </identifier>"),
                mock.call.write("\n"),
                mock.call.write("                        <symbol> [ </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                        <expression>"),
                mock.call.write("\n"),
                mock.call.write("                          <term>"),
                mock.call.write("\n"),
                mock.call.write(
                    "                            <integerConstant> 2 </integerConstant>"
                ),
                mock.call.write("\n"),
                mock.call.write("                          </term>"),
                mock.call.write("\n"),
                mock.call.write("                        </expression>"),
                mock.call.write("\n"),
                mock.call.write("                        <symbol> ] </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                      </term>"),
                mock.call.write("\n"),
                mock.call.write("                    </expression>"),
                mock.call.write("\n"),
                mock.call.write("                    <symbol> ; </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                  </letStatement>"),
                mock.call.write("\n"),
                mock.call.write("                </statements>"),
                mock.call.write("\n"),
                mock.call.write("              <symbol> } </symbol>"),
                mock.call.write("\n"),
                mock.call.write("              <keyword> else </keyword>"),
                mock.call.write("\n"),
                mock.call.write("              <symbol> { </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                <statements>"),
                mock.call.write("\n"),
                mock.call.write("                  <letStatement>"),
                mock.call.write("\n"),
                mock.call.write("                    <keyword> let </keyword>"),
                mock.call.write("\n"),
                mock.call.write("                    <identifier> i </identifier>"),
                mock.call.write("\n"),
                mock.call.write("                    <symbol> = </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                    <expression>"),
                mock.call.write("\n"),
                mock.call.write("                      <term>"),
                mock.call.write("\n"),
                mock.call.write("                        <identifier> i </identifier>"),
                mock.call.write("\n"),
                mock.call.write("                      </term>"),
                mock.call.write("\n"),
                mock.call.write("                      <symbol> * </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                      <term>"),
                mock.call.write("\n"),
                mock.call.write("                        <symbol> ( </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                        <expression>"),
                mock.call.write("\n"),
                mock.call.write("                          <term>"),
                mock.call.write("\n"),
                mock.call.write("                            <symbol> - </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                            <term>"),
                mock.call.write("\n"),
                mock.call.write(
                    "                              <identifier> j </identifier>"
                ),
                mock.call.write("\n"),
                mock.call.write("                            </term>"),
                mock.call.write("\n"),
                mock.call.write("                          </term>"),
                mock.call.write("\n"),
                mock.call.write("                        </expression>"),
                mock.call.write("\n"),
                mock.call.write("                        <symbol> ) </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                      </term>"),
                mock.call.write("\n"),
                mock.call.write("                    </expression>"),
                mock.call.write("\n"),
                mock.call.write("                    <symbol> ; </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                  </letStatement>"),
                mock.call.write("\n"),
                mock.call.write("                  <letStatement>"),
                mock.call.write("\n"),
                mock.call.write("                    <keyword> let </keyword>"),
                mock.call.write("\n"),
                mock.call.write("                    <identifier> j </identifier>"),
                mock.call.write("\n"),
                mock.call.write("                    <symbol> = </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                    <expression>"),
                mock.call.write("\n"),
                mock.call.write("                      <term>"),
                mock.call.write("\n"),
                mock.call.write("                        <identifier> j </identifier>"),
                mock.call.write("\n"),
                mock.call.write("                      </term>"),
                mock.call.write("\n"),
                mock.call.write("                      <symbol> / </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                      <term>"),
                mock.call.write("\n"),
                mock.call.write("                        <symbol> ( </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                        <expression>"),
                mock.call.write("\n"),
                mock.call.write("                          <term>"),
                mock.call.write("\n"),
                mock.call.write("                            <symbol> - </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                            <term>"),
                mock.call.write("\n"),
                mock.call.write(
                    "                              <integerConstant> 2 </integerConstant>"
                ),
                mock.call.write("\n"),
                mock.call.write("                            </term>"),
                mock.call.write("\n"),
                mock.call.write("                          </term>"),
                mock.call.write("\n"),
                mock.call.write("                        </expression>"),
                mock.call.write("\n"),
                mock.call.write("                        <symbol> ) </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                      </term>"),
                mock.call.write("\n"),
                mock.call.write("                    </expression>"),
                mock.call.write("\n"),
                mock.call.write("                    <symbol> ; </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                  </letStatement>"),
                mock.call.write("\n"),
                mock.call.write("                  <letStatement>"),
                mock.call.write("\n"),
                mock.call.write("                    <keyword> let </keyword>"),
                mock.call.write("\n"),
                mock.call.write("                    <identifier> i </identifier>"),
                mock.call.write("\n"),
                mock.call.write("                    <symbol> = </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                    <expression>"),
                mock.call.write("\n"),
                mock.call.write("                      <term>"),
                mock.call.write("\n"),
                mock.call.write("                        <identifier> i </identifier>"),
                mock.call.write("\n"),
                mock.call.write("                      </term>"),
                mock.call.write("\n"),
                mock.call.write("                      <symbol> | </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                      <term>"),
                mock.call.write("\n"),
                mock.call.write("                        <identifier> j </identifier>"),
                mock.call.write("\n"),
                mock.call.write("                      </term>"),
                mock.call.write("\n"),
                mock.call.write("                    </expression>"),
                mock.call.write("\n"),
                mock.call.write("                    <symbol> ; </symbol>"),
                mock.call.write("\n"),
                mock.call.write("                  </letStatement>"),
                mock.call.write("\n"),
                mock.call.write("                </statements>"),
                mock.call.write("\n"),
                mock.call.write("              <symbol> } </symbol>"),
                mock.call.write("\n"),
                mock.call.write("            </ifStatement>"),
                mock.call.write("\n"),
                mock.call.write("            <returnStatement>"),
                mock.call.write("\n"),
                mock.call.write("            <keyword> return </keyword>"),
                mock.call.write("\n"),
                mock.call.write("              <symbol> ; </symbol>"),
                mock.call.write("\n"),
                mock.call.write("            </returnStatement>"),
                mock.call.write("\n"),
                mock.call.write("          </statements>"),
                mock.call.write("\n"),
                mock.call.write("        <symbol> } </symbol>"),
                mock.call.write("\n"),
                mock.call.write("      </subroutineBody>"),
                mock.call.write("\n"),
                mock.call.write("  </subroutineDec>"),
                mock.call.write("\n"),
                mock.call.write("  <symbol> } </symbol>"),
                mock.call.write("\n"),
                mock.call.write("</class>"),
                mock.call.write("\n"),
            ]
        )
