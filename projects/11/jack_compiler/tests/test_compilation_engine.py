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

    def test_square(self):
        mock_tokens = peekable(
            iter(
                [
                    Keyword("class"),
                    Identifier("Square"),
                    Symbol("{"),
                    Keyword("field"),
                    Keyword("int"),
                    Identifier("x"),
                    Symbol(","),
                    Identifier("y"),
                    Symbol(";"),
                    Keyword("field"),
                    Keyword("int"),
                    Identifier("size"),
                    Symbol(";"),
                    Keyword("constructor"),
                    Identifier("Square"),
                    Identifier("new"),
                    Symbol("("),
                    Keyword("int"),
                    Identifier("Ax"),
                    Symbol(","),
                    Keyword("int"),
                    Identifier("Ay"),
                    Symbol(","),
                    Keyword("int"),
                    Identifier("Asize"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("let"),
                    Identifier("x"),
                    Symbol("="),
                    Identifier("Ax"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("y"),
                    Symbol("="),
                    Identifier("Ay"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("size"),
                    Symbol("="),
                    Identifier("Asize"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("draw"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("return"),
                    Keyword("this"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("method"),
                    Keyword("void"),
                    Identifier("dispose"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("Memory"),
                    Symbol("."),
                    Identifier("deAlloc"),
                    Symbol("("),
                    Keyword("this"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("return"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("method"),
                    Keyword("void"),
                    Identifier("draw"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("Screen"),
                    Symbol("."),
                    Identifier("setColor"),
                    Symbol("("),
                    Keyword("true"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Screen"),
                    Symbol("."),
                    Identifier("drawRectangle"),
                    Symbol("("),
                    Identifier("x"),
                    Symbol(","),
                    Identifier("y"),
                    Symbol(","),
                    Identifier("x"),
                    Symbol("+"),
                    Identifier("size"),
                    Symbol(","),
                    Identifier("y"),
                    Symbol("+"),
                    Identifier("size"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("return"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("method"),
                    Keyword("void"),
                    Identifier("erase"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("Screen"),
                    Symbol("."),
                    Identifier("setColor"),
                    Symbol("("),
                    Keyword("false"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Screen"),
                    Symbol("."),
                    Identifier("drawRectangle"),
                    Symbol("("),
                    Identifier("x"),
                    Symbol(","),
                    Identifier("y"),
                    Symbol(","),
                    Identifier("x"),
                    Symbol("+"),
                    Identifier("size"),
                    Symbol(","),
                    Identifier("y"),
                    Symbol("+"),
                    Identifier("size"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("return"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("method"),
                    Keyword("void"),
                    Identifier("incSize"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("if"),
                    Symbol("("),
                    Symbol("("),
                    Symbol("("),
                    Identifier("y"),
                    Symbol("+"),
                    Identifier("size"),
                    Symbol(")"),
                    Symbol("<"),
                    IntegerConstant("254"),
                    Symbol(")"),
                    Symbol("&"),
                    Symbol("("),
                    Symbol("("),
                    Identifier("x"),
                    Symbol("+"),
                    Identifier("size"),
                    Symbol(")"),
                    Symbol("<"),
                    IntegerConstant("510"),
                    Symbol(")"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("erase"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("size"),
                    Symbol("="),
                    Identifier("size"),
                    Symbol("+"),
                    IntegerConstant("2"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("draw"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("return"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("method"),
                    Keyword("void"),
                    Identifier("decSize"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("if"),
                    Symbol("("),
                    Identifier("size"),
                    Symbol(">"),
                    IntegerConstant("2"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("erase"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("size"),
                    Symbol("="),
                    Identifier("size"),
                    Symbol("-"),
                    IntegerConstant("2"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("draw"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("return"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("method"),
                    Keyword("void"),
                    Identifier("moveUp"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("if"),
                    Symbol("("),
                    Identifier("y"),
                    Symbol(">"),
                    IntegerConstant("1"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("Screen"),
                    Symbol("."),
                    Identifier("setColor"),
                    Symbol("("),
                    Keyword("false"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Screen"),
                    Symbol("."),
                    Identifier("drawRectangle"),
                    Symbol("("),
                    Identifier("x"),
                    Symbol(","),
                    Symbol("("),
                    Identifier("y"),
                    Symbol("+"),
                    Identifier("size"),
                    Symbol(")"),
                    Symbol("-"),
                    IntegerConstant("1"),
                    Symbol(","),
                    Identifier("x"),
                    Symbol("+"),
                    Identifier("size"),
                    Symbol(","),
                    Identifier("y"),
                    Symbol("+"),
                    Identifier("size"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("y"),
                    Symbol("="),
                    Identifier("y"),
                    Symbol("-"),
                    IntegerConstant("2"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Screen"),
                    Symbol("."),
                    Identifier("setColor"),
                    Symbol("("),
                    Keyword("true"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Screen"),
                    Symbol("."),
                    Identifier("drawRectangle"),
                    Symbol("("),
                    Identifier("x"),
                    Symbol(","),
                    Identifier("y"),
                    Symbol(","),
                    Identifier("x"),
                    Symbol("+"),
                    Identifier("size"),
                    Symbol(","),
                    Identifier("y"),
                    Symbol("+"),
                    IntegerConstant("1"),
                    Symbol(")"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("return"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("method"),
                    Keyword("void"),
                    Identifier("moveDown"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("if"),
                    Symbol("("),
                    Symbol("("),
                    Identifier("y"),
                    Symbol("+"),
                    Identifier("size"),
                    Symbol(")"),
                    Symbol("<"),
                    IntegerConstant("254"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("Screen"),
                    Symbol("."),
                    Identifier("setColor"),
                    Symbol("("),
                    Keyword("false"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Screen"),
                    Symbol("."),
                    Identifier("drawRectangle"),
                    Symbol("("),
                    Identifier("x"),
                    Symbol(","),
                    Identifier("y"),
                    Symbol(","),
                    Identifier("x"),
                    Symbol("+"),
                    Identifier("size"),
                    Symbol(","),
                    Identifier("y"),
                    Symbol("+"),
                    IntegerConstant("1"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("y"),
                    Symbol("="),
                    Identifier("y"),
                    Symbol("+"),
                    IntegerConstant("2"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Screen"),
                    Symbol("."),
                    Identifier("setColor"),
                    Symbol("("),
                    Keyword("true"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Screen"),
                    Symbol("."),
                    Identifier("drawRectangle"),
                    Symbol("("),
                    Identifier("x"),
                    Symbol(","),
                    Symbol("("),
                    Identifier("y"),
                    Symbol("+"),
                    Identifier("size"),
                    Symbol(")"),
                    Symbol("-"),
                    IntegerConstant("1"),
                    Symbol(","),
                    Identifier("x"),
                    Symbol("+"),
                    Identifier("size"),
                    Symbol(","),
                    Identifier("y"),
                    Symbol("+"),
                    Identifier("size"),
                    Symbol(")"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("return"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("method"),
                    Keyword("void"),
                    Identifier("moveLeft"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("if"),
                    Symbol("("),
                    Identifier("x"),
                    Symbol(">"),
                    IntegerConstant("1"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("Screen"),
                    Symbol("."),
                    Identifier("setColor"),
                    Symbol("("),
                    Keyword("false"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Screen"),
                    Symbol("."),
                    Identifier("drawRectangle"),
                    Symbol("("),
                    Symbol("("),
                    Identifier("x"),
                    Symbol("+"),
                    Identifier("size"),
                    Symbol(")"),
                    Symbol("-"),
                    IntegerConstant("1"),
                    Symbol(","),
                    Identifier("y"),
                    Symbol(","),
                    Identifier("x"),
                    Symbol("+"),
                    Identifier("size"),
                    Symbol(","),
                    Identifier("y"),
                    Symbol("+"),
                    Identifier("size"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("x"),
                    Symbol("="),
                    Identifier("x"),
                    Symbol("-"),
                    IntegerConstant("2"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Screen"),
                    Symbol("."),
                    Identifier("setColor"),
                    Symbol("("),
                    Keyword("true"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Screen"),
                    Symbol("."),
                    Identifier("drawRectangle"),
                    Symbol("("),
                    Identifier("x"),
                    Symbol(","),
                    Identifier("y"),
                    Symbol(","),
                    Identifier("x"),
                    Symbol("+"),
                    IntegerConstant("1"),
                    Symbol(","),
                    Identifier("y"),
                    Symbol("+"),
                    Identifier("size"),
                    Symbol(")"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("return"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("method"),
                    Keyword("void"),
                    Identifier("moveRight"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("if"),
                    Symbol("("),
                    Symbol("("),
                    Identifier("x"),
                    Symbol("+"),
                    Identifier("size"),
                    Symbol(")"),
                    Symbol("<"),
                    IntegerConstant("510"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("Screen"),
                    Symbol("."),
                    Identifier("setColor"),
                    Symbol("("),
                    Keyword("false"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Screen"),
                    Symbol("."),
                    Identifier("drawRectangle"),
                    Symbol("("),
                    Identifier("x"),
                    Symbol(","),
                    Identifier("y"),
                    Symbol(","),
                    Identifier("x"),
                    Symbol("+"),
                    IntegerConstant("1"),
                    Symbol(","),
                    Identifier("y"),
                    Symbol("+"),
                    Identifier("size"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("x"),
                    Symbol("="),
                    Identifier("x"),
                    Symbol("+"),
                    IntegerConstant("2"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Screen"),
                    Symbol("."),
                    Identifier("setColor"),
                    Symbol("("),
                    Keyword("true"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Screen"),
                    Symbol("."),
                    Identifier("drawRectangle"),
                    Symbol("("),
                    Symbol("("),
                    Identifier("x"),
                    Symbol("+"),
                    Identifier("size"),
                    Symbol(")"),
                    Symbol("-"),
                    IntegerConstant("1"),
                    Symbol(","),
                    Identifier("y"),
                    Symbol(","),
                    Identifier("x"),
                    Symbol("+"),
                    Identifier("size"),
                    Symbol(","),
                    Identifier("y"),
                    Symbol("+"),
                    Identifier("size"),
                    Symbol(")"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("return"),
                    Symbol(";"),
                    Symbol("}"),
                    Symbol("}"),
                ]
            )
        )

        engine = CompilationEngine("Seven.jack")
        vm_insts = engine.compile_class(mock_tokens, SymbolTable())
        self.assertEqual(next(vm_insts), "function Square.new 0")
        self.assertEqual(next(vm_insts), "push constant 3")
        self.assertEqual(next(vm_insts), "call Memory.alloc 1")
        self.assertEqual(next(vm_insts), "pop pointer 0")
        self.assertEqual(next(vm_insts), "push argument 0")
        self.assertEqual(next(vm_insts), "pop this 0")
        self.assertEqual(next(vm_insts), "push argument 1")
        self.assertEqual(next(vm_insts), "pop this 1")
        self.assertEqual(next(vm_insts), "push argument 2")
        self.assertEqual(next(vm_insts), "pop this 2")
        self.assertEqual(next(vm_insts), "push pointer 0")
        self.assertEqual(next(vm_insts), "call Square.draw 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push pointer 0")
        self.assertEqual(next(vm_insts), "return")
        self.assertEqual(next(vm_insts), "function Square.dispose 0")
        self.assertEqual(next(vm_insts), "push argument 0")
        self.assertEqual(next(vm_insts), "pop pointer 0")
        self.assertEqual(next(vm_insts), "push pointer 0")
        self.assertEqual(next(vm_insts), "call Memory.deAlloc 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "return")
        self.assertEqual(next(vm_insts), "function Square.draw 0")
        self.assertEqual(next(vm_insts), "push argument 0")
        self.assertEqual(next(vm_insts), "pop pointer 0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "not")
        self.assertEqual(next(vm_insts), "call Screen.setColor 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "call Screen.drawRectangle 4")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "return")
        self.assertEqual(next(vm_insts), "function Square.erase 0")
        self.assertEqual(next(vm_insts), "push argument 0")
        self.assertEqual(next(vm_insts), "pop pointer 0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "call Screen.setColor 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "call Screen.drawRectangle 4")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "return")
        self.assertEqual(next(vm_insts), "function Square.incSize 0")
        self.assertEqual(next(vm_insts), "push argument 0")
        self.assertEqual(next(vm_insts), "pop pointer 0")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push constant 254")
        self.assertEqual(next(vm_insts), "lt")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push constant 510")
        self.assertEqual(next(vm_insts), "lt")
        self.assertEqual(next(vm_insts), "and")
        self.assertEqual(next(vm_insts), "if-goto IF_TRUE0")
        self.assertEqual(next(vm_insts), "goto IF_FALSE0")
        self.assertEqual(next(vm_insts), "label IF_TRUE0")
        self.assertEqual(next(vm_insts), "push pointer 0")
        self.assertEqual(next(vm_insts), "call Square.erase 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "push constant 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop this 2")
        self.assertEqual(next(vm_insts), "push pointer 0")
        self.assertEqual(next(vm_insts), "call Square.draw 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "label IF_FALSE0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "return")
        self.assertEqual(next(vm_insts), "function Square.decSize 0")
        self.assertEqual(next(vm_insts), "push argument 0")
        self.assertEqual(next(vm_insts), "pop pointer 0")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "push constant 2")
        self.assertEqual(next(vm_insts), "gt")
        self.assertEqual(next(vm_insts), "if-goto IF_TRUE0")
        self.assertEqual(next(vm_insts), "goto IF_FALSE0")
        self.assertEqual(next(vm_insts), "label IF_TRUE0")
        self.assertEqual(next(vm_insts), "push pointer 0")
        self.assertEqual(next(vm_insts), "call Square.erase 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "push constant 2")
        self.assertEqual(next(vm_insts), "sub")
        self.assertEqual(next(vm_insts), "pop this 2")
        self.assertEqual(next(vm_insts), "push pointer 0")
        self.assertEqual(next(vm_insts), "call Square.draw 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "label IF_FALSE0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "return")
        self.assertEqual(next(vm_insts), "function Square.moveUp 0")
        self.assertEqual(next(vm_insts), "push argument 0")
        self.assertEqual(next(vm_insts), "pop pointer 0")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push constant 1")
        self.assertEqual(next(vm_insts), "gt")
        self.assertEqual(next(vm_insts), "if-goto IF_TRUE0")
        self.assertEqual(next(vm_insts), "goto IF_FALSE0")
        self.assertEqual(next(vm_insts), "label IF_TRUE0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "call Screen.setColor 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push constant 1")
        self.assertEqual(next(vm_insts), "sub")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "call Screen.drawRectangle 4")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push constant 2")
        self.assertEqual(next(vm_insts), "sub")
        self.assertEqual(next(vm_insts), "pop this 1")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "not")
        self.assertEqual(next(vm_insts), "call Screen.setColor 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push constant 1")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "call Screen.drawRectangle 4")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "label IF_FALSE0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "return")
        self.assertEqual(next(vm_insts), "function Square.moveDown 0")
        self.assertEqual(next(vm_insts), "push argument 0")
        self.assertEqual(next(vm_insts), "pop pointer 0")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push constant 254")
        self.assertEqual(next(vm_insts), "lt")
        self.assertEqual(next(vm_insts), "if-goto IF_TRUE0")
        self.assertEqual(next(vm_insts), "goto IF_FALSE0")
        self.assertEqual(next(vm_insts), "label IF_TRUE0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "call Screen.setColor 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push constant 1")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "call Screen.drawRectangle 4")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push constant 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop this 1")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "not")
        self.assertEqual(next(vm_insts), "call Screen.setColor 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push constant 1")
        self.assertEqual(next(vm_insts), "sub")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "call Screen.drawRectangle 4")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "label IF_FALSE0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "return")
        self.assertEqual(next(vm_insts), "function Square.moveLeft 0")
        self.assertEqual(next(vm_insts), "push argument 0")
        self.assertEqual(next(vm_insts), "pop pointer 0")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push constant 1")
        self.assertEqual(next(vm_insts), "gt")
        self.assertEqual(next(vm_insts), "if-goto IF_TRUE0")
        self.assertEqual(next(vm_insts), "goto IF_FALSE0")
        self.assertEqual(next(vm_insts), "label IF_TRUE0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "call Screen.setColor 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push constant 1")
        self.assertEqual(next(vm_insts), "sub")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "call Screen.drawRectangle 4")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push constant 2")
        self.assertEqual(next(vm_insts), "sub")
        self.assertEqual(next(vm_insts), "pop this 0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "not")
        self.assertEqual(next(vm_insts), "call Screen.setColor 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push constant 1")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "call Screen.drawRectangle 4")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "label IF_FALSE0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "return")
        self.assertEqual(next(vm_insts), "function Square.moveRight 0")
        self.assertEqual(next(vm_insts), "push argument 0")
        self.assertEqual(next(vm_insts), "pop pointer 0")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push constant 510")
        self.assertEqual(next(vm_insts), "lt")
        self.assertEqual(next(vm_insts), "if-goto IF_TRUE0")
        self.assertEqual(next(vm_insts), "goto IF_FALSE0")
        self.assertEqual(next(vm_insts), "label IF_TRUE0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "call Screen.setColor 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push constant 1")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "call Screen.drawRectangle 4")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push constant 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop this 0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "not")
        self.assertEqual(next(vm_insts), "call Screen.setColor 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push constant 1")
        self.assertEqual(next(vm_insts), "sub")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push this 0")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push this 1")
        self.assertEqual(next(vm_insts), "push this 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "call Screen.drawRectangle 4")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "label IF_FALSE0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "return")

    def test_average(self):
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
                    Keyword("var"),
                    Identifier("Array"),
                    Identifier("a"),
                    Symbol(";"),
                    Keyword("var"),
                    Keyword("int"),
                    Identifier("length"),
                    Symbol(";"),
                    Keyword("var"),
                    Keyword("int"),
                    Identifier("i"),
                    Symbol(","),
                    Identifier("sum"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("length"),
                    Symbol("="),
                    Identifier("Keyboard"),
                    Symbol("."),
                    Identifier("readInt"),
                    Symbol("("),
                    StringConstant("How many numbers? "),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("a"),
                    Symbol("="),
                    Identifier("Array"),
                    Symbol("."),
                    Identifier("new"),
                    Symbol("("),
                    Identifier("length"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("i"),
                    Symbol("="),
                    IntegerConstant("0"),
                    Symbol(";"),
                    Keyword("while"),
                    Symbol("("),
                    Identifier("i"),
                    Symbol("<"),
                    Identifier("length"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("let"),
                    Identifier("a"),
                    Symbol("["),
                    Identifier("i"),
                    Symbol("]"),
                    Symbol("="),
                    Identifier("Keyboard"),
                    Symbol("."),
                    Identifier("readInt"),
                    Symbol("("),
                    StringConstant("Enter a number: "),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("sum"),
                    Symbol("="),
                    Identifier("sum"),
                    Symbol("+"),
                    Identifier("a"),
                    Symbol("["),
                    Identifier("i"),
                    Symbol("]"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("i"),
                    Symbol("="),
                    Identifier("i"),
                    Symbol("+"),
                    IntegerConstant("1"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("do"),
                    Identifier("Output"),
                    Symbol("."),
                    Identifier("printString"),
                    Symbol("("),
                    StringConstant("The average is "),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Output"),
                    Symbol("."),
                    Identifier("printInt"),
                    Symbol("("),
                    Identifier("sum"),
                    Symbol("/"),
                    Identifier("length"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("return"),
                    Symbol(";"),
                    Symbol("}"),
                    Symbol("}"),
                ]
            )
        )
        engine = CompilationEngine("Average.jack")
        vm_insts = engine.compile_class(mock_tokens, SymbolTable())

        self.assertEqual(next(vm_insts), "function Main.main 4")
        self.assertEqual(next(vm_insts), "push constant 18")
        self.assertEqual(next(vm_insts), "call String.new 1")
        self.assertEqual(next(vm_insts), "push constant 72")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 111")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 119")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 109")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 97")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 110")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 121")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 110")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 117")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 109")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 98")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 114")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 115")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 63")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "call Keyboard.readInt 1")
        self.assertEqual(next(vm_insts), "pop local 1")
        self.assertEqual(next(vm_insts), "push local 1")
        self.assertEqual(next(vm_insts), "call Array.new 1")
        self.assertEqual(next(vm_insts), "pop local 0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "pop local 2")
        self.assertEqual(next(vm_insts), "label WHILE_EXP0")
        self.assertEqual(next(vm_insts), "push local 2")
        self.assertEqual(next(vm_insts), "push local 1")
        self.assertEqual(next(vm_insts), "lt")
        self.assertEqual(next(vm_insts), "not")
        self.assertEqual(next(vm_insts), "if-goto WHILE_END0")
        self.assertEqual(next(vm_insts), "push local 2")
        self.assertEqual(next(vm_insts), "push local 0")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push constant 16")
        self.assertEqual(next(vm_insts), "call String.new 1")
        self.assertEqual(next(vm_insts), "push constant 69")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 110")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 114")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 97")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 110")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 117")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 109")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 98")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 114")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 58")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "call Keyboard.readInt 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push temp 0")
        self.assertEqual(next(vm_insts), "pop that 0")
        self.assertEqual(next(vm_insts), "push local 3")
        self.assertEqual(next(vm_insts), "push local 2")
        self.assertEqual(next(vm_insts), "push local 0")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push that 0")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop local 3")
        self.assertEqual(next(vm_insts), "push local 2")
        self.assertEqual(next(vm_insts), "push constant 1")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop local 2")
        self.assertEqual(next(vm_insts), "goto WHILE_EXP0")
        self.assertEqual(next(vm_insts), "label WHILE_END0")
        self.assertEqual(next(vm_insts), "push constant 15")
        self.assertEqual(next(vm_insts), "call String.new 1")
        self.assertEqual(next(vm_insts), "push constant 84")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 104")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 97")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 118")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 114")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 97")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 103")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 105")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 115")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "call Output.printString 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push local 3")
        self.assertEqual(next(vm_insts), "push local 1")
        self.assertEqual(next(vm_insts), "call Math.divide 2")
        self.assertEqual(next(vm_insts), "call Output.printInt 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "return")

    def test_square_game(self):
        mock_tokens = peekable(
            iter(
                [
                    Keyword("class"),
                    Identifier("SquareGame"),
                    Symbol("{"),
                    Keyword("field"),
                    Identifier("Square"),
                    Identifier("square"),
                    Symbol(";"),
                    Keyword("field"),
                    Keyword("int"),
                    Identifier("direction"),
                    Symbol(";"),
                    Keyword("constructor"),
                    Identifier("SquareGame"),
                    Identifier("new"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("let"),
                    Identifier("square"),
                    Symbol("="),
                    Identifier("Square"),
                    Symbol("."),
                    Identifier("new"),
                    Symbol("("),
                    IntegerConstant("0"),
                    Symbol(","),
                    IntegerConstant("0"),
                    Symbol(","),
                    IntegerConstant("30"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("direction"),
                    Symbol("="),
                    IntegerConstant("0"),
                    Symbol(";"),
                    Keyword("return"),
                    Keyword("this"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("method"),
                    Keyword("void"),
                    Identifier("dispose"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("square"),
                    Symbol("."),
                    Identifier("dispose"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Memory"),
                    Symbol("."),
                    Identifier("deAlloc"),
                    Symbol("("),
                    Keyword("this"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("return"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("method"),
                    Keyword("void"),
                    Identifier("moveSquare"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("if"),
                    Symbol("("),
                    Identifier("direction"),
                    Symbol("="),
                    IntegerConstant("1"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("square"),
                    Symbol("."),
                    Identifier("moveUp"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("if"),
                    Symbol("("),
                    Identifier("direction"),
                    Symbol("="),
                    IntegerConstant("2"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("square"),
                    Symbol("."),
                    Identifier("moveDown"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("if"),
                    Symbol("("),
                    Identifier("direction"),
                    Symbol("="),
                    IntegerConstant("3"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("square"),
                    Symbol("."),
                    Identifier("moveLeft"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("if"),
                    Symbol("("),
                    Identifier("direction"),
                    Symbol("="),
                    IntegerConstant("4"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("square"),
                    Symbol("."),
                    Identifier("moveRight"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("do"),
                    Identifier("Sys"),
                    Symbol("."),
                    Identifier("wait"),
                    Symbol("("),
                    IntegerConstant("5"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("return"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("method"),
                    Keyword("void"),
                    Identifier("run"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("var"),
                    Keyword("char"),
                    Identifier("key"),
                    Symbol(";"),
                    Keyword("var"),
                    Keyword("boolean"),
                    Identifier("exit"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("exit"),
                    Symbol("="),
                    Keyword("false"),
                    Symbol(";"),
                    Keyword("while"),
                    Symbol("("),
                    Symbol("~"),
                    Identifier("exit"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("while"),
                    Symbol("("),
                    Identifier("key"),
                    Symbol("="),
                    IntegerConstant("0"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("let"),
                    Identifier("key"),
                    Symbol("="),
                    Identifier("Keyboard"),
                    Symbol("."),
                    Identifier("keyPressed"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("moveSquare"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("if"),
                    Symbol("("),
                    Identifier("key"),
                    Symbol("="),
                    IntegerConstant("81"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("let"),
                    Identifier("exit"),
                    Symbol("="),
                    Keyword("true"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("if"),
                    Symbol("("),
                    Identifier("key"),
                    Symbol("="),
                    IntegerConstant("90"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("square"),
                    Symbol("."),
                    Identifier("decSize"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("if"),
                    Symbol("("),
                    Identifier("key"),
                    Symbol("="),
                    IntegerConstant("88"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("square"),
                    Symbol("."),
                    Identifier("incSize"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("if"),
                    Symbol("("),
                    Identifier("key"),
                    Symbol("="),
                    IntegerConstant("131"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("let"),
                    Identifier("direction"),
                    Symbol("="),
                    IntegerConstant("1"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("if"),
                    Symbol("("),
                    Identifier("key"),
                    Symbol("="),
                    IntegerConstant("133"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("let"),
                    Identifier("direction"),
                    Symbol("="),
                    IntegerConstant("2"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("if"),
                    Symbol("("),
                    Identifier("key"),
                    Symbol("="),
                    IntegerConstant("130"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("let"),
                    Identifier("direction"),
                    Symbol("="),
                    IntegerConstant("3"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("if"),
                    Symbol("("),
                    Identifier("key"),
                    Symbol("="),
                    IntegerConstant("132"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("let"),
                    Identifier("direction"),
                    Symbol("="),
                    IntegerConstant("4"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("while"),
                    Symbol("("),
                    Symbol("~"),
                    Symbol("("),
                    Identifier("key"),
                    Symbol("="),
                    IntegerConstant("0"),
                    Symbol(")"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("let"),
                    Identifier("key"),
                    Symbol("="),
                    Identifier("Keyboard"),
                    Symbol("."),
                    Identifier("keyPressed"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("moveSquare"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Symbol("}"),
                    Symbol("}"),
                    Keyword("return"),
                    Symbol(";"),
                    Symbol("}"),
                    Symbol("}"),
                ]
            )
        )

        engine = CompilationEngine("SquareGame.jack")
        vm_instructions = engine.compile_class(mock_tokens, SymbolTable())

        self.assertEqual(next(vm_instructions), "function SquareGame.new 0")
        self.assertEqual(next(vm_instructions), "push constant 2")
        self.assertEqual(next(vm_instructions), "call Memory.alloc 1")
        self.assertEqual(next(vm_instructions), "pop pointer 0")
        self.assertEqual(next(vm_instructions), "push constant 0")
        self.assertEqual(next(vm_instructions), "push constant 0")
        self.assertEqual(next(vm_instructions), "push constant 30")
        self.assertEqual(next(vm_instructions), "call Square.new 3")
        self.assertEqual(next(vm_instructions), "pop this 0")
        self.assertEqual(next(vm_instructions), "push constant 0")
        self.assertEqual(next(vm_instructions), "pop this 1")
        self.assertEqual(next(vm_instructions), "push pointer 0")
        self.assertEqual(next(vm_instructions), "return")
        self.assertEqual(next(vm_instructions), "function SquareGame.dispose 0")
        self.assertEqual(next(vm_instructions), "push argument 0")
        self.assertEqual(next(vm_instructions), "pop pointer 0")
        self.assertEqual(next(vm_instructions), "push this 0")
        self.assertEqual(next(vm_instructions), "call Square.dispose 1")
        self.assertEqual(next(vm_instructions), "pop temp 0")
        self.assertEqual(next(vm_instructions), "push pointer 0")
        self.assertEqual(next(vm_instructions), "call Memory.deAlloc 1")
        self.assertEqual(next(vm_instructions), "pop temp 0")
        self.assertEqual(next(vm_instructions), "push constant 0")
        self.assertEqual(next(vm_instructions), "return")
        self.assertEqual(next(vm_instructions), "function SquareGame.moveSquare 0")
        self.assertEqual(next(vm_instructions), "push argument 0")
        self.assertEqual(next(vm_instructions), "pop pointer 0")
        self.assertEqual(next(vm_instructions), "push this 1")
        self.assertEqual(next(vm_instructions), "push constant 1")
        self.assertEqual(next(vm_instructions), "eq")
        self.assertEqual(next(vm_instructions), "if-goto IF_TRUE0")
        self.assertEqual(next(vm_instructions), "goto IF_FALSE0")
        self.assertEqual(next(vm_instructions), "label IF_TRUE0")
        self.assertEqual(next(vm_instructions), "push this 0")
        self.assertEqual(next(vm_instructions), "call Square.moveUp 1")
        self.assertEqual(next(vm_instructions), "pop temp 0")
        self.assertEqual(next(vm_instructions), "label IF_FALSE0")
        self.assertEqual(next(vm_instructions), "push this 1")
        self.assertEqual(next(vm_instructions), "push constant 2")
        self.assertEqual(next(vm_instructions), "eq")
        self.assertEqual(next(vm_instructions), "if-goto IF_TRUE1")
        self.assertEqual(next(vm_instructions), "goto IF_FALSE1")
        self.assertEqual(next(vm_instructions), "label IF_TRUE1")
        self.assertEqual(next(vm_instructions), "push this 0")
        self.assertEqual(next(vm_instructions), "call Square.moveDown 1")
        self.assertEqual(next(vm_instructions), "pop temp 0")
        self.assertEqual(next(vm_instructions), "label IF_FALSE1")
        self.assertEqual(next(vm_instructions), "push this 1")
        self.assertEqual(next(vm_instructions), "push constant 3")
        self.assertEqual(next(vm_instructions), "eq")
        self.assertEqual(next(vm_instructions), "if-goto IF_TRUE2")
        self.assertEqual(next(vm_instructions), "goto IF_FALSE2")
        self.assertEqual(next(vm_instructions), "label IF_TRUE2")
        self.assertEqual(next(vm_instructions), "push this 0")
        self.assertEqual(next(vm_instructions), "call Square.moveLeft 1")
        self.assertEqual(next(vm_instructions), "pop temp 0")
        self.assertEqual(next(vm_instructions), "label IF_FALSE2")
        self.assertEqual(next(vm_instructions), "push this 1")
        self.assertEqual(next(vm_instructions), "push constant 4")
        self.assertEqual(next(vm_instructions), "eq")
        self.assertEqual(next(vm_instructions), "if-goto IF_TRUE3")
        self.assertEqual(next(vm_instructions), "goto IF_FALSE3")
        self.assertEqual(next(vm_instructions), "label IF_TRUE3")
        self.assertEqual(next(vm_instructions), "push this 0")
        self.assertEqual(next(vm_instructions), "call Square.moveRight 1")
        self.assertEqual(next(vm_instructions), "pop temp 0")
        self.assertEqual(next(vm_instructions), "label IF_FALSE3")
        self.assertEqual(next(vm_instructions), "push constant 5")
        self.assertEqual(next(vm_instructions), "call Sys.wait 1")
        self.assertEqual(next(vm_instructions), "pop temp 0")
        self.assertEqual(next(vm_instructions), "push constant 0")
        self.assertEqual(next(vm_instructions), "return")
        self.assertEqual(next(vm_instructions), "function SquareGame.run 2")
        self.assertEqual(next(vm_instructions), "push argument 0")
        self.assertEqual(next(vm_instructions), "pop pointer 0")
        self.assertEqual(next(vm_instructions), "push constant 0")
        self.assertEqual(next(vm_instructions), "pop local 1")
        self.assertEqual(next(vm_instructions), "label WHILE_EXP0")
        self.assertEqual(next(vm_instructions), "push local 1")
        self.assertEqual(next(vm_instructions), "not")
        self.assertEqual(next(vm_instructions), "not")
        self.assertEqual(next(vm_instructions), "if-goto WHILE_END0")
        self.assertEqual(next(vm_instructions), "label WHILE_EXP1")
        self.assertEqual(next(vm_instructions), "push local 0")
        self.assertEqual(next(vm_instructions), "push constant 0")
        self.assertEqual(next(vm_instructions), "eq")
        self.assertEqual(next(vm_instructions), "not")
        self.assertEqual(next(vm_instructions), "if-goto WHILE_END1")
        self.assertEqual(next(vm_instructions), "call Keyboard.keyPressed 0")
        self.assertEqual(next(vm_instructions), "pop local 0")
        self.assertEqual(next(vm_instructions), "push pointer 0")
        self.assertEqual(next(vm_instructions), "call SquareGame.moveSquare 1")
        self.assertEqual(next(vm_instructions), "pop temp 0")
        self.assertEqual(next(vm_instructions), "goto WHILE_EXP1")
        self.assertEqual(next(vm_instructions), "label WHILE_END1")
        self.assertEqual(next(vm_instructions), "push local 0")
        self.assertEqual(next(vm_instructions), "push constant 81")
        self.assertEqual(next(vm_instructions), "eq")
        self.assertEqual(next(vm_instructions), "if-goto IF_TRUE0")
        self.assertEqual(next(vm_instructions), "goto IF_FALSE0")
        self.assertEqual(next(vm_instructions), "label IF_TRUE0")
        self.assertEqual(next(vm_instructions), "push constant 0")
        self.assertEqual(next(vm_instructions), "not")
        self.assertEqual(next(vm_instructions), "pop local 1")
        self.assertEqual(next(vm_instructions), "label IF_FALSE0")
        self.assertEqual(next(vm_instructions), "push local 0")
        self.assertEqual(next(vm_instructions), "push constant 90")
        self.assertEqual(next(vm_instructions), "eq")
        self.assertEqual(next(vm_instructions), "if-goto IF_TRUE1")
        self.assertEqual(next(vm_instructions), "goto IF_FALSE1")
        self.assertEqual(next(vm_instructions), "label IF_TRUE1")
        self.assertEqual(next(vm_instructions), "push this 0")
        self.assertEqual(next(vm_instructions), "call Square.decSize 1")
        self.assertEqual(next(vm_instructions), "pop temp 0")
        self.assertEqual(next(vm_instructions), "label IF_FALSE1")
        self.assertEqual(next(vm_instructions), "push local 0")
        self.assertEqual(next(vm_instructions), "push constant 88")
        self.assertEqual(next(vm_instructions), "eq")
        self.assertEqual(next(vm_instructions), "if-goto IF_TRUE2")
        self.assertEqual(next(vm_instructions), "goto IF_FALSE2")
        self.assertEqual(next(vm_instructions), "label IF_TRUE2")
        self.assertEqual(next(vm_instructions), "push this 0")
        self.assertEqual(next(vm_instructions), "call Square.incSize 1")
        self.assertEqual(next(vm_instructions), "pop temp 0")
        self.assertEqual(next(vm_instructions), "label IF_FALSE2")
        self.assertEqual(next(vm_instructions), "push local 0")
        self.assertEqual(next(vm_instructions), "push constant 131")
        self.assertEqual(next(vm_instructions), "eq")
        self.assertEqual(next(vm_instructions), "if-goto IF_TRUE3")
        self.assertEqual(next(vm_instructions), "goto IF_FALSE3")
        self.assertEqual(next(vm_instructions), "label IF_TRUE3")
        self.assertEqual(next(vm_instructions), "push constant 1")
        self.assertEqual(next(vm_instructions), "pop this 1")
        self.assertEqual(next(vm_instructions), "label IF_FALSE3")
        self.assertEqual(next(vm_instructions), "push local 0")
        self.assertEqual(next(vm_instructions), "push constant 133")
        self.assertEqual(next(vm_instructions), "eq")
        self.assertEqual(next(vm_instructions), "if-goto IF_TRUE4")
        self.assertEqual(next(vm_instructions), "goto IF_FALSE4")
        self.assertEqual(next(vm_instructions), "label IF_TRUE4")
        self.assertEqual(next(vm_instructions), "push constant 2")
        self.assertEqual(next(vm_instructions), "pop this 1")
        self.assertEqual(next(vm_instructions), "label IF_FALSE4")
        self.assertEqual(next(vm_instructions), "push local 0")
        self.assertEqual(next(vm_instructions), "push constant 130")
        self.assertEqual(next(vm_instructions), "eq")
        self.assertEqual(next(vm_instructions), "if-goto IF_TRUE5")
        self.assertEqual(next(vm_instructions), "goto IF_FALSE5")
        self.assertEqual(next(vm_instructions), "label IF_TRUE5")
        self.assertEqual(next(vm_instructions), "push constant 3")
        self.assertEqual(next(vm_instructions), "pop this 1")
        self.assertEqual(next(vm_instructions), "label IF_FALSE5")
        self.assertEqual(next(vm_instructions), "push local 0")
        self.assertEqual(next(vm_instructions), "push constant 132")
        self.assertEqual(next(vm_instructions), "eq")
        self.assertEqual(next(vm_instructions), "if-goto IF_TRUE6")
        self.assertEqual(next(vm_instructions), "goto IF_FALSE6")
        self.assertEqual(next(vm_instructions), "label IF_TRUE6")
        self.assertEqual(next(vm_instructions), "push constant 4")
        self.assertEqual(next(vm_instructions), "pop this 1")
        self.assertEqual(next(vm_instructions), "label IF_FALSE6")
        self.assertEqual(next(vm_instructions), "label WHILE_EXP2")
        self.assertEqual(next(vm_instructions), "push local 0")
        self.assertEqual(next(vm_instructions), "push constant 0")
        self.assertEqual(next(vm_instructions), "eq")
        self.assertEqual(next(vm_instructions), "not")
        self.assertEqual(next(vm_instructions), "not")
        self.assertEqual(next(vm_instructions), "if-goto WHILE_END2")
        self.assertEqual(next(vm_instructions), "call Keyboard.keyPressed 0")
        self.assertEqual(next(vm_instructions), "pop local 0")
        self.assertEqual(next(vm_instructions), "push pointer 0")
        self.assertEqual(next(vm_instructions), "call SquareGame.moveSquare 1")
        self.assertEqual(next(vm_instructions), "pop temp 0")
        self.assertEqual(next(vm_instructions), "goto WHILE_EXP2")
        self.assertEqual(next(vm_instructions), "label WHILE_END2")
        self.assertEqual(next(vm_instructions), "goto WHILE_EXP0")
        self.assertEqual(next(vm_instructions), "label WHILE_END0")
        self.assertEqual(next(vm_instructions), "push constant 0")
        self.assertEqual(next(vm_instructions), "return")
