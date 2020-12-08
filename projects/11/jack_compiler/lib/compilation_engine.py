import pdb
from .jack_token import Keyword, Identifier, Symbol, IntegerConstant, StringConstant
from .symbol_table import SymbolTable
from .vm_writer import VMWriter


class CompilationEngine:
    TAB_SIZE = 2

    def __init__(self, srouce_file_name):
        self.source_file_name = srouce_file_name
        self.class_name: str = None
        self.sub_routine_name: str = None
        self.sub_routine_kind: str = None
        self.sub_routine_return_type: str = None
        self.sub_routine_arg_count: int = 0  # should this be part of the symbol table because it contains other state as well?
        self.if_level = -1

    def compile_term(self, tokens, symbol_table, lvl=0):
        print("DEBUG", (lvl + 1) * " ", "compile_term")
        if isinstance(tokens.peek(), IntegerConstant):
            # consume int constant
            num = next(tokens)
            yield f"push constant {num.val}"
        elif isinstance(tokens.peek(), StringConstant):
            # consume string constant
            string = next(tokens)
            yield f"Sys.alloc({len(string)})"
            for s in string:
                yield f"push {s}"
        elif isinstance(tokens.peek(), Keyword):
            # consume keyword constant (true/false/null)
            const_keyword = next(tokens).val
            print("DEBUG", (lvl + 1) * " ", "const_keyword:", const_keyword)
            if const_keyword == "true":
                yield f"push constant 0"
                yield f"not"
            elif const_keyword == "false":
                yield f"push constant 0"
            elif const_keyword == "null":
                yield f"push constant 0"
            elif const_keyword == "this":
                # TODO: need to tell if this term comes from Class.method(expr) or return expr;
                if self.sub_routine_kind == "constructor":
                    yield f"push pointer 0"
                else:
                    yield f"push {symbol_table.kind_of('this')} {symbol_table.index_of('this')}"
            else:
                raise ValueError(f"Invalid constant keyword:{const_keyword}")
        elif isinstance(tokens.peek(), Identifier):
            identifier = tokens.peek().val
            print("DEBUG", (lvl + 1) * " ", "identifier:", identifier)
            if tokens[1] == Symbol("["):
                var_name = next(tokens).val  # varName
                next(tokens).to_xml(lvl + 1)  # [
                for i in self.compile_expression(tokens, symbol_table, lvl + 1):
                    yield i
                next(tokens).to_xml(lvl + 1)  # ]
            elif tokens[1] in [Symbol("("), Symbol(".")]:
                # subRoutineCall
                for i in self.compile_subroutine_call(tokens, symbol_table, lvl + 1):
                    yield i
            else:  # regular var
                var_name = next(tokens).val  # varName
                SEGMENT_MAP = {"var": "local", "field": "this", "argument": "argument"}
                yield f"push {SEGMENT_MAP[symbol_table.kind_of(var_name)]} {symbol_table.index_of(var_name)}"
        elif tokens.peek() == Symbol("("):
            next(tokens).to_xml(lvl + 1)  # (
            for i in self.compile_expression(tokens, symbol_table, lvl + 1):
                yield i
            next(tokens).to_xml(lvl + 1)  # )
        elif tokens.peek() in [Symbol("-"), Symbol("~")]:
            op = next(tokens)
            for i in self.compile_term(tokens, symbol_table, lvl + 1):
                yield i
            yield "neg" if op.val == "-" else "not"
        else:
            raise ValueError(f"invalid token {tokens.peek()}")

    def compile_expression(self, tokens, symbol_table, lvl=0) -> str:
        if tokens.peek() in [
            Symbol("="),
            Symbol(")"),
            Symbol("]"),
            Symbol(";"),
            Symbol("}"),
        ]:
            return

        # caller handles the starting([) and enclosing(]) brackets.
        for i in self.compile_term(tokens, symbol_table, lvl + 1):
            yield i
        op = None
        if tokens.peek() in [
            Symbol(x) for x in ["+", "-", "*", "/", "&", "|", "<", ">", "="]
        ]:
            op = next(tokens)  # op
            for i in self.compile_expression(tokens, symbol_table, lvl + 1):
                yield i
        if op:
            # TODO: handle minus operation, how to differentiate from neg?
            if op.val == "+":
                yield f"add"
            elif op.val == "*":
                yield f"call Math.multiply 2"
            elif op.val == "-":
                yield f"sub"
            elif op.val == "/":
                yield f"call Math.divide 2"
            elif op.val == "&":
                yield f"and"
            elif op.val == "|":
                yield f"or"
            elif op.val == "=":
                yield f"eq"
            elif op.val == ">":
                yield f"gt"
            elif op.val == "<":
                yield f"lt"
            else:
                raise ValueError(f"Operator not supported: {op}")

    def compile_expression_list(self, tokens, symbol_table, lvl=0):
        print("DEBUG", (lvl + 1) * " ", "compile_expression_list")
        if tokens.peek() == Symbol(")"):
            return

        self.sub_routine_arg_count = 1
        for i in self.compile_expression(tokens, symbol_table, lvl + 1):
            yield i
        while tokens.peek() == Symbol(","):
            self.sub_routine_arg_count += 1
            next(tokens)  # ,
            for i in self.compile_expression(tokens, symbol_table, lvl + 1):
                yield i

    def compile_subroutine_call(self, tokens, symbol_table, lvl=0):
        print("DEBUG", (lvl + 1) * " ", "compile_subroutine_call")
        name = next(tokens).val  # subroutine name | (className | varName)

        method_name = None
        if tokens.peek() == Symbol("."):
            next(tokens)  # .
            method_name = next(tokens).val  # subroutineName

        next(tokens)  # (
        for i in self.compile_expression_list(tokens, symbol_table, lvl + 1):
            yield i
        next(tokens)  # )

        if method_name:
            yield f"call {name}.{method_name} {self.sub_routine_arg_count}"
            yield "pop temp 0"
        else:
            # calling an object method
            yield "push pointer 0"
            yield f"call {self.class_name}.{name} {self.sub_routine_arg_count + 1}"
            yield "pop temp 0"
        # TODO remove this stateful sub_routine_arg_count global variable
        self.sub_routine_arg_count = 0

    def compile_statements(self, tokens, symbol_table, lvl=0) -> str:
        if tokens.peek() == Symbol("}"):
            return

        while tokens and tokens.peek() in [
            Keyword("let"),
            Keyword("do"),
            Keyword("if"),
            Keyword("while"),
            Keyword("return"),
        ]:
            for i in self.compile_statement(tokens, symbol_table, lvl + 1):
                yield i

    def compile_statement(self, tokens, symbol_table, lvl=0) -> str:
        if tokens.peek() == Keyword("let"):
            print("DEBUG", (lvl + 1) * " ", "let_statement")

            next(tokens)  # let
            var_name = next(tokens).val  # varName

            if tokens.peek() == Symbol("="):
                next(tokens)  # "="
                for i in self.compile_expression(
                    tokens, symbol_table, lvl + 2
                ):  # expression
                    yield i
                next(tokens)  # ";"

                SEGMENT_MAP = {"var": "local", "field": "this"}
                yield f"pop {SEGMENT_MAP[symbol_table.kind_of(var_name)]} {symbol_table.index_of(var_name)}"
            elif tokens.peek() == Symbol("["):
                next(tokens).to_xml(lvl + 2)  # [
                for i in self.compile_expression(
                    tokens, symbol_table, lvl + 2
                ):  # expression
                    yield i
                next(tokens).to_xml(lvl + 2)  # "]"
                next(tokens).to_xml(lvl + 2)  # =
                for i in self.compile_expression(tokens, symbol_table, lvl + 2):
                    yield i
                next(tokens).to_xml(lvl + 2)  # ;
            else:
                raise ValueError(f"{tokens.peek()} invalid.")

        elif tokens.peek() == Keyword("if"):
            self.if_level += 1
            print("DEBUG", (lvl + 1) * " ", "if_statement")

            next(tokens)  # if
            next(tokens)  # (
            for i in self.compile_expression(tokens, symbol_table, lvl + 2):
                yield i
            next(tokens)  # )

            next(tokens)  # {
            if_statements = [*self.compile_statements(tokens, symbol_table, lvl + 2)]
            next(tokens)  # }

            else_statements = []
            if tokens and tokens.peek() == Keyword("else"):
                next(tokens)  # else
                next(tokens)  # {
                else_statements = [
                    *self.compile_statements(tokens, symbol_table, lvl + 2)
                ]
                next(tokens)  # }

            yield f"if-goto IF_TRUE{self.if_level}"
            yield f"goto IF_FALSE{self.if_level}"
            yield f"label IF_TRUE{self.if_level}"
            for i in if_statements:
                yield i
            yield f"goto IF_END{self.if_level}"
            yield f"label IF_FALSE{self.if_level}"
            for i in else_statements:
                yield i
            yield f"label IF_END{self.if_level}"
            self.if_level -= 1
        elif tokens.peek() == Keyword("while"):
            print("DEBUG", (lvl + 1) * " ", "while_statement")

            yield f"label WHILE_EXP0"
            next(tokens)  # while
            next(tokens)  # (
            for i in self.compile_expression(tokens, symbol_table, lvl + 2):
                yield i
            next(tokens)  # )
            yield "not"
            yield "if-goto WHILE_END0"
            next(tokens)  # {
            for i in self.compile_statements(tokens, symbol_table, lvl + 2):
                yield i
            next(tokens)  # }
            yield "goto WHILE_EXP0"
            yield "label WHILE_END0"

        elif tokens.peek() == Keyword("do"):
            print("DEBUG", (lvl + 1) * " ", "do_statement")
            next(tokens)  # do
            for i in self.compile_subroutine_call(tokens, symbol_table, lvl + 2):
                yield i
            next(tokens)  # ;
        elif tokens.peek() == Keyword("return"):
            print("DEBUG", (lvl + 1) * " ", "return_statement")
            # TODO: handle return; keep state for sub_method return type
            next(tokens)  # return
            if tokens.peek() != Symbol(";"):
                for i in self.compile_expression(tokens, symbol_table, lvl + 2):
                    yield i
            next(tokens)  # ;

            if self.sub_routine_return_type == "void":
                yield "push constant 0"
            yield "return"

        else:
            raise ValueError(f"invalid token: {tokens.peek()}")

    def compile_var_dec(self, tokens, symbol_table, lvl=0):
        print("DEBUG", (lvl + 1) * " ", "compile_var_dec")
        # inside subroutine_body, symbols should be LOL
        next(tokens)  # 'var'
        type = next(tokens)  # type
        var_name = next(tokens).val  # varName
        symbol_table.define(var_name, type, "var")

        if tokens.peek() == Symbol(";"):
            next(tokens)
        elif tokens.peek() == Symbol(","):
            while tokens.peek() != Symbol(";"):
                next(tokens)  # ,
                var_name = next(tokens).val  # varName
                symbol_table.define(var_name, type, "var")

            next(tokens).to_xml(lvl + 2)  # ;
        else:
            raise ValueError(f"invalid token: {tokens.peek()}")

    def compile_subroutine_body(self, tokens, symbol_table, lvl=0):
        next(tokens)  # {
        while tokens.peek() == Keyword("var"):
            self.compile_var_dec(tokens, symbol_table, lvl + 3)

        while tokens.peek() in [
            Keyword("let"),
            Keyword("if"),
            Keyword("while"),
            Keyword("do"),
            Keyword("return"),
        ]:
            for i in self.compile_statements(tokens, symbol_table, lvl + 2):
                yield i
        next(tokens).to_xml(lvl + 2)  # }

    def compile_parameter_list(self, tokens, symbol_table, lvl=0):
        if tokens.peek() == Symbol(")"):
            return

        type = next(tokens).val  # type
        name = next(tokens).val
        symbol_table.define(name, type, "argument")
        while tokens.peek() == Symbol(","):
            next(tokens)  # ,
            type = next(tokens)  # type
            name = next(tokens).val  # varName
            symbol_table.define(name, type, "argument")

    def compile_subroutine_dec(self, tokens, symbol_table, lvl=0):
        # TODO: handle constructor and method
        symbol_table.start_subroutine()
        self.sub_routine_kind = next(tokens).val  # (constructor | function | method)
        self.sub_routine_return_type = next(tokens).val  # void | int | String
        self.sub_routine_name = next(tokens).val  # subroutine_name

        if self.sub_routine_kind == "method":
            symbol_table.define("this", self.class_name, "pointer")
            # align this object with allocated memory address
            yield "push argument 0"
            yield "pop pointer 0"

        next(tokens)  # (
        self.compile_parameter_list(tokens, symbol_table, lvl + 2)
        next(tokens)  # )
        for i in self.compile_subroutine_body(tokens, symbol_table, lvl + 2):
            yield i

    def compile_class_var_dec(self, tokens, symbol_table, lvl=0):
        kind = next(tokens).val  # static|field
        type = next(tokens).val  # int|string etc
        var_name = next(tokens).val  # varName

        symbol_table.define(var_name, type, kind)
        if tokens.peek() == Symbol(";"):
            next(tokens)  # ;
        elif tokens.peek() == Symbol(","):
            while tokens.peek() != Symbol(";"):
                next(tokens)  # ,
                var_name = next(tokens).val  # varName
                symbol_table.define(var_name, type, kind)
            next(tokens)  # ;
        else:
            raise ValueError(f"invalid token: {tokens.peek()}")

    def compile_class(self, tokens, symbol_table: SymbolTable, lvl=0):
        next(tokens).to_xml(lvl + 1)  # class
        self.class_name = next(tokens).val  # className
        next(tokens).to_xml(lvl + 1)  # {
        while tokens.peek() in [Keyword("static"), Keyword("field")]:
            self.compile_class_var_dec(tokens, symbol_table, lvl + 1)

        while tokens.peek() in [
            Keyword("constructor"),
            Keyword("function"),
            Keyword("method"),
        ]:
            sub_routine_insts = [
                *self.compile_subroutine_dec(tokens, symbol_table, lvl + 1)
            ]

            yield f"function {self.class_name}.{self.sub_routine_name} {symbol_table.var_count['var']}"
            if self.sub_routine_kind == "constructor":
                # allocate RAM slot for newly created object
                yield f"push constant {symbol_table.var_count['field']}"
                yield "call Memory.alloc 1"
                yield "pop pointer 0"
            for i in sub_routine_insts:
                yield i

        next(tokens).to_xml(lvl + 1)  # }

    def parse(self, tokens, symbol_table):
        yield self.compile_class(tokens, symbol_table, lvl=1)
