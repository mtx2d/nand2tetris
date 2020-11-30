import pdb
from .jack_token import Keyword, Identifier, Symbol, IntegerConstant, StringConstant


class CompilationEngine:
    TAB_SIZE = 2

    @staticmethod
    def compile_var_dec(tokens, symbol_table, lvl=0):
        yield f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}<varDec>"

        yield next(tokens).to_xml(lvl=lvl + 2)  # 'var'
        for i in CompilationEngine.compile_type(tokens, symbol_table, lvl + 2):  # type
            yield i
        yield next(tokens).to_xml(lvl=lvl + 2)  # varName

        if tokens.peek() == Symbol(";"):
            yield next(tokens).to_xml(lvl + 2)
        elif tokens.peek() == Symbol(","):
            while tokens.peek() != Symbol(";"):
                yield next(tokens).to_xml(lvl + 2)  # ,
                yield next(tokens).to_xml(lvl + 2)  # varName
            yield next(tokens).to_xml(lvl + 2)
        else:
            raise ValueError(f"invalid token: {tokens.peek()}")
        yield f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}</varDec>"

    @staticmethod
    def compile_term(tokens, symbol_table, lvl=0):
        yield f"{' ' * CompilationEngine.TAB_SIZE * lvl}<term>"
        if isinstance(tokens.peek(), IntegerConstant):
            yield next(tokens).to_xml(lvl + 1)
        elif isinstance(tokens.peek(), StringConstant):
            yield next(tokens).to_xml(lvl + 1)
        elif isinstance(tokens.peek(), Keyword):
            # how to handle keyword constant?
            yield next(tokens).to_xml(lvl + 1)
        elif isinstance(tokens.peek(), Identifier):
            if tokens[1] == Symbol("["):
                yield next(tokens).to_xml(lvl + 1)  # varName
                yield next(tokens).to_xml(lvl + 1)  # [
                for i in CompilationEngine.compile_expression(
                    tokens, symbol_table, lvl + 1
                ):
                    yield i
                yield next(tokens).to_xml(lvl + 1)  # ]
            elif tokens[1] in [Symbol("("), Symbol(".")]:
                # subRoutineCall
                for i in CompilationEngine.compile_subroutine_call(
                    tokens, symbol_table, lvl + 1
                ):
                    yield i
            else:
                yield next(tokens).to_xml(lvl + 1)  # varName
        elif tokens.peek() == Symbol("("):
            yield next(tokens).to_xml(lvl + 1)  # (
            for i in CompilationEngine.compile_expression(
                tokens, symbol_table, lvl + 1
            ):
                yield i
            yield next(tokens).to_xml(lvl + 1)  # )
        elif tokens.peek() in [Symbol("-"), Symbol("~")]:
            yield next(tokens).to_xml(lvl + 1)
            yield CompilationEngine.compile_term(tokens, symbol_table, lvl + 1)
        else:
            raise ValueError(f"invalid token {tokens.peek()}")
        yield f"{' ' * CompilationEngine.TAB_SIZE * lvl}</term>"

    @staticmethod
    def compile_expression(tokens, symbol_table, lvl=0) -> str:
        if tokens.peek() in [
            Symbol("="),
            Symbol(")"),
            Symbol("]"),
            Symbol(";"),
            Symbol("}"),
        ]:
            yield
        yield f"{' ' * CompilationEngine.TAB_SIZE * lvl}<expression>"

        # caller handles the starting([) and enclosing(]) brackets.
        for i in CompilationEngine.compile_term(tokens, symbol_table, lvl + 1):
            yield i
        while tokens.peek() in [
            Symbol(x) for x in ["+", "-", "*", "/", "&", "|", "<", ">", "="]
        ]:
            yield next(tokens).to_xml(lvl + 1)
            for i in CompilationEngine.compile_term(tokens, symbol_table, lvl + 1):
                yield i
        yield f"{' ' * CompilationEngine.TAB_SIZE * lvl}</expression>"

    @staticmethod
    def compile_expression_list(tokens, symbol_table, lvl=0):
        yield f"{' ' * CompilationEngine.TAB_SIZE * lvl}<expressionList>"

        for i in CompilationEngine.compile_expression(tokens, symbol_table, lvl + 1):
            yield i
        while tokens.peek() == Symbol(","):
            yield next(tokens).to_xml(lvl + 1)  # ,
            for i in CompilationEngine.compile_expression(
                tokens, symbol_table, lvl + 1
            ):
                yield i
        yield f"{' ' * CompilationEngine.TAB_SIZE * lvl}</expressionList>"

    @staticmethod
    def compile_subroutine_call(tokens, symbol_table, lvl=0):
        yield next(tokens).to_xml(lvl + 1)  # subroutine name | (className | varName)
        if tokens.peek() == Symbol("("):
            yield next(tokens).to_xml(lvl + 1)  # (
            for i in CompilationEngine.compile_expression_list(
                tokens, symbol_table, lvl + 1
            ):
                yield i
            yield next(tokens).to_xml(lvl + 1)  # )
        elif tokens.peek() == Symbol("."):
            yield next(tokens).to_xml(lvl + 1)  # .
            yield next(tokens).to_xml(lvl + 1)  # subroutineName
            yield next(tokens).to_xml(lvl + 1)  # (
            for i in CompilationEngine.compile_expression_list(
                tokens, symbol_table, lvl + 1
            ):
                yield i
            yield next(tokens).to_xml(lvl + 1)  # )
        else:
            raise ValueError(f"invalid token: {tokens.peek()}")

    @staticmethod
    def compile_statements(tokens, symbol_table, lvl=0) -> str:
        if tokens.peek() == Symbol("}"):
            yield
        yield f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}<statements>"

        while tokens and tokens.peek() in [
            Keyword("let"),
            Keyword("do"),
            Keyword("if"),
            Keyword("while"),
            Keyword("return"),
        ]:
            for i in CompilationEngine.compile_statement(tokens, symbol_table, lvl + 1):
                yield i
            yield f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}</statements>"

    @staticmethod
    def compile_statement(tokens, symbol_table, lvl=0) -> str:
        if tokens.peek() == Keyword("let"):
            yield f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}<letStatement>"

            yield next(tokens).to_xml(lvl + 2)  # let
            yield next(tokens).to_xml(lvl + 2)  # varName

            if tokens.peek() == Symbol("="):
                yield next(tokens).to_xml(lvl + 2)  # "="
                for i in CompilationEngine.compile_expression(
                    tokens, symbol_table, lvl + 2
                ):  # expression
                    yield i
                yield next(tokens).to_xml(lvl + 2)  # ";"
            elif tokens.peek() == Symbol("["):
                yield next(tokens).to_xml(lvl + 2)  # [
                for i in CompilationEngine.compile_expression(
                    tokens, symbol_table, lvl + 2
                ):  # expression
                    yield i
                yield next(tokens).to_xml(lvl + 2)  # "]"
                yield next(tokens).to_xml(lvl + 2)  # =
                for i in CompilationEngine.compile_expression(
                    tokens, symbol_table, lvl + 2
                ):
                    yield i
                yield next(tokens).to_xml(lvl + 2)  # ;
            else:
                raise ValueError(f"{tokens.peek()} invalid.")

            yield f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}</letStatement>"

        elif tokens.peek() == Keyword("if"):
            yield f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}<ifStatement>"

            yield next(tokens).to_xml(lvl + 2)  # if
            yield next(tokens).to_xml(lvl + 2)  # (
            for i in CompilationEngine.compile_expression(
                tokens, symbol_table, lvl + 2
            ):
                yield i
            yield next(tokens).to_xml(lvl + 2)  # )

            yield next(tokens).to_xml(lvl + 2)  # {
            for i in CompilationEngine.compile_statements(
                tokens, symbol_table, lvl + 2
            ):
                yield i
            yield next(tokens).to_xml(lvl + 2)  # }

            if tokens and tokens.peek() == Keyword("else"):
                yield next(tokens).to_xml(lvl + 2)  # else
                yield next(tokens).to_xml(lvl + 2)  # {
                for i in CompilationEngine.compile_statements(
                    tokens, symbol_table, lvl + 2
                ):
                    yield i
                yield next(tokens).to_xml(lvl + 2)  # }
            yield f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}</ifStatement>"
        elif tokens.peek() == Keyword("while"):
            yield f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}<whileStatement>"

            yield next(tokens).to_xml(lvl + 2)  # while
            yield next(tokens).to_xml(lvl + 2)  # (
            yield CompilationEngine.compile_expression(tokens, symbol_table, lvl + 2)
            yield next(tokens).to_xml(lvl + 2)  # )

            yield next(tokens).to_xml(lvl + 2)  # {
            yield CompilationEngine.compile_statements(tokens, symbol_table, lvl + 2)
            yield next(tokens).to_xml(lvl + 2)  # }
            yield f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}</whileStatement>"

        elif tokens.peek() == Keyword("do"):
            yield f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}<doStatement>"

            yield next(tokens).to_xml(lvl + 2)  # do
            for i in CompilationEngine.compile_subroutine_call(
                tokens, symbol_table, lvl + 2
            ):
                yield i
            yield next(tokens).to_xml(lvl + 2)  # ;
            yield f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}</doStatement>"
        elif tokens.peek() == Keyword("return"):
            yield f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}<returnStatement>"
            yield next(tokens).to_xml(lvl + 1)  # return
            if tokens.peek() != Symbol(";"):
                for i in CompilationEngine.compile_expression(
                    tokens, symbol_table, lvl + 2
                ):
                    yield i
            yield next(tokens).to_xml(lvl + 2)  # ;
            yield f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}</returnStatement>"

        else:
            raise ValueError(f"invalid token: {tokens.peek()}")

    @staticmethod
    def compile_subroutine_body(tokens, symbol_table, lvl=0):
        yield f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}<subroutineBody>"

        yield next(tokens).to_xml(lvl + 2)  # {
        while tokens.peek() == Keyword("var"):
            for i in CompilationEngine.compile_var_dec(tokens, symbol_table, lvl + 2):
                yield i
        while tokens.peek() in [
            Keyword("let"),
            Keyword("if"),
            Keyword("while"),
            Keyword("do"),
            Keyword("return"),
        ]:
            for i in CompilationEngine.compile_statements(
                tokens, symbol_table, lvl + 2
            ):
                yield i
        yield next(tokens).to_xml(lvl + 2)
        yield f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}</subroutineBody>"

    @staticmethod
    def compile_type(tokens, symbol_table, lvl=0):
        yield next(tokens).to_xml(lvl + 1)

    @staticmethod
    def compile_parameter_list(tokens, symbol_table, lvl=0):
        yield f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}<parameterList>"
        if tokens.peek() == Symbol(")"):
            yield f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}</parameterList>"
            return

        for i in CompilationEngine.compile_type(tokens, symbol_table, lvl + 2):
            yield i
        yield next(tokens).to_xml(lvl + 2)
        while tokens.peek() == Symbol(","):
            yield next(tokens).to_xml(lvl + 2)  # ,
            for i in CompilationEngine.compile_type(
                tokens, symbol_table, lvl + 2
            ):  # type
                yield i
            yield next(tokens).to_xml(lvl + 2)  # varName
        yield f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}</parameterList>"

    @staticmethod
    def compile_subroutine_dec(tokens, symbol_table, lvl=0):
        yield f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}<subroutineDec>"

        yield next(tokens).to_xml(lvl + 2)  # (constructor | function | method)
        for i in CompilationEngine.compile_type(tokens, symbol_table):  # type
            yield i
        yield next(tokens).to_xml(lvl + 2)  # subroutine_name
        yield next(tokens).to_xml(lvl + 2)  # (
        for i in CompilationEngine.compile_parameter_list(
            tokens, symbol_table, lvl + 2
        ):
            yield i
        yield next(tokens).to_xml(lvl + 2)  # )
        for i in CompilationEngine.compile_subroutine_body(
            tokens, symbol_table, lvl + 2
        ):
            yield i

        yield f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}</subroutineDec>"

    @staticmethod
    def compile_class_var_dec(tokens, symbol_table, lvl=0):
        yield f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}<classVarDec>"
        yield next(tokens).to_xml(lvl + 2)  # static|field
        for i in CompilationEngine.compile_type(tokens, symbol_table, lvl + 2):  # type
            yield i
        yield next(tokens).to_xml(lvl + 2)  # varName

        if tokens.peek() == Symbol(";"):
            yield next(tokens).to_xml(lvl + 2)
        elif tokens.peek() == Symbol(","):
            while tokens.peek() != Symbol(";"):
                yield next(tokens).to_xml(lvl + 2)  # ,
                yield next(tokens).to_xml(lvl + 2)  # varName
            yield next(tokens).to_xml(lvl + 2)
        else:
            raise ValueError(f"invalid token: {tokens.peek()}")
        yield f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}</classVarDec>"

    @staticmethod
    def compile_class(tokens, symbol_table, lvl=0):
        yield f"{' ' * CompilationEngine.TAB_SIZE * lvl}<class>"
        yield next(tokens).to_xml(lvl + 1)  # class
        yield next(tokens).to_xml(lvl + 1)  # className
        yield next(tokens).to_xml(lvl + 1)  # (
        while tokens.peek() in [Keyword("static"), Keyword("field")]:
            for i in CompilationEngine.compile_class_var_dec(
                tokens, symbol_table, lvl + 1
            ):
                yield i

        while tokens.peek() in [
            Keyword("constructor"),
            Keyword("function"),
            Keyword("method"),
        ]:
            for i in CompilationEngine.compile_subroutine_dec(
                tokens, symbol_table, lvl  # TODO fix this indentation bug
            ):
                yield i

        yield next(tokens).to_xml(lvl + 1)  # )
        yield f"{' ' * CompilationEngine.TAB_SIZE * lvl}</class>"

    @staticmethod
    def parse(tokens, symbol_table):
        yield CompilationEngine.compile_class(tokens, symbol_table, lvl=1)
