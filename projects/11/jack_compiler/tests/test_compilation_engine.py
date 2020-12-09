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

    def test_pong_game(self):
        mock_tokens = peekable(
            iter(
                [
                    Keyword("class"),
                    Identifier("PongGame"),
                    Symbol("{"),
                    Keyword("static"),
                    Identifier("PongGame"),
                    Identifier("instance"),
                    Symbol(";"),
                    Keyword("field"),
                    Identifier("Bat"),
                    Identifier("bat"),
                    Symbol(";"),
                    Keyword("field"),
                    Identifier("Ball"),
                    Identifier("ball"),
                    Symbol(";"),
                    Keyword("field"),
                    Keyword("int"),
                    Identifier("wall"),
                    Symbol(";"),
                    Keyword("field"),
                    Keyword("boolean"),
                    Identifier("exit"),
                    Symbol(";"),
                    Keyword("field"),
                    Keyword("int"),
                    Identifier("score"),
                    Symbol(";"),
                    Keyword("field"),
                    Keyword("int"),
                    Identifier("lastWall"),
                    Symbol(";"),
                    Keyword("field"),
                    Keyword("int"),
                    Identifier("batWidth"),
                    Symbol(";"),
                    Keyword("constructor"),
                    Identifier("PongGame"),
                    Identifier("new"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("Screen"),
                    Symbol("."),
                    Identifier("clearScreen"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("batWidth"),
                    Symbol("="),
                    IntegerConstant("50"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("bat"),
                    Symbol("="),
                    Identifier("Bat"),
                    Symbol("."),
                    Identifier("new"),
                    Symbol("("),
                    IntegerConstant("230"),
                    Symbol(","),
                    IntegerConstant("229"),
                    Symbol(","),
                    Identifier("batWidth"),
                    Symbol(","),
                    IntegerConstant("7"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("ball"),
                    Symbol("="),
                    Identifier("Ball"),
                    Symbol("."),
                    Identifier("new"),
                    Symbol("("),
                    IntegerConstant("253"),
                    Symbol(","),
                    IntegerConstant("222"),
                    Symbol(","),
                    IntegerConstant("0"),
                    Symbol(","),
                    IntegerConstant("511"),
                    Symbol(","),
                    IntegerConstant("0"),
                    Symbol(","),
                    IntegerConstant("229"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("ball"),
                    Symbol("."),
                    Identifier("setDestination"),
                    Symbol("("),
                    IntegerConstant("400"),
                    Symbol(","),
                    IntegerConstant("0"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Screen"),
                    Symbol("."),
                    Identifier("drawRectangle"),
                    Symbol("("),
                    IntegerConstant("0"),
                    Symbol(","),
                    IntegerConstant("238"),
                    Symbol(","),
                    IntegerConstant("511"),
                    Symbol(","),
                    IntegerConstant("240"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Output"),
                    Symbol("."),
                    Identifier("moveCursor"),
                    Symbol("("),
                    IntegerConstant("22"),
                    Symbol(","),
                    IntegerConstant("0"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Output"),
                    Symbol("."),
                    Identifier("printString"),
                    Symbol("("),
                    StringConstant("Score: 0"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("exit"),
                    Symbol("="),
                    Keyword("false"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("score"),
                    Symbol("="),
                    IntegerConstant("0"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("wall"),
                    Symbol("="),
                    IntegerConstant("0"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("lastWall"),
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
                    Identifier("bat"),
                    Symbol("."),
                    Identifier("dispose"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("ball"),
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
                    Keyword("function"),
                    Keyword("void"),
                    Identifier("newInstance"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("let"),
                    Identifier("instance"),
                    Symbol("="),
                    Identifier("PongGame"),
                    Symbol("."),
                    Identifier("new"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("return"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("function"),
                    Identifier("PongGame"),
                    Identifier("getInstance"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("return"),
                    Identifier("instance"),
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
                    Keyword("while"),
                    Symbol("("),
                    Symbol("~"),
                    Identifier("exit"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("while"),
                    Symbol("("),
                    Symbol("("),
                    Identifier("key"),
                    Symbol("="),
                    IntegerConstant("0"),
                    Symbol(")"),
                    Symbol("&"),
                    Symbol("("),
                    Symbol("~"),
                    Identifier("exit"),
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
                    Identifier("bat"),
                    Symbol("."),
                    Identifier("move"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("moveBall"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Sys"),
                    Symbol("."),
                    Identifier("wait"),
                    Symbol("("),
                    IntegerConstant("50"),
                    Symbol(")"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("if"),
                    Symbol("("),
                    Identifier("key"),
                    Symbol("="),
                    IntegerConstant("130"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("bat"),
                    Symbol("."),
                    Identifier("setDirection"),
                    Symbol("("),
                    IntegerConstant("1"),
                    Symbol(")"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("else"),
                    Symbol("{"),
                    Keyword("if"),
                    Symbol("("),
                    Identifier("key"),
                    Symbol("="),
                    IntegerConstant("132"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("bat"),
                    Symbol("."),
                    Identifier("setDirection"),
                    Symbol("("),
                    IntegerConstant("2"),
                    Symbol(")"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("else"),
                    Symbol("{"),
                    Keyword("if"),
                    Symbol("("),
                    Identifier("key"),
                    Symbol("="),
                    IntegerConstant("140"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("let"),
                    Identifier("exit"),
                    Symbol("="),
                    Keyword("true"),
                    Symbol(";"),
                    Symbol("}"),
                    Symbol("}"),
                    Symbol("}"),
                    Keyword("while"),
                    Symbol("("),
                    Symbol("("),
                    Symbol("~"),
                    Symbol("("),
                    Identifier("key"),
                    Symbol("="),
                    IntegerConstant("0"),
                    Symbol(")"),
                    Symbol(")"),
                    Symbol("&"),
                    Symbol("("),
                    Symbol("~"),
                    Identifier("exit"),
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
                    Identifier("bat"),
                    Symbol("."),
                    Identifier("move"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("moveBall"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Sys"),
                    Symbol("."),
                    Identifier("wait"),
                    Symbol("("),
                    IntegerConstant("50"),
                    Symbol(")"),
                    Symbol(";"),
                    Symbol("}"),
                    Symbol("}"),
                    Keyword("if"),
                    Symbol("("),
                    Identifier("exit"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("Output"),
                    Symbol("."),
                    Identifier("moveCursor"),
                    Symbol("("),
                    IntegerConstant("10"),
                    Symbol(","),
                    IntegerConstant("27"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Output"),
                    Symbol("."),
                    Identifier("printString"),
                    Symbol("("),
                    StringConstant("Game Over"),
                    Symbol(")"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("return"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("method"),
                    Keyword("void"),
                    Identifier("moveBall"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("var"),
                    Keyword("int"),
                    Identifier("bouncingDirection"),
                    Symbol(","),
                    Identifier("batLeft"),
                    Symbol(","),
                    Identifier("batRight"),
                    Symbol(","),
                    Identifier("ballLeft"),
                    Symbol(","),
                    Identifier("ballRight"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("wall"),
                    Symbol("="),
                    Identifier("ball"),
                    Symbol("."),
                    Identifier("move"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("if"),
                    Symbol("("),
                    Symbol("("),
                    Identifier("wall"),
                    Symbol(">"),
                    IntegerConstant("0"),
                    Symbol(")"),
                    Symbol("&"),
                    Symbol("("),
                    Symbol("~"),
                    Symbol("("),
                    Identifier("wall"),
                    Symbol("="),
                    Identifier("lastWall"),
                    Symbol(")"),
                    Symbol(")"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("let"),
                    Identifier("lastWall"),
                    Symbol("="),
                    Identifier("wall"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("bouncingDirection"),
                    Symbol("="),
                    IntegerConstant("0"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("batLeft"),
                    Symbol("="),
                    Identifier("bat"),
                    Symbol("."),
                    Identifier("getLeft"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("batRight"),
                    Symbol("="),
                    Identifier("bat"),
                    Symbol("."),
                    Identifier("getRight"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("ballLeft"),
                    Symbol("="),
                    Identifier("ball"),
                    Symbol("."),
                    Identifier("getLeft"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("ballRight"),
                    Symbol("="),
                    Identifier("ball"),
                    Symbol("."),
                    Identifier("getRight"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("if"),
                    Symbol("("),
                    Identifier("wall"),
                    Symbol("="),
                    IntegerConstant("4"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("let"),
                    Identifier("exit"),
                    Symbol("="),
                    Symbol("("),
                    Identifier("batLeft"),
                    Symbol(">"),
                    Identifier("ballRight"),
                    Symbol(")"),
                    Symbol("|"),
                    Symbol("("),
                    Identifier("batRight"),
                    Symbol("<"),
                    Identifier("ballLeft"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("if"),
                    Symbol("("),
                    Symbol("~"),
                    Identifier("exit"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("if"),
                    Symbol("("),
                    Identifier("ballRight"),
                    Symbol("<"),
                    Symbol("("),
                    Identifier("batLeft"),
                    Symbol("+"),
                    IntegerConstant("10"),
                    Symbol(")"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("let"),
                    Identifier("bouncingDirection"),
                    Symbol("="),
                    Symbol("-"),
                    IntegerConstant("1"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("else"),
                    Symbol("{"),
                    Keyword("if"),
                    Symbol("("),
                    Identifier("ballLeft"),
                    Symbol(">"),
                    Symbol("("),
                    Identifier("batRight"),
                    Symbol("-"),
                    IntegerConstant("10"),
                    Symbol(")"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("let"),
                    Identifier("bouncingDirection"),
                    Symbol("="),
                    IntegerConstant("1"),
                    Symbol(";"),
                    Symbol("}"),
                    Symbol("}"),
                    Keyword("let"),
                    Identifier("batWidth"),
                    Symbol("="),
                    Identifier("batWidth"),
                    Symbol("-"),
                    IntegerConstant("2"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("bat"),
                    Symbol("."),
                    Identifier("setWidth"),
                    Symbol("("),
                    Identifier("batWidth"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("score"),
                    Symbol("="),
                    Identifier("score"),
                    Symbol("+"),
                    IntegerConstant("1"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Output"),
                    Symbol("."),
                    Identifier("moveCursor"),
                    Symbol("("),
                    IntegerConstant("22"),
                    Symbol(","),
                    IntegerConstant("7"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Output"),
                    Symbol("."),
                    Identifier("printInt"),
                    Symbol("("),
                    Identifier("score"),
                    Symbol(")"),
                    Symbol(";"),
                    Symbol("}"),
                    Symbol("}"),
                    Keyword("do"),
                    Identifier("ball"),
                    Symbol("."),
                    Identifier("bounce"),
                    Symbol("("),
                    Identifier("bouncingDirection"),
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

        engine = CompilationEngine("PongGame.jack")
        vm_insts = engine.compile_class(mock_tokens, SymbolTable())

        self.assertEqual(next(vm_insts), "function PongGame.new 0"),
        self.assertEqual(next(vm_insts), "push constant 7"),
        self.assertEqual(next(vm_insts), "call Memory.alloc 1"),
        self.assertEqual(next(vm_insts), "pop pointer 0"),
        self.assertEqual(next(vm_insts), "call Screen.clearScreen 0"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "push constant 50"),
        self.assertEqual(next(vm_insts), "pop this 6"),
        self.assertEqual(next(vm_insts), "push constant 230"),
        self.assertEqual(next(vm_insts), "push constant 229"),
        self.assertEqual(next(vm_insts), "push this 6"),
        self.assertEqual(next(vm_insts), "push constant 7"),
        self.assertEqual(next(vm_insts), "call Bat.new 4"),
        self.assertEqual(next(vm_insts), "pop this 0"),
        self.assertEqual(next(vm_insts), "push constant 253"),
        self.assertEqual(next(vm_insts), "push constant 222"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "push constant 511"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "push constant 229"),
        self.assertEqual(next(vm_insts), "call Ball.new 6"),
        self.assertEqual(next(vm_insts), "pop this 1"),
        self.assertEqual(next(vm_insts), "push this 1"),
        self.assertEqual(next(vm_insts), "push constant 400"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "call Ball.setDestination 3"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "push constant 238"),
        self.assertEqual(next(vm_insts), "push constant 511"),
        self.assertEqual(next(vm_insts), "push constant 240"),
        self.assertEqual(next(vm_insts), "call Screen.drawRectangle 4"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "push constant 22"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "call Output.moveCursor 2"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "push constant 8"),
        self.assertEqual(next(vm_insts), "call String.new 1"),
        self.assertEqual(next(vm_insts), "push constant 83"),
        self.assertEqual(next(vm_insts), "call String.appendChar 2"),
        self.assertEqual(next(vm_insts), "push constant 99"),
        self.assertEqual(next(vm_insts), "call String.appendChar 2"),
        self.assertEqual(next(vm_insts), "push constant 111"),
        self.assertEqual(next(vm_insts), "call String.appendChar 2"),
        self.assertEqual(next(vm_insts), "push constant 114"),
        self.assertEqual(next(vm_insts), "call String.appendChar 2"),
        self.assertEqual(next(vm_insts), "push constant 101"),
        self.assertEqual(next(vm_insts), "call String.appendChar 2"),
        self.assertEqual(next(vm_insts), "push constant 58"),
        self.assertEqual(next(vm_insts), "call String.appendChar 2"),
        self.assertEqual(next(vm_insts), "push constant 32"),
        self.assertEqual(next(vm_insts), "call String.appendChar 2"),
        self.assertEqual(next(vm_insts), "push constant 48"),
        self.assertEqual(next(vm_insts), "call String.appendChar 2"),
        self.assertEqual(next(vm_insts), "call Output.printString 1"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "pop this 3"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "pop this 4"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "pop this 2"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "pop this 5"),
        self.assertEqual(next(vm_insts), "push pointer 0"),
        self.assertEqual(next(vm_insts), "return"),
        self.assertEqual(next(vm_insts), "function PongGame.dispose 0"),
        self.assertEqual(next(vm_insts), "push argument 0"),
        self.assertEqual(next(vm_insts), "pop pointer 0"),
        self.assertEqual(next(vm_insts), "push this 0"),
        self.assertEqual(next(vm_insts), "call Bat.dispose 1"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "push this 1"),
        self.assertEqual(next(vm_insts), "call Ball.dispose 1"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "push pointer 0"),
        self.assertEqual(next(vm_insts), "call Memory.deAlloc 1"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "return"),
        self.assertEqual(next(vm_insts), "function PongGame.newInstance 0"),
        self.assertEqual(next(vm_insts), "call PongGame.new 0"),
        self.assertEqual(next(vm_insts), "pop static 0"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "return"),
        self.assertEqual(next(vm_insts), "function PongGame.getInstance 0"),
        self.assertEqual(next(vm_insts), "push static 0"),
        self.assertEqual(next(vm_insts), "return"),
        self.assertEqual(next(vm_insts), "function PongGame.run 1"),
        self.assertEqual(next(vm_insts), "push argument 0"),
        self.assertEqual(next(vm_insts), "pop pointer 0"),
        self.assertEqual(next(vm_insts), "label WHILE_EXP0"),
        self.assertEqual(next(vm_insts), "push this 3"),
        self.assertEqual(next(vm_insts), "not"),
        self.assertEqual(next(vm_insts), "not"),
        self.assertEqual(next(vm_insts), "if-goto WHILE_END0"),
        self.assertEqual(next(vm_insts), "label WHILE_EXP1"),
        self.assertEqual(next(vm_insts), "push local 0"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "eq"),
        self.assertEqual(next(vm_insts), "push this 3"),
        self.assertEqual(next(vm_insts), "not"),
        self.assertEqual(next(vm_insts), "and"),
        self.assertEqual(next(vm_insts), "not"),
        self.assertEqual(next(vm_insts), "if-goto WHILE_END1"),
        self.assertEqual(next(vm_insts), "call Keyboard.keyPressed 0"),
        self.assertEqual(next(vm_insts), "pop local 0"),
        self.assertEqual(next(vm_insts), "push this 0"),
        self.assertEqual(next(vm_insts), "call Bat.move 1"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "push pointer 0"),
        self.assertEqual(next(vm_insts), "call PongGame.moveBall 1"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "push constant 50"),
        self.assertEqual(next(vm_insts), "call Sys.wait 1"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "goto WHILE_EXP1"),
        self.assertEqual(next(vm_insts), "label WHILE_END1"),
        self.assertEqual(next(vm_insts), "push local 0"),
        self.assertEqual(next(vm_insts), "push constant 130"),
        self.assertEqual(next(vm_insts), "eq"),
        self.assertEqual(next(vm_insts), "if-goto IF_TRUE0"),
        self.assertEqual(next(vm_insts), "goto IF_FALSE0"),
        self.assertEqual(next(vm_insts), "label IF_TRUE0"),
        self.assertEqual(next(vm_insts), "push this 0"),
        self.assertEqual(next(vm_insts), "push constant 1"),
        self.assertEqual(next(vm_insts), "call Bat.setDirection 2"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "goto IF_END0"),
        self.assertEqual(next(vm_insts), "label IF_FALSE0"),
        self.assertEqual(next(vm_insts), "push local 0"),
        self.assertEqual(next(vm_insts), "push constant 132"),
        self.assertEqual(next(vm_insts), "eq"),
        self.assertEqual(next(vm_insts), "if-goto IF_TRUE1"),
        self.assertEqual(next(vm_insts), "goto IF_FALSE1"),
        self.assertEqual(next(vm_insts), "label IF_TRUE1"),
        self.assertEqual(next(vm_insts), "push this 0"),
        self.assertEqual(next(vm_insts), "push constant 2"),
        self.assertEqual(next(vm_insts), "call Bat.setDirection 2"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "goto IF_END1"),
        self.assertEqual(next(vm_insts), "label IF_FALSE1"),
        self.assertEqual(next(vm_insts), "push local 0"),
        self.assertEqual(next(vm_insts), "push constant 140"),
        self.assertEqual(next(vm_insts), "eq"),
        self.assertEqual(next(vm_insts), "if-goto IF_TRUE2"),
        self.assertEqual(next(vm_insts), "goto IF_FALSE2"),
        self.assertEqual(next(vm_insts), "label IF_TRUE2"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "not"),
        self.assertEqual(next(vm_insts), "pop this 3"),
        self.assertEqual(next(vm_insts), "label IF_FALSE2"),
        self.assertEqual(next(vm_insts), "label IF_END1"),
        self.assertEqual(next(vm_insts), "label IF_END0"),
        self.assertEqual(next(vm_insts), "label WHILE_EXP2"),
        self.assertEqual(next(vm_insts), "push local 0"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "eq"),
        self.assertEqual(next(vm_insts), "not"),
        self.assertEqual(next(vm_insts), "push this 3"),
        self.assertEqual(next(vm_insts), "not"),
        self.assertEqual(next(vm_insts), "and"),
        self.assertEqual(next(vm_insts), "not"),
        self.assertEqual(next(vm_insts), "if-goto WHILE_END2"),
        self.assertEqual(next(vm_insts), "call Keyboard.keyPressed 0"),
        self.assertEqual(next(vm_insts), "pop local 0"),
        self.assertEqual(next(vm_insts), "push this 0"),
        self.assertEqual(next(vm_insts), "call Bat.move 1"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "push pointer 0"),
        self.assertEqual(next(vm_insts), "call PongGame.moveBall 1"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "push constant 50"),
        self.assertEqual(next(vm_insts), "call Sys.wait 1"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "goto WHILE_EXP2"),
        self.assertEqual(next(vm_insts), "label WHILE_END2"),
        self.assertEqual(next(vm_insts), "goto WHILE_EXP0"),
        self.assertEqual(next(vm_insts), "label WHILE_END0"),
        self.assertEqual(next(vm_insts), "push this 3"),
        self.assertEqual(next(vm_insts), "if-goto IF_TRUE3"),
        self.assertEqual(next(vm_insts), "goto IF_FALSE3"),
        self.assertEqual(next(vm_insts), "label IF_TRUE3"),
        self.assertEqual(next(vm_insts), "push constant 10"),
        self.assertEqual(next(vm_insts), "push constant 27"),
        self.assertEqual(next(vm_insts), "call Output.moveCursor 2"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "push constant 9"),
        self.assertEqual(next(vm_insts), "call String.new 1"),
        self.assertEqual(next(vm_insts), "push constant 71"),
        self.assertEqual(next(vm_insts), "call String.appendChar 2"),
        self.assertEqual(next(vm_insts), "push constant 97"),
        self.assertEqual(next(vm_insts), "call String.appendChar 2"),
        self.assertEqual(next(vm_insts), "push constant 109"),
        self.assertEqual(next(vm_insts), "call String.appendChar 2"),
        self.assertEqual(next(vm_insts), "push constant 101"),
        self.assertEqual(next(vm_insts), "call String.appendChar 2"),
        self.assertEqual(next(vm_insts), "push constant 32"),
        self.assertEqual(next(vm_insts), "call String.appendChar 2"),
        self.assertEqual(next(vm_insts), "push constant 79"),
        self.assertEqual(next(vm_insts), "call String.appendChar 2"),
        self.assertEqual(next(vm_insts), "push constant 118"),
        self.assertEqual(next(vm_insts), "call String.appendChar 2"),
        self.assertEqual(next(vm_insts), "push constant 101"),
        self.assertEqual(next(vm_insts), "call String.appendChar 2"),
        self.assertEqual(next(vm_insts), "push constant 114"),
        self.assertEqual(next(vm_insts), "call String.appendChar 2"),
        self.assertEqual(next(vm_insts), "call Output.printString 1"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "label IF_FALSE3"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "return"),
        self.assertEqual(next(vm_insts), "function PongGame.moveBall 5"),
        self.assertEqual(next(vm_insts), "push argument 0"),
        self.assertEqual(next(vm_insts), "pop pointer 0"),
        self.assertEqual(next(vm_insts), "push this 1"),
        self.assertEqual(next(vm_insts), "call Ball.move 1"),
        self.assertEqual(next(vm_insts), "pop this 2"),
        self.assertEqual(next(vm_insts), "push this 2"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "gt"),
        self.assertEqual(next(vm_insts), "push this 2"),
        self.assertEqual(next(vm_insts), "push this 5"),
        self.assertEqual(next(vm_insts), "eq"),
        self.assertEqual(next(vm_insts), "not"),
        self.assertEqual(next(vm_insts), "and"),
        self.assertEqual(next(vm_insts), "if-goto IF_TRUE0"),
        self.assertEqual(next(vm_insts), "goto IF_FALSE0"),
        self.assertEqual(next(vm_insts), "label IF_TRUE0"),
        self.assertEqual(next(vm_insts), "push this 2"),
        self.assertEqual(next(vm_insts), "pop this 5"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "pop local 0"),
        self.assertEqual(next(vm_insts), "push this 0"),
        self.assertEqual(next(vm_insts), "call Bat.getLeft 1"),
        self.assertEqual(next(vm_insts), "pop local 1"),
        self.assertEqual(next(vm_insts), "push this 0"),
        self.assertEqual(next(vm_insts), "call Bat.getRight 1"),
        self.assertEqual(next(vm_insts), "pop local 2"),
        self.assertEqual(next(vm_insts), "push this 1"),
        self.assertEqual(next(vm_insts), "call Ball.getLeft 1"),
        self.assertEqual(next(vm_insts), "pop local 3"),
        self.assertEqual(next(vm_insts), "push this 1"),
        self.assertEqual(next(vm_insts), "call Ball.getRight 1"),
        self.assertEqual(next(vm_insts), "pop local 4"),
        self.assertEqual(next(vm_insts), "push this 2"),
        self.assertEqual(next(vm_insts), "push constant 4"),
        self.assertEqual(next(vm_insts), "eq"),
        self.assertEqual(next(vm_insts), "if-goto IF_TRUE1"),
        self.assertEqual(next(vm_insts), "goto IF_FALSE1"),
        self.assertEqual(next(vm_insts), "label IF_TRUE1"),
        self.assertEqual(next(vm_insts), "push local 1"),
        self.assertEqual(next(vm_insts), "push local 4"),
        self.assertEqual(next(vm_insts), "gt"),
        self.assertEqual(next(vm_insts), "push local 2"),
        self.assertEqual(next(vm_insts), "push local 3"),
        self.assertEqual(next(vm_insts), "lt"),
        self.assertEqual(next(vm_insts), "or"),
        self.assertEqual(next(vm_insts), "pop this 3"),
        self.assertEqual(next(vm_insts), "push this 3"),
        self.assertEqual(next(vm_insts), "not"),
        self.assertEqual(next(vm_insts), "if-goto IF_TRUE2"),
        self.assertEqual(next(vm_insts), "goto IF_FALSE2"),
        self.assertEqual(next(vm_insts), "label IF_TRUE2"),
        self.assertEqual(next(vm_insts), "push local 4"),
        self.assertEqual(next(vm_insts), "push local 1"),
        self.assertEqual(next(vm_insts), "push constant 10"),
        self.assertEqual(next(vm_insts), "add"),
        self.assertEqual(next(vm_insts), "lt"),
        self.assertEqual(next(vm_insts), "if-goto IF_TRUE3"),
        self.assertEqual(next(vm_insts), "goto IF_FALSE3"),
        self.assertEqual(next(vm_insts), "label IF_TRUE3"),
        self.assertEqual(next(vm_insts), "push constant 1"),
        self.assertEqual(next(vm_insts), "neg"),
        self.assertEqual(next(vm_insts), "pop local 0"),
        self.assertEqual(next(vm_insts), "goto IF_END3"),
        self.assertEqual(next(vm_insts), "label IF_FALSE3"),
        self.assertEqual(next(vm_insts), "push local 3"),
        self.assertEqual(next(vm_insts), "push local 2"),
        self.assertEqual(next(vm_insts), "push constant 10"),
        self.assertEqual(next(vm_insts), "sub"),
        self.assertEqual(next(vm_insts), "gt"),
        self.assertEqual(next(vm_insts), "if-goto IF_TRUE4"),
        self.assertEqual(next(vm_insts), "goto IF_FALSE4"),
        self.assertEqual(next(vm_insts), "label IF_TRUE4"),
        self.assertEqual(next(vm_insts), "push constant 1"),
        self.assertEqual(next(vm_insts), "pop local 0"),
        self.assertEqual(next(vm_insts), "label IF_FALSE4"),
        self.assertEqual(next(vm_insts), "label IF_END3"),
        self.assertEqual(next(vm_insts), "push this 6"),
        self.assertEqual(next(vm_insts), "push constant 2"),
        self.assertEqual(next(vm_insts), "sub"),
        self.assertEqual(next(vm_insts), "pop this 6"),
        self.assertEqual(next(vm_insts), "push this 0"),
        self.assertEqual(next(vm_insts), "push this 6"),
        self.assertEqual(next(vm_insts), "call Bat.setWidth 2"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "push this 4"),
        self.assertEqual(next(vm_insts), "push constant 1"),
        self.assertEqual(next(vm_insts), "add"),
        self.assertEqual(next(vm_insts), "pop this 4"),
        self.assertEqual(next(vm_insts), "push constant 22"),
        self.assertEqual(next(vm_insts), "push constant 7"),
        self.assertEqual(next(vm_insts), "call Output.moveCursor 2"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "push this 4"),
        self.assertEqual(next(vm_insts), "call Output.printInt 1"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "label IF_FALSE2"),
        self.assertEqual(next(vm_insts), "label IF_FALSE1"),
        self.assertEqual(next(vm_insts), "push this 1"),
        self.assertEqual(next(vm_insts), "push local 0"),
        self.assertEqual(next(vm_insts), "call Ball.bounce 2"),
        self.assertEqual(next(vm_insts), "pop temp 0"),
        self.assertEqual(next(vm_insts), "label IF_FALSE0"),
        self.assertEqual(next(vm_insts), "push constant 0"),
        self.assertEqual(next(vm_insts), "return"),

    def test_complex_array(self):
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
                    Symbol(","),
                    Identifier("b"),
                    Symbol(","),
                    Identifier("c"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("a"),
                    Symbol("="),
                    Identifier("Array"),
                    Symbol("."),
                    Identifier("new"),
                    Symbol("("),
                    IntegerConstant("10"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("b"),
                    Symbol("="),
                    Identifier("Array"),
                    Symbol("."),
                    Identifier("new"),
                    Symbol("("),
                    IntegerConstant("5"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("c"),
                    Symbol("="),
                    Identifier("Array"),
                    Symbol("."),
                    Identifier("new"),
                    Symbol("("),
                    IntegerConstant("1"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("a"),
                    Symbol("["),
                    IntegerConstant("3"),
                    Symbol("]"),
                    Symbol("="),
                    IntegerConstant("2"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("a"),
                    Symbol("["),
                    IntegerConstant("4"),
                    Symbol("]"),
                    Symbol("="),
                    IntegerConstant("8"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("a"),
                    Symbol("["),
                    IntegerConstant("5"),
                    Symbol("]"),
                    Symbol("="),
                    IntegerConstant("4"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("b"),
                    Symbol("["),
                    Identifier("a"),
                    Symbol("["),
                    IntegerConstant("3"),
                    Symbol("]"),
                    Symbol("]"),
                    Symbol("="),
                    Identifier("a"),
                    Symbol("["),
                    IntegerConstant("3"),
                    Symbol("]"),
                    Symbol("+"),
                    IntegerConstant("3"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("a"),
                    Symbol("["),
                    Identifier("b"),
                    Symbol("["),
                    Identifier("a"),
                    Symbol("["),
                    IntegerConstant("3"),
                    Symbol("]"),
                    Symbol("]"),
                    Symbol("]"),
                    Symbol("="),
                    Identifier("a"),
                    Symbol("["),
                    Identifier("a"),
                    Symbol("["),
                    IntegerConstant("5"),
                    Symbol("]"),
                    Symbol("]"),
                    Symbol("*"),
                    Identifier("b"),
                    Symbol("["),
                    Symbol("("),
                    Symbol("("),
                    IntegerConstant("7"),
                    Symbol("-"),
                    Identifier("a"),
                    Symbol("["),
                    IntegerConstant("3"),
                    Symbol("]"),
                    Symbol(")"),
                    Symbol("-"),
                    Identifier("Main"),
                    Symbol("."),
                    Identifier("double"),
                    Symbol("("),
                    IntegerConstant("2"),
                    Symbol(")"),
                    Symbol(")"),
                    Symbol("+"),
                    IntegerConstant("1"),
                    Symbol("]"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("c"),
                    Symbol("["),
                    IntegerConstant("0"),
                    Symbol("]"),
                    Symbol("="),
                    Keyword("null"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("c"),
                    Symbol("="),
                    Identifier("c"),
                    Symbol("["),
                    IntegerConstant("0"),
                    Symbol("]"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Output"),
                    Symbol("."),
                    Identifier("printString"),
                    Symbol("("),
                    StringConstant("Test 1: expected result: 5; actual result: "),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Output"),
                    Symbol("."),
                    Identifier("printInt"),
                    Symbol("("),
                    Identifier("b"),
                    Symbol("["),
                    IntegerConstant("2"),
                    Symbol("]"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Output"),
                    Symbol("."),
                    Identifier("println"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Output"),
                    Symbol("."),
                    Identifier("printString"),
                    Symbol("("),
                    StringConstant("Test 2: expected result: 40; actual result: "),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Output"),
                    Symbol("."),
                    Identifier("printInt"),
                    Symbol("("),
                    Identifier("a"),
                    Symbol("["),
                    IntegerConstant("5"),
                    Symbol("]"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Output"),
                    Symbol("."),
                    Identifier("println"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Output"),
                    Symbol("."),
                    Identifier("printString"),
                    Symbol("("),
                    StringConstant("Test 3: expected result: 0; actual result: "),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Output"),
                    Symbol("."),
                    Identifier("printInt"),
                    Symbol("("),
                    Identifier("c"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Output"),
                    Symbol("."),
                    Identifier("println"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("c"),
                    Symbol("="),
                    Keyword("null"),
                    Symbol(";"),
                    Keyword("if"),
                    Symbol("("),
                    Identifier("c"),
                    Symbol("="),
                    Keyword("null"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("do"),
                    Identifier("Main"),
                    Symbol("."),
                    Identifier("fill"),
                    Symbol("("),
                    Identifier("a"),
                    Symbol(","),
                    IntegerConstant("10"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("c"),
                    Symbol("="),
                    Identifier("a"),
                    Symbol("["),
                    IntegerConstant("3"),
                    Symbol("]"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("c"),
                    Symbol("["),
                    IntegerConstant("1"),
                    Symbol("]"),
                    Symbol("="),
                    IntegerConstant("33"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("c"),
                    Symbol("="),
                    Identifier("a"),
                    Symbol("["),
                    IntegerConstant("7"),
                    Symbol("]"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("c"),
                    Symbol("["),
                    IntegerConstant("1"),
                    Symbol("]"),
                    Symbol("="),
                    IntegerConstant("77"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("b"),
                    Symbol("="),
                    Identifier("a"),
                    Symbol("["),
                    IntegerConstant("3"),
                    Symbol("]"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("b"),
                    Symbol("["),
                    IntegerConstant("1"),
                    Symbol("]"),
                    Symbol("="),
                    Identifier("b"),
                    Symbol("["),
                    IntegerConstant("1"),
                    Symbol("]"),
                    Symbol("+"),
                    Identifier("c"),
                    Symbol("["),
                    IntegerConstant("1"),
                    Symbol("]"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("do"),
                    Identifier("Output"),
                    Symbol("."),
                    Identifier("printString"),
                    Symbol("("),
                    StringConstant("Test 4: expected result: 77; actual result: "),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Output"),
                    Symbol("."),
                    Identifier("printInt"),
                    Symbol("("),
                    Identifier("c"),
                    Symbol("["),
                    IntegerConstant("1"),
                    Symbol("]"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Output"),
                    Symbol("."),
                    Identifier("println"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Output"),
                    Symbol("."),
                    Identifier("printString"),
                    Symbol("("),
                    StringConstant("Test 5: expected result: 110; actual result: "),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Output"),
                    Symbol("."),
                    Identifier("printInt"),
                    Symbol("("),
                    Identifier("b"),
                    Symbol("["),
                    IntegerConstant("1"),
                    Symbol("]"),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("do"),
                    Identifier("Output"),
                    Symbol("."),
                    Identifier("println"),
                    Symbol("("),
                    Symbol(")"),
                    Symbol(";"),
                    Keyword("return"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("function"),
                    Keyword("int"),
                    Identifier("double"),
                    Symbol("("),
                    Keyword("int"),
                    Identifier("a"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("return"),
                    Identifier("a"),
                    Symbol("*"),
                    IntegerConstant("2"),
                    Symbol(";"),
                    Symbol("}"),
                    Keyword("function"),
                    Keyword("void"),
                    Identifier("fill"),
                    Symbol("("),
                    Identifier("Array"),
                    Identifier("a"),
                    Symbol(","),
                    Keyword("int"),
                    Identifier("size"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("while"),
                    Symbol("("),
                    Identifier("size"),
                    Symbol(">"),
                    IntegerConstant("0"),
                    Symbol(")"),
                    Symbol("{"),
                    Keyword("let"),
                    Identifier("size"),
                    Symbol("="),
                    Identifier("size"),
                    Symbol("-"),
                    IntegerConstant("1"),
                    Symbol(";"),
                    Keyword("let"),
                    Identifier("a"),
                    Symbol("["),
                    Identifier("size"),
                    Symbol("]"),
                    Symbol("="),
                    Identifier("Array"),
                    Symbol("."),
                    Identifier("new"),
                    Symbol("("),
                    IntegerConstant("3"),
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

        engine = CompilationEngine("Main.jack")
        vm_insts = engine.compile_class(mock_tokens, SymbolTable())

        self.assertEqual(next(vm_insts), "function Main.main 3")
        self.assertEqual(next(vm_insts), "push constant 10")
        self.assertEqual(next(vm_insts), "call Array.new 1")
        self.assertEqual(next(vm_insts), "pop local 0")
        self.assertEqual(next(vm_insts), "push constant 5")
        self.assertEqual(next(vm_insts), "call Array.new 1")
        self.assertEqual(next(vm_insts), "pop local 1")
        self.assertEqual(next(vm_insts), "push constant 1")
        self.assertEqual(next(vm_insts), "call Array.new 1")
        self.assertEqual(next(vm_insts), "pop local 2")
        self.assertEqual(next(vm_insts), "push constant 3")
        self.assertEqual(next(vm_insts), "push local 0")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push constant 2")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push temp 0")
        self.assertEqual(next(vm_insts), "pop that 0")
        self.assertEqual(next(vm_insts), "push constant 4")
        self.assertEqual(next(vm_insts), "push local 0")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push constant 8")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push temp 0")
        self.assertEqual(next(vm_insts), "pop that 0")
        self.assertEqual(next(vm_insts), "push constant 5")
        self.assertEqual(next(vm_insts), "push local 0")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push constant 4")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push temp 0")
        self.assertEqual(next(vm_insts), "pop that 0")
        self.assertEqual(next(vm_insts), "push constant 3")
        self.assertEqual(next(vm_insts), "push local 0")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push that 0")
        self.assertEqual(next(vm_insts), "push local 1")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push constant 3")
        self.assertEqual(next(vm_insts), "push local 0")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push that 0")
        self.assertEqual(next(vm_insts), "push constant 3")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push temp 0")
        self.assertEqual(next(vm_insts), "pop that 0")
        self.assertEqual(next(vm_insts), "push constant 3")
        self.assertEqual(next(vm_insts), "push local 0")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push that 0")
        self.assertEqual(next(vm_insts), "push local 1")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push that 0")
        self.assertEqual(next(vm_insts), "push local 0")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push constant 5")
        self.assertEqual(next(vm_insts), "push local 0")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push that 0")
        self.assertEqual(next(vm_insts), "push local 0")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push that 0")
        self.assertEqual(next(vm_insts), "push constant 7")
        self.assertEqual(next(vm_insts), "push constant 3")
        self.assertEqual(next(vm_insts), "push local 0")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push that 0")
        self.assertEqual(next(vm_insts), "sub")
        self.assertEqual(next(vm_insts), "push constant 2")
        self.assertEqual(next(vm_insts), "call Main.double 1")
        self.assertEqual(next(vm_insts), "sub")
        self.assertEqual(next(vm_insts), "push constant 1")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push local 1")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push that 0")
        self.assertEqual(next(vm_insts), "call Math.multiply 2")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push temp 0")
        self.assertEqual(next(vm_insts), "pop that 0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "push local 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push temp 0")
        self.assertEqual(next(vm_insts), "pop that 0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "push local 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push that 0")
        self.assertEqual(next(vm_insts), "pop local 2")
        self.assertEqual(next(vm_insts), "push constant 43")
        self.assertEqual(next(vm_insts), "call String.new 1")
        self.assertEqual(next(vm_insts), "push constant 84")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 115")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 49")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 58")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 120")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 112")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 99")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 100")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 114")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 115")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 117")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 108")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 58")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 53")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 59")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 97")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 99")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 117")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 97")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 108")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 114")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 115")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 117")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 108")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 58")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "call Output.printString 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push constant 2")
        self.assertEqual(next(vm_insts), "push local 1")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push that 0")
        self.assertEqual(next(vm_insts), "call Output.printInt 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "call Output.println 0")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push constant 44")
        self.assertEqual(next(vm_insts), "call String.new 1")
        self.assertEqual(next(vm_insts), "push constant 84")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 115")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 50")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 58")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 120")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 112")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 99")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 100")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 114")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 115")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 117")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 108")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 58")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 52")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 48")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 59")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 97")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 99")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 117")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 97")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 108")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 114")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 115")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 117")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 108")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 58")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "call Output.printString 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push constant 5")
        self.assertEqual(next(vm_insts), "push local 0")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push that 0")
        self.assertEqual(next(vm_insts), "call Output.printInt 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "call Output.println 0")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push constant 43")
        self.assertEqual(next(vm_insts), "call String.new 1")
        self.assertEqual(next(vm_insts), "push constant 84")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 115")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 51")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 58")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 120")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 112")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 99")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 100")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 114")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 115")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 117")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 108")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 58")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 48")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 59")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 97")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 99")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 117")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 97")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 108")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 114")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 115")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 117")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 108")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 58")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "call Output.printString 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push local 2")
        self.assertEqual(next(vm_insts), "call Output.printInt 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "call Output.println 0")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "pop local 2")
        self.assertEqual(next(vm_insts), "push local 2")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "eq")
        self.assertEqual(next(vm_insts), "if-goto IF_TRUE0")
        self.assertEqual(next(vm_insts), "goto IF_FALSE0")
        self.assertEqual(next(vm_insts), "label IF_TRUE0")
        self.assertEqual(next(vm_insts), "push local 0")
        self.assertEqual(next(vm_insts), "push constant 10")
        self.assertEqual(next(vm_insts), "call Main.fill 2")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push constant 3")
        self.assertEqual(next(vm_insts), "push local 0")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push that 0")
        self.assertEqual(next(vm_insts), "pop local 2")
        self.assertEqual(next(vm_insts), "push constant 1")
        self.assertEqual(next(vm_insts), "push local 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push constant 33")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push temp 0")
        self.assertEqual(next(vm_insts), "pop that 0")
        self.assertEqual(next(vm_insts), "push constant 7")
        self.assertEqual(next(vm_insts), "push local 0")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push that 0")
        self.assertEqual(next(vm_insts), "pop local 2")
        self.assertEqual(next(vm_insts), "push constant 1")
        self.assertEqual(next(vm_insts), "push local 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push constant 77")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push temp 0")
        self.assertEqual(next(vm_insts), "pop that 0")
        self.assertEqual(next(vm_insts), "push constant 3")
        self.assertEqual(next(vm_insts), "push local 0")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push that 0")
        self.assertEqual(next(vm_insts), "pop local 1")
        self.assertEqual(next(vm_insts), "push constant 1")
        self.assertEqual(next(vm_insts), "push local 1")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push constant 1")
        self.assertEqual(next(vm_insts), "push local 1")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push that 0")
        self.assertEqual(next(vm_insts), "push constant 1")
        self.assertEqual(next(vm_insts), "push local 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push that 0")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push temp 0")
        self.assertEqual(next(vm_insts), "pop that 0")
        self.assertEqual(next(vm_insts), "label IF_FALSE0")
        self.assertEqual(next(vm_insts), "push constant 44")
        self.assertEqual(next(vm_insts), "call String.new 1")
        self.assertEqual(next(vm_insts), "push constant 84")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 115")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 52")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 58")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 120")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 112")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 99")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 100")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 114")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 115")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 117")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 108")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 58")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 55")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 55")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 59")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 97")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 99")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 117")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 97")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 108")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 114")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 115")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 117")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 108")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 58")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "call Output.printString 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push constant 1")
        self.assertEqual(next(vm_insts), "push local 2")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push that 0")
        self.assertEqual(next(vm_insts), "call Output.printInt 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "call Output.println 0")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push constant 45")
        self.assertEqual(next(vm_insts), "call String.new 1")
        self.assertEqual(next(vm_insts), "push constant 84")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 115")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 53")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 58")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 120")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 112")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 99")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 100")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 114")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 115")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 117")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 108")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 58")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 49")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 49")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 48")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 59")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 97")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 99")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 117")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 97")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 108")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 114")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 101")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 115")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 117")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 108")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 116")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 58")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "push constant 32")
        self.assertEqual(next(vm_insts), "call String.appendChar 2")
        self.assertEqual(next(vm_insts), "call Output.printString 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push constant 1")
        self.assertEqual(next(vm_insts), "push local 1")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push that 0")
        self.assertEqual(next(vm_insts), "call Output.printInt 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "call Output.println 0")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "return")
        self.assertEqual(next(vm_insts), "function Main.double 0")
        self.assertEqual(next(vm_insts), "push argument 0")
        self.assertEqual(next(vm_insts), "push constant 2")
        self.assertEqual(next(vm_insts), "call Math.multiply 2")
        self.assertEqual(next(vm_insts), "return")
        self.assertEqual(next(vm_insts), "function Main.fill 0")
        self.assertEqual(next(vm_insts), "label WHILE_EXP0")
        self.assertEqual(next(vm_insts), "push argument 1")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "gt")
        self.assertEqual(next(vm_insts), "not")
        self.assertEqual(next(vm_insts), "if-goto WHILE_END0")
        self.assertEqual(next(vm_insts), "push argument 1")
        self.assertEqual(next(vm_insts), "push constant 1")
        self.assertEqual(next(vm_insts), "sub")
        self.assertEqual(next(vm_insts), "pop argument 1")
        self.assertEqual(next(vm_insts), "push argument 1")
        self.assertEqual(next(vm_insts), "push argument 0")
        self.assertEqual(next(vm_insts), "add")
        self.assertEqual(next(vm_insts), "push constant 3")
        self.assertEqual(next(vm_insts), "call Array.new 1")
        self.assertEqual(next(vm_insts), "pop temp 0")
        self.assertEqual(next(vm_insts), "pop pointer 1")
        self.assertEqual(next(vm_insts), "push temp 0")
        self.assertEqual(next(vm_insts), "pop that 0")
        self.assertEqual(next(vm_insts), "goto WHILE_EXP0")
        self.assertEqual(next(vm_insts), "label WHILE_END0")
        self.assertEqual(next(vm_insts), "push constant 0")
        self.assertEqual(next(vm_insts), "return")
