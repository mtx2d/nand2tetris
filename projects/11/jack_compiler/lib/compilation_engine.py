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

    def compile_var_dec(self, tokens, symbol_table, lvl=0):
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
                for i in VMWriter.write_push("local"):
                    yield i

            next(tokens).to_xml(lvl + 2)  # ;
        else:
            raise ValueError(f"invalid token: {tokens.peek()}")

    def compile_term(self, tokens, symbol_table, lvl=0):
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
            next(tokens).to_xml(lvl + 1)
        elif isinstance(tokens.peek(), Identifier):
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
            else:
                var_name = next(tokens).val  # varName
                segment = symbol_table.kind_of(var_name)
                idx = symbol_table.index_of(var_name)
                yield f"pop local {idx}"
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
            if op.val == "+":
                yield f"add"
            elif op.val == "*":
                yield f"call Math.multiply 2"
            elif op.val == "-":
                yield f"neg"
            else:
                raise ValueError("Operator not supported: {op}")

    def compile_expression_list(self, tokens, symbol_table, lvl=0):
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
        else:
            yield f"call {name} {self.sub_routine_arg_count}"

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

            next(tokens).to_xml(lvl + 2)  # let
            var_name = next(tokens).to_xml(lvl + 2)  # varName

            if tokens.peek() == Symbol("="):
                next(tokens).to_xml(lvl + 2)  # "="
                for i in self.compile_expression(
                    tokens, symbol_table, lvl + 2
                ):  # expression
                    yield i
                next(tokens).to_xml(lvl + 2)  # ";"
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
            yield f"{' ' * self.TAB_SIZE * (lvl + 1)}<ifStatement>"

            yield next(tokens).to_xml(lvl + 2)  # if
            yield next(tokens).to_xml(lvl + 2)  # (
            for i in self.compile_expression(tokens, symbol_table, lvl + 2):
                yield i
            yield next(tokens).to_xml(lvl + 2)  # )

            yield next(tokens).to_xml(lvl + 2)  # {
            for i in self.compile_statements(tokens, symbol_table, lvl + 2):
                yield i
            yield next(tokens).to_xml(lvl + 2)  # }

            if tokens and tokens.peek() == Keyword("else"):
                yield next(tokens).to_xml(lvl + 2)  # else
                yield next(tokens).to_xml(lvl + 2)  # {
                for i in self.compile_statements(tokens, symbol_table, lvl + 2):
                    yield i
                yield next(tokens).to_xml(lvl + 2)  # }
            yield f"{' ' * self.TAB_SIZE * (lvl + 1)}</ifStatement>"
        elif tokens.peek() == Keyword("while"):
            yield f"{' ' * self.TAB_SIZE * (lvl + 1)}<whileStatement>"

            yield next(tokens).to_xml(lvl + 2)  # while
            yield next(tokens).to_xml(lvl + 2)  # (
            yield self.compile_expression(tokens, symbol_table, lvl + 2)
            yield next(tokens).to_xml(lvl + 2)  # )

            yield next(tokens).to_xml(lvl + 2)  # {
            yield self.compile_statements(tokens, symbol_table, lvl + 2)
            yield next(tokens).to_xml(lvl + 2)  # }
            yield f"{' ' * self.TAB_SIZE * (lvl + 1)}</whileStatement>"

        elif tokens.peek() == Keyword("do"):
            next(tokens)  # do
            for i in self.compile_subroutine_call(tokens, symbol_table, lvl + 2):
                yield i
            next(tokens)  # ;
            # if invoked a void sub_routine
            if self.sub_routine_return_type == "void":
                yield "pop temp 0"
        elif tokens.peek() == Keyword("return"):
            # TODO: handle return; keep state for sub_method return type
            next(tokens)  # return
            if tokens.peek() != Symbol(";"):
                for i in self.compile_expression(tokens, symbol_table, lvl + 2):
                    yield i

            # if this sub_routine itself return void
            yield "push constant 0"
            yield "return"
            next(tokens).to_xml(lvl + 2)  # ;

        else:
            raise ValueError(f"invalid token: {tokens.peek()}")

    def compile_subroutine_body(self, tokens, symbol_table, lvl=0):
        next(tokens)  # {
        while tokens.peek() == Keyword("var"):
            for i in self.compile_var_dec(tokens, symbol_table, lvl + 2):
                yield i

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

    def compile_type(self, tokens, symbol_table, lvl=0):
        yield next(tokens).to_xml(lvl + 1)

    def compile_parameter_list(self, tokens, symbol_table, lvl=0):
        if tokens.peek() == Symbol(")"):
            return

        type = next(tokens)  # type
        name = next(tokens).to_xml(lvl + 2)
        symbol_table.define(name, type, SymbolTable.Kind.VAR)
        while tokens.peek() == Symbol(","):
            yield next(tokens).to_xml(lvl + 2)  # ,
            for i in self.compile_type(tokens, symbol_table, lvl + 2):  # type
                yield i
            yield next(tokens).to_xml(lvl + 2)  # varName

    def compile_subroutine_dec(self, tokens, symbol_table, lvl=0):
        symbol_table.start_subroutine()
        self.sub_routine_kind = next(tokens).val  # (constructor | function | method)
        self.sub_routine_return_type = next(tokens).val  # void | int | String
        self.sub_routine_name = next(tokens).val  # subroutine_name

        next(tokens).to_xml(lvl + 2)  # (
        for i in self.compile_parameter_list(tokens, symbol_table, lvl + 2):
            yield i

        next(tokens).to_xml(lvl + 2)  # )
        for i in self.compile_subroutine_body(tokens, symbol_table, lvl + 2):
            yield i

    def compile_class_var_dec(self, tokens, symbol_table, lvl=0):
        kind = next(tokens).val  # static|field
        type = next(tokens).val  # int|string etc
        var_name = next(tokens).val  # varName

        if tokens.peek() == Symbol(";"):
            next(tokens)  # ;
            symbol_table.define(var_name, type, kind)
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
            for i in self.compile_class_var_dec(tokens, symbol_table, lvl + 1):
                yield i

        while tokens.peek() in [
            Keyword("constructor"),
            Keyword("function"),
            Keyword("method"),
        ]:
            sub_routine_insts = [
                *self.compile_subroutine_dec(tokens, symbol_table, lvl + 1)
            ]

            yield f"{self.sub_routine_kind} {self.class_name}.{self.sub_routine_name} {sum(symbol_table.var_count.values())}"

            for i in sub_routine_insts:
                yield i
            yield f"call {self.sub_routine_name} 1"

        next(tokens).to_xml(lvl + 1)  # }

    def parse(self, tokens, symbol_table):
        yield self.compile_class(tokens, symbol_table, lvl=1)
