from .jack_token import Keyword, Identifier, Symbol


class CompilationEngine:
    @staticmethod
    def compile_class_var_dec(tokens, output_file, lvl=0):
        print(next(tokens).to_xml(lvl + 1), file=output_file)  # 'static|field'
        CompilationEngine.compile_type(tokens, output_file, lvl + 1)  # type
        print(next(tokens).to_xml(lvl + 1), file=output_file)  # varName
        
        if tokens.peek() == Symbol(';'):
            print(next(tokens).to_xml(lvl + 1), file=output_file)
        elif tokens.peek() == Symbol(','):
            while tokens.peek() != Symbol(';'):
                print(next(tokens).to_xml(lvl + 1), file=output_file) # ,
                print(next(tokens).to_xml(lvl + 1), file=output_file) # varName
            print(next(tokens).to_xml(lvl + 1), file=output_file)
        else:
            raise ValueError(f"invalid token: {tokens.peek()}")


    @staticmethod
    def compile_type(tokens, output_file, lvl=0):
        token = next(tokens)
        print(token)
        print(token.to_xml(lvl + 1), file=output_file)

    @staticmethod
    def compile_parameter_list(tokens, output_file, lvl=0):
        CompilationEngine.compile_type(tokens, output_file, lvl + 1)
        print(next(tokens).to_xml(lvl + 1), file=output_file)
        while token := next(tokens):
            if token == Symbol(","):
                pass
            elif token == Symbol(";"):
                pass

    @staticmethod
    def compile_var_dec(tokens, output_file, lvl=0):
        print(next(tokens).to_xml(lvl=lvl + 1), file=output_file)  # 'var'
        CompilationEngine.compile_type(tokens, output_file, lvl + 1)  # type
        print(next(tokens).to_xml(lvl=lvl + 1), file=output_file)  # varName

        while token := next(tokens):
            if token == Symbol(","):
                print(tokens.to_xml(lvl + 1), file=output_file)  # ,
                print(next(tokens).to_xml(lvl + 1), file=output_file)  # varName
            elif token == Symbol(";"):
                print(token.to_xml(lvl + 1), file=output_file)  # ;
                break
            else:
                raise Exception(f"invalid token: {token}")

    @staticmethod
    def compile_statements(tokens, output_file, lvl=0):
        token = next(tokens)
        if token == Keyword("let"):
            print(token.to_xml(lvl + 1), file=output_file)  # let
            print(next(tokens).to_xml(lvl + 1), file=output_file)  # varName
            token2 = next(tokens)
            if token2 == Symbol("="):
                CompilationEngine.compile_expression(
                    token, output_file, lvl + 1
                )  # expression
                print(next(tokens).to_xml(lvl + 1), file=output_file)  # ";"
            elif token2 == Symbol("["):
                # how can I have the token stream to roll back one item?
                print(token2.to_xml(lvl + 1), file=output_file)
                CompilationEngine.compile_expression(
                    token, output_file, lvl + 1
                )  # expression
                print(next(tokens).to_xml(lvl + 1), file=output_file)  # "]"
            else:
                raise ValueError(f"{token2} invalid.")

    @staticmethod
    def compile_subroutine_body(tokens, output_file, lvl=0):
        print(next(tokens).to_xml(lvl + 1), file=output_file)
        CompilationEngine.compile_var_dec(tokens, output_file, lvl + 1)
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

        if (t := next(tokens)) == Symbol(")"):
            # t is right bracket
            print(t.to_xml(lvl + 1), file=output_file)
        else:
            # parameter list
            CompilationEngine.compile_subroutine_type(t, output_file, lvl + 1)  # type
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
        CompilationEngine.compile_subroutine_dec(tokens, output_file)
        right = next(tokens)
        print(right.to_xml(lvl + 1), file=output_file)

    @staticmethod
    def parse(tokens, output_file):
        CompilationEngine.compile_class(tokens, output_file)
