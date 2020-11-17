import pdb
from .jack_token import Keyword, Identifier, Symbol, IntegerConstant, StringConstant


class CompilationEngine:
    TAB_SIZE = 2

    @staticmethod
    def compile_class_var_dec(tokens, output_file, lvl=0):

        print(
            f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}<classVarDec>",
            file=output_file,
        )
        print(next(tokens).to_xml(lvl + 2), file=output_file)  # static|field
        CompilationEngine.compile_type(tokens, output_file, lvl + 2)  # type
        print(next(tokens).to_xml(lvl + 2), file=output_file)  # varName

        if tokens.peek() == Symbol(";"):
            print(next(tokens).to_xml(lvl + 2), file=output_file)
        elif tokens.peek() == Symbol(","):
            while tokens.peek() != Symbol(";"):
                print(next(tokens).to_xml(lvl + 2), file=output_file)  # ,
                print(next(tokens).to_xml(lvl + 2), file=output_file)  # varName
            print(next(tokens).to_xml(lvl + 2), file=output_file)
        elif tokens.peek() in [Keyword("static"), Keyword("field")]:
            CompilationEngine.compile_class_var_dec(tokens, output_file, lvl + 2)
        else:
            raise ValueError(f"invalid token: {tokens.peek()}")
        print(
            f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}</classVarDec>",
            file=output_file,
        )

    @staticmethod
    def compile_var_dec(tokens, output_file, lvl=0):
        print(
            f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}<varDec>",
            file=output_file,
        )

        print(next(tokens).to_xml(lvl=lvl + 2), file=output_file)  # 'var'
        CompilationEngine.compile_type(tokens, output_file, lvl + 2)  # type
        print(next(tokens).to_xml(lvl=lvl + 2), file=output_file)  # varName

        if tokens.peek() == Symbol(";"):
            print(next(tokens).to_xml(lvl + 2), file=output_file)
        elif tokens.peek() == Symbol(","):
            while tokens.peek() != Symbol(";"):
                print(next(tokens).to_xml(lvl + 2), file=output_file)  # ,
                print(next(tokens).to_xml(lvl + 2), file=output_file)  # varName
            print(next(tokens).to_xml(lvl + 2), file=output_file)
        else:
            raise ValueError(f"invalid token: {tokens.peek()}")
        print(
            f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}</varDec>",
            file=output_file,
        )

    @staticmethod
    def compile_term(tokens, output_file, lvl=0):
        print(
            f"{' ' * CompilationEngine.TAB_SIZE * lvl}<term>",
            file=output_file,
        )
        if isinstance(tokens.peek(), IntegerConstant):
            print(next(tokens).to_xml(lvl + 1), file=output_file)
        elif isinstance(tokens.peek(), StringConstant):
            print(next(tokens).to_xml(lvl + 1), file=output_file)
        elif isinstance(tokens.peek(), Keyword):
            # how to handle keyword constant?
            print(next(tokens).to_xml(lvl + 1), file=output_file)
        elif isinstance(tokens.peek(), Identifier):
            if tokens[1] == Symbol("["):
                print(next(tokens).to_xml(lvl + 1), file=output_file)  # varName
                print(next(tokens).to_xml(lvl + 1), file=output_file)  # [
                CompilationEngine.compile_expression(tokens, output_file, lvl + 1)
                print(next(tokens).to_xml(lvl + 1), file=output_file)  # ]
            elif tokens[1] in [Symbol("("), Symbol(".")]:
                # subRoutineCall
                CompilationEngine.compile_subroutine_call(tokens, output_file, lvl + 1)
            else:
                print(next(tokens).to_xml(lvl + 1), file=output_file)  # varName
        elif tokens.peek() == Symbol("("):
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # (
            CompilationEngine.compile_expression(tokens, output_file, lvl + 1)
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # )
        elif tokens.peek() in [Symbol("-"), Symbol("~")]:
            print(next(tokens).to_xml(lvl + 1), file=output_file)
            CompilationEngine.compile_term(tokens, output_file, lvl + 1)
        else:
            raise ValueError(f"invalid token {tokens.peek()}")
        print(
            f"{' ' * CompilationEngine.TAB_SIZE * lvl}</term>",
            file=output_file,
        )

    @staticmethod
    def compile_expression(tokens, output_file, lvl=0):
        if tokens.peek() in [
            Symbol("="),
            Symbol(")"),
            Symbol("]"),
            Symbol(";"),
            Symbol("}"),
        ]:
            return
        print(
            f"{' ' * CompilationEngine.TAB_SIZE * lvl}<expression>",
            file=output_file,
        )
        # caller handles the starting([) and enclosing(]) brackets.
        CompilationEngine.compile_term(tokens, output_file, lvl + 1)
        while tokens.peek() in [
            Symbol(x) for x in ["+", "-", "*", "/", "&", "|", "<", ">", "="]
        ]:
            print(next(tokens).to_xml(lvl + 1), file=output_file)
            CompilationEngine.compile_term(tokens, output_file, lvl + 1)
        print(
            f"{' ' * CompilationEngine.TAB_SIZE * lvl}</expression>",
            file=output_file,
        )

    @staticmethod
    def compile_expression_list(tokens, output_file, lvl=0):
        print(
            f"{' ' * CompilationEngine.TAB_SIZE * lvl}<expression_list>",
            file=output_file,
        )
        CompilationEngine.compile_expression(tokens, output_file, lvl + 1)
        while tokens.peek() == Symbol(","):
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # ,
            CompilationEngine.compile_expression(tokens, output_file, lvl + 1)
        print(
            f"{' ' * CompilationEngine.TAB_SIZE * lvl}</expression_list>",
            file=output_file,
        )

    @staticmethod
    def compile_subroutine_call(tokens, output_file, lvl=0):
        print(
            next(tokens).to_xml(lvl + 1), file=output_file
        )  # subroutine name | (className | varName)
        if tokens.peek() == Symbol("("):
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # (
            CompilationEngine.compile_expression_list(tokens, output_file, lvl + 1)
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # )
        elif tokens.peek() == Symbol("."):
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # .
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # subroutineName
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # (
            CompilationEngine.compile_expression_list(tokens, output_file, lvl + 1)
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # )
        else:
            raise ValueError(f"invalid token: {tokens.peek()}")

    @staticmethod
    def compile_statements(tokens, output_file, lvl=0):
        if tokens.peek() == Symbol("}"):
            return
        print(
            f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}<statements>",
            file=output_file,
        )
        while tokens and tokens.peek() in [
            Keyword("let"),
            Keyword("do"),
            Keyword("if"),
            Keyword("while"),
            Keyword("return"),
        ]:
            CompilationEngine.compile_statement(tokens, output_file, lvl + 1)
        print(
            f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}</statements>",
            file=output_file,
        )

    @staticmethod
    def compile_statement(tokens, output_file, lvl=0):
        if tokens.peek() == Keyword("let"):
            print(
                f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}<letStatement>",
                file=output_file,
            )
            print(next(tokens).to_xml(lvl + 2), file=output_file)  # let
            print(next(tokens).to_xml(lvl + 2), file=output_file)  # varName

            if tokens.peek() == Symbol("="):
                print(next(tokens).to_xml(lvl + 2), file=output_file)  # "="
                CompilationEngine.compile_expression(
                    tokens, output_file, lvl + 2
                )  # expression
                print(next(tokens).to_xml(lvl + 2), file=output_file)  # ";"
            elif tokens.peek() == Symbol("["):
                print(next(tokens).to_xml(lvl + 2), file=output_file)  # [
                CompilationEngine.compile_expression(
                    tokens, output_file, lvl + 2
                )  # expression
                print(next(tokens).to_xml(lvl + 2), file=output_file)  # "]"
                print(next(tokens).to_xml(lvl + 2), file=output_file)  # =
                CompilationEngine.compile_expression(tokens, output_file, lvl + 2)
                print(next(tokens).to_xml(lvl + 2), file=output_file)  # ;
            else:
                raise ValueError(f"{tokens.peek()} invalid.")

            print(
                f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}</letStatement>",
                file=output_file,
            )

        elif tokens.peek() == Keyword("if"):
            print(
                f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}<ifStatement>",
                file=output_file,
            )
            print(next(tokens).to_xml(lvl + 2), file=output_file)  # if
            print(next(tokens).to_xml(lvl + 2), file=output_file)  # (
            CompilationEngine.compile_expression(tokens, output_file, lvl + 2)
            print(next(tokens).to_xml(lvl + 2), file=output_file)  # )

            print(next(tokens).to_xml(lvl + 2), file=output_file)  # {
            CompilationEngine.compile_statements(tokens, output_file, lvl + 2)
            print(next(tokens).to_xml(lvl + 2), file=output_file)  # }

            if tokens and tokens.peek() == Keyword("else"):
                print(next(tokens).to_xml(lvl + 2), file=output_file)  # else
                print(next(tokens).to_xml(lvl + 2), file=output_file)  # {
                CompilationEngine.compile_statements(tokens, output_file, lvl + 2)
                print(next(tokens).to_xml(lvl + 2), file=output_file)  # }
            print(
                f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}</ifStatement>",
                file=output_file,
            )
        elif tokens.peek() == Keyword("while"):
            print(
                f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}<whileStatement>",
                file=output_file,
            )
            print(next(tokens).to_xml(lvl + 2), file=output_file)  # while
            print(next(tokens).to_xml(lvl + 2), file=output_file)  # (
            CompilationEngine.compile_expression(tokens, output_file, lvl + 2)
            print(next(tokens).to_xml(lvl + 2), file=output_file)  # )

            print(next(tokens).to_xml(lvl + 2), file=output_file)  # {
            CompilationEngine.compile_statements(tokens, output_file, lvl + 2)
            print(next(tokens).to_xml(lvl + 2), file=output_file)  # }
            print(
                f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}</whileStatement>",
                file=output_file,
            )
        elif tokens.peek() == Keyword("do"):
            print(
                f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}<doStatement>",
                file=output_file,
            )
            print(next(tokens).to_xml(lvl + 2), file=output_file)  # do
            CompilationEngine.compile_subroutine_call(tokens, output_file, lvl + 2)
            print(next(tokens).to_xml(lvl + 2), file=output_file)  # ;
            print(
                f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}</doStatement>",
                file=output_file,
            )
        elif tokens.peek() == Keyword("return"):
            print(
                f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}<returnStatement>",
                file=output_file,
            )
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # return
            if tokens.peek() != Symbol(";"):
                CompilationEngine.compile_expression(tokens, output_file, lvl + 2)
            print(next(tokens).to_xml(lvl + 2), file=output_file)  # ;
            print(
                f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}</returnStatement>",
                file=output_file,
            )
        else:
            raise ValueError(f"invalid token: {tokens.peek()}")

    @staticmethod
    def compile_subroutine_body(tokens, output_file, lvl=0):
        print(
            f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}<subroutineBody>",
            file=output_file,
        )
        print(next(tokens).to_xml(lvl + 2), file=output_file)  # {
        while tokens.peek() == Keyword("var"):
            CompilationEngine.compile_var_dec(tokens, output_file, lvl + 2)
        while tokens.peek() in [
            Keyword("let"),
            Keyword("if"),
            Keyword("while"),
            Keyword("do"),
            Keyword("return"),
        ]:
            CompilationEngine.compile_statements(tokens, output_file, lvl + 2)
        print(next(tokens).to_xml(lvl + 2), file=output_file)
        print(
            f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}</subroutineBody>",
            file=output_file,
        )

    @staticmethod
    def compile_type(tokens, output_file, lvl=0):
        token = next(tokens)
        print(token.to_xml(lvl + 1), file=output_file)

    @staticmethod
    def compile_parameter_list(tokens, output_file, lvl=0):
        print(
            f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}<parameterList>",
            file=output_file,
        )
        CompilationEngine.compile_type(tokens, output_file, lvl + 2)
        print(next(tokens).to_xml(lvl + 2), file=output_file)
        while tokens.peek() == Symbol(","):
            CompilationEngine.compile_type(tokens, output_file, lvl + 2)
            print(next(tokens).to_xml(lvl + 2), file=output_file)
        print(
            f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}</parameterList>",
            file=output_file,
        )

    @staticmethod
    def compile_subroutine_dec(tokens, output_file, lvl=0):
        print(
            f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}<subroutineDec>",
            file=output_file,
        )

        print(
            next(tokens).to_xml(lvl + 2), file=output_file
        )  # (constructor | function | method)
        CompilationEngine.compile_type(tokens, output_file)  # type
        print(next(tokens).to_xml(lvl + 2), file=output_file)  # subroutine_name
        print(next(tokens).to_xml(lvl + 2), file=output_file)  # (
        CompilationEngine.compile_parameter_list(tokens, output_file, lvl + 2)
        print(next(tokens).to_xml(lvl + 2), file=output_file)  # )
        CompilationEngine.compile_subroutine_body(tokens, output_file, lvl + 2)

        print(
            f"{' ' * CompilationEngine.TAB_SIZE * (lvl + 1)}</subroutineDec>",
            file=output_file,
        )

    @staticmethod
    def compile_class(tokens, output_file, lvl=0):
        print(f"{' ' * CompilationEngine.TAB_SIZE * lvl}<class>", file=output_file)
        print(next(tokens).to_xml(lvl + 1), file=output_file)  # class
        print(next(tokens).to_xml(lvl + 1), file=output_file)  # className
        print(next(tokens).to_xml(lvl + 1), file=output_file)  # (
        CompilationEngine.compile_class_var_dec(tokens, output_file)
        while tokens.peek() in [
            Keyword("constructor"),
            Keyword("function"),
            Keyword("method"),
        ]:
            CompilationEngine.compile_subroutine_dec(tokens, output_file)
        print(next(tokens).to_xml(lvl + 1), file=output_file)  # )
        print(f"{' ' * CompilationEngine.TAB_SIZE * lvl}</class>", file=output_file)

    @staticmethod
    def parse(tokens, output_file):
        # print("<tokens>", file=output_file)
        CompilationEngine.compile_class(tokens, output_file, lvl=1)
        # print("</tokens>", file=output_file)
