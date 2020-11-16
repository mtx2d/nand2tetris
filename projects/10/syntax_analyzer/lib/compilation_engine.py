import pdb
from .jack_token import Keyword, Identifier, Symbol, IntegerConstant, StringConstant


class CompilationEngine:
    @staticmethod
    def compile_class_var_dec(tokens, output_file, lvl=0):
        print(next(tokens).to_xml(lvl + 1), file=output_file)  # static|field
        CompilationEngine.compile_type(tokens, output_file, lvl + 1)  # type
        print(next(tokens).to_xml(lvl + 1), file=output_file)  # varName

        if tokens.peek() == Symbol(";"):
            print(next(tokens).to_xml(lvl + 1), file=output_file)
        elif tokens.peek() == Symbol(","):
            while tokens.peek() != Symbol(";"):
                print(next(tokens).to_xml(lvl + 1), file=output_file)  # ,
                print(next(tokens).to_xml(lvl + 1), file=output_file)  # varName
            print(next(tokens).to_xml(lvl + 1), file=output_file)
        elif tokens.peek() in [Keyword("static"), Keyword("field")]:
            CompilationEngine.compile_class_var_dec(tokens, output_file, lvl + 1)
        else:
            raise ValueError(f"invalid token: {tokens.peek()}")

    @staticmethod
    def compile_type(tokens, output_file, lvl=0):
        token = next(tokens)
        print(token.to_xml(lvl + 1), file=output_file)

    @staticmethod
    def compile_parameter_list(tokens, output_file, lvl=0):
        if tokens.peek() == ")":
            return
        CompilationEngine.compile_type(tokens, output_file, lvl + 1)
        print(next(tokens).to_xml(lvl + 1), file=output_file)
        while tokens.peek() == Symbol(","):
            CompilationEngine.compile_type(tokens, output_file, lvl + 1)
            print(next(tokens).to_xml(lvl + 1), file=output_file)

    @staticmethod
    def compile_var_dec(tokens, output_file, lvl=0):
        print(next(tokens).to_xml(lvl=lvl + 1), file=output_file)  # 'var'
        CompilationEngine.compile_type(tokens, output_file, lvl + 1)  # type
        print(next(tokens).to_xml(lvl=lvl + 1), file=output_file)  # varName

        if tokens.peek() == Symbol(";"):
            print(next(tokens).to_xml(lvl + 1), file=output_file)
        elif tokens.peek() == Symbol(","):
            while tokens.peek() != Symbol(";"):
                print(next(tokens).to_xml(lvl + 1), file=output_file)  # ,
                print(next(tokens).to_xml(lvl + 1), file=output_file)  # varName
            print(next(tokens).to_xml(lvl + 1), file=output_file)
        else:
            raise ValueError(f"invalid token: {tokens.peek()}")

    @staticmethod
    def compile_term(tokens, output_file, lvl=0):
        if isinstance(tokens.peek(), IntegerConstant):
            print(next(tokens).to_xml(lvl + 1), file=output_file)
        elif isinstance(tokens.peek(), StringConstant):
            print(next(tokens).to_xml(lvl + 1), file=output_file)
        elif isinstance(tokens.peek(), Keyword):
            print(next(tokens).to_xml(lvl + 1), file=output_file)
        elif isinstance(tokens.peek(), Identifier):
            if tokens[1] == Symbol("["):
                print(next(tokens).to_xml(lvl + 1), file=output_file)  # varName
                print(next(tokens).to_xml(lvl + 1), file=output_file)  # [
                CompilationEngine.compile_expression(tokens, output_file, lvl + 1)
                print(next(tokens).to_xml(lvl + 1), file=output_file)  # ]
            if tokens[1] == Symbol("("):
                # subRoutineCall
                CompilationEngine.compile_subroutine_call(tokens, output_file, lvl + 1)
        elif tokens.peek() == Symbol("("):
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # (
            CompilationEngine.compile_expression(tokens, output_file, lvl + 1)
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # )
        elif tokens.peek() in [Symbol("-"), Symbol("~")]:
            print(next(tokens).to_xml(lvl + 1), file=output_file)
            CompilationEngine.compile_term(tokens, output_file, lvl + 1)
        else:
            raise ValueError(f"invalid token {tokens.peek()}")

    @staticmethod
    def compile_expression(tokens, output_file, lvl=0):
        # caller handles the starting([) and enclosing(]) brackets.
        if tokens.peek() in [Symbol("="), Symbol(")"), Symbol("]"), Symbol(";")]:
            return
        CompilationEngine.compile_term(tokens, output_file, lvl + 1)
        while tokens.peek() in [
            Symbol(x) for x in ["+", "-", "*", "/", "&", "|", "<", ">", "="]
        ]:
            print(next(tokens).to_xml(lvl + 1), file=output_file)
            CompilationEngine.compile_term(tokens, output_file, lvl + 1)

    @staticmethod
    def compile_expression_list(tokens, output_file, lvl=0):
        CompilationEngine.compile_expression(tokens, output_file, lvl + 1)
        while tokens.peek() == Symbol(","):
            print(next(tokens).to_xml(lvl + 1), file=output_file)
            CompilationEngine.compile_expression(tokens, output_file, lvl + 1)

    @staticmethod
    def compile_subroutine_call(tokens, output_file, lvl=0):
        print(
            next(tokens).to_xml(lvl + 1), file=output_file
        )  # subroutine name | (className | varName)
        if tokens.peek() == Symbol("("):
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # (
            CompilationEngine.compile_expression_list(tokens, output_file)
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # )
        elif tokens.peek() == Symbol("."):
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # .
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # subroutineName
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # (
            CompilationEngine.compile_expression_list(tokens, output_file)
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # )
        else:
            raise ValueError(f"invalid token: {tokens.peek()}")

    @staticmethod
    def compile_statements(tokens, output_file, lvl=0):
        if tokens.peek() == Keyword("let"):
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # let
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # varName

            if tokens.peek() == Symbol("="):
                print(next(tokens).to_xml(lvl + 1), file=output_file)  # "="
                CompilationEngine.compile_expression(
                    tokens, output_file, lvl + 1
                )  # expression
                print(next(tokens).to_xml(lvl + 1), file=output_file)  # ";"
            elif tokens.peek() == Symbol("["):
                print(next(tokens).to_xml(lvl + 1), file=output_file)  # [
                CompilationEngine.compile_expression(
                    tokens, output_file, lvl + 1
                )  # expression
                print(next(tokens).to_xml(lvl + 1), file=output_file)  # "]"
            else:
                raise ValueError(f"{tokens.peek()} invalid.")
        elif tokens.peek() == Keyword("if"):
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # if
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # (
            CompilationEngine.compile_expression(tokens, output_file, lvl + 1)
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # )

            print(next(tokens).to_xml(lvl + 1), file=output_file)  # {
            CompilationEngine.compile_statements(tokens, output_file, lvl + 1)
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # }

            if tokens and tokens.peek() == Keyword("else"):
                print(next(tokens).to_xml(lvl + 1), file=output_file)  # {
                CompilationEngine.compile_statements(tokens, output_file, lvl + 1)
                print(next(tokens).to_xml(lvl + 1), file=output_file)  # }
        elif tokens.peek() == Keyword("while"):
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # while
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # (
            CompilationEngine.compile_expression(tokens, output_file, lvl + 1)
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # )

            print(next(tokens).to_xml(lvl + 1), file=output_file)  # {
            CompilationEngine.compile_statements(tokens, output_file, lvl + 1)
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # }
        elif tokens.peek() == Keyword("do"):
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # do
            CompilationEngine.compile_subroutine_call(tokens, output_file, lvl + 1)
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # ;
        elif tokens.peek() == Keyword("return"):
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # return
            if tokens.peek() != Symbol(";"):
                CompilationEngine.compile_expression(tokens, output_file, lvl + 1)
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # ;
        else:
            raise ValueError(f"invalid token: {tokens.peek()}")

    @staticmethod
    def compile_subroutine_body(tokens, output_file, lvl=0):
        pdb.set_trace()
        print(next(tokens).to_xml(lvl + 1), file=output_file)  # {
        while tokens.peek() == Keyword("var"):
            CompilationEngine.compile_var_dec(tokens, output_file, lvl + 1)
        while tokens.peek() in [
            Keyword("let"),
            Keyword("if"),
            Keyword("while"),
            Keyword("do"),
            Keyword("return"),
        ]:
            CompilationEngine.compile_statements(tokens, output_file, lvl + 1)
        print(next(tokens).to_xml(lvl + 1), file=output_file)

    @staticmethod
    def compile_subroutine_dec(tokens, output_file, lvl=0):
        subroutine_type = next(tokens)
        print(subroutine_type.to_xml(lvl + 1), file=output_file)
        CompilationEngine.compile_type(tokens, output_file)
        subroutine_name = next(tokens)
        print(subroutine_name.to_xml(lvl + 1), file=output_file)
        left_bracket = next(tokens)
        print(left_bracket.to_xml(lvl + 1), file=output_file)

        if tokens.peek() == Symbol(")"):
            # t is right bracket
            print(next(tokens).to_xml(lvl + 1), file=output_file)
        elif tokens.peek() in [Keyword("static"), Keyword("field")]:
            CompilationEngine.compile_subroutine_dec(tokens, output_file, lvl + 1)
        else:
            # parameter list
            CompilationEngine.compile_type(next(tokens), output_file, lvl + 1)  # type
            print(next(tokens).to_xml(lvl + 1))  # varNam, file=output_filee
            while t := next(tokens):
                if t == Symbol(","):
                    print(t.to_xml(lvl + 1), file=output_file)
                    print(next(tokens).to_xml(lvl + 1), file=output_file)
                elif t == Symbol(";"):
                    print(t.to_xml(lvl + 1), file=output_file)
                    break
                else:
                    raise ValueError(f"invalid token: {t}")
            print(t.to_xml(lvl + 1), file=output_file)
        CompilationEngine.compile_subroutine_body(tokens, output_file, lvl + 1)

    @staticmethod
    def compile_class(tokens, output_file, lvl=0):
        kls = next(tokens)
        print(kls.to_xml(lvl + 1), file=output_file)
        class_name = next(tokens)
        print(class_name.to_xml(lvl + 1), file=output_file)
        left = next(tokens)
        print(left.to_xml(lvl + 1), file=output_file)
        CompilationEngine.compile_class_var_dec(tokens, output_file)
        while tokens.peek() in [
            Keyword("constructor"),
            Keyword("function"),
            Keyword("method"),
        ]:
            CompilationEngine.compile_subroutine_dec(tokens, output_file)
        right = next(tokens)
        print(right.to_xml(lvl + 1), file=output_file)

    @staticmethod
    def parse(tokens, output_file):
        print("<tokens>", file=output_file)
        CompilationEngine.compile_class(tokens, output_file, lvl=1)
        print("</tokens>", file=output_file)
