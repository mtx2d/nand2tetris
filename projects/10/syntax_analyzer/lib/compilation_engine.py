from jack_token import Keyword, Identifier, Symbol


class CompilationEngine:
    @staticmethod
    def compile_class_var_dec(tokens, output_file, lvl=0):
        output_file.write(next(tokens).to_xml(lvl=lvl + 1))  # 'static|field'
        CompilationEngine.compile_type(tokens, output_file, lvl + 1)  # type
        output_file.write(next(tokens).to_xml(lvl=lvl + 1))  # varName

        while token := next(tokens):
            if token == Symbol(","):
                output_file.write(tokens.to_xml(lvl + 1))  # ,
                output_file.write(next(tokens).to_xml(lvl + 1))  # varName
            elif token == Symbol(";"):
                output_file.write(token.to_xml(lvl + 1))  # ;
                break
            else:
                raise Exception(f"invalid token: {token}")

    @staticmethod
    def compile_type(tokens, output_file, lvl=0):
        token = next(tokens)
        print(token)
        output_file.write(token.to_xml(lvl + 1))

    @staticmethod
    def compile_parameter_list(tokens, output_file, lvl=0):
        CompilationEngine.compile_type(tokens, output_file, lvl + 1)
        output_file.write(next(tokens).to_xml(lvl + 1))
        while token := next(tokens):
            if token == Symbol(","):
                pass
            elif token == Symbol(";"):
                pass

    @staticmethod
    def compile_var_dec(tokens, output_file, lvl=0):
        output_file.write(next(tokens).to_xml(lvl=lvl + 1))  # 'var'
        CompilationEngine.compile_type(tokens, output_file, lvl + 1)  # type
        output_file.write(next(tokens).to_xml(lvl=lvl + 1))  # varName

        while token := next(tokens):
            if token == Symbol(","):
                output_file.write(tokens.to_xml(lvl + 1))  # ,
                output_file.write(next(tokens).to_xml(lvl + 1))  # varName
            elif token == Symbol(";"):
                output_file.write(token.to_xml(lvl + 1))  # ;
                break
            else:
                raise Exception(f"invalid token: {token}")

    @staticmethod
    def compile_statements(tokens, output_file, lvl=0):
        pass

    @staticmethod
    def compile_subroutine_body(tokens, output_file, lvl=0):
        output_file.write(next(tokens).to_xml(lvl + 1))
        CompilationEngine.compile_var_dec(tokens, output_file, lvl + 1)
        CompilationEngine.compile_statements(tokens, output_file, lvl + 1)
        output_file.write(next(tokens).to_xml(lvl + 1))

    @staticmethod
    def compile_subroutine_dec(tokens, output_file, lvl=0):
        subroutine_type = next(tokens)
        output_file.write(subroutine_type.to_xml(lvl + 1))
        CompilationEngine.compile_type(tokens, output_file)
        subroutine_name = next(tokens)
        output_file.write(subroutine_name.to_xml(lvl + 1))
        left_bracket = next(tokens)
        output_file.write(left_bracket.to_xml(lvl + 1))

        if (t := next(tokens)) == Symbol(")"):
            # t is right bracket 
            output_file.write(t.to_xml(lvl + 1))
        else:
            # parameter list
            CompilationEngine.compile_subroutine_type(t, output_file, lvl + 1)  # type
            output_file.write(next(tokens).to_xml(lvl + 1)) # varName
            while t := next(tokens):
                if t == Symbol(","):
                    output_file.write(t.to_xml(lvl + 1))
                    output_file.write(next(tokens).to_xml(lvl + 1))
                elif t == Symbol(";"):
                    output_file.write(t.to_xml(lvl + 1))
                    break
                else:
                    raise ValueError(f"invalid token: {t}")
            output_file.write(t.to_xml(lvl + 1))
        CompilationEngine.compile_subroutine_body(tokens, output_file, lvl + 1)

    @staticmethod
    def compile_class(tokens, output_file, lvl=0):
        kls = next(tokens)
        output_file.write(kls.to_xml(lvl + 1))
        class_name = next(tokens)
        output_file.write(class_name.to_xml(lvl + 1))
        left = next(tokens)
        output_file.write(left.to_xml(lvl + 1))
        CompilationEngine.compile_class_var_dec(tokens, output_file)
        CompilationEngine.compile_subroutine_dec(tokens, output_file)
        right = next(tokens)
        output_file.write(right.to_xml(lvl + 1))

    @staticmethod
    def parse(tokens, output_file):
        CompilationEngine.compile_class(tokens, output_file)
