from jack_token import Keyword, Identifier


class CompilationEngine:
    @staticmethod
    def compile_class_var_dec(tokens, output_file):
        pass

    @staticmethod
    def compile_type(tokens, output_file):
        token = next(tokens)
        print(token)
        if isinstance(token, Keyword):
            output_file.write(f"<keyword> {token.val} </keyword>\n")
        elif isinstance(token, Identifier):
            output_file.write(f"<identifier> {token.val} </identifier>\n")
        else:
            raise TypeError(f"{token} should be either a Keyword or an Identifier.")

    @staticmethod
    def compile_parameter_list(tokens, output_file):
        pass

    @staticmethod
    def compile_subroutine_body(tokens, output_file):
        pass

    @staticmethod
    def compile_subroutine_dec(tokens, output_file):
        subroutine_type = next(tokens)
        return_type = CompilationEngine.compile_type(tokens, output_file)
        subroutine_name = next(tokens)
        left_bracket = next(tokens)
        parameter_list = CompilationEngine.compile_parameter_list(tokens, output_file)
        right_bracket = next(tokens)
        subroutine_body = CompilationEngine.compile_subroutine_body(tokens, output_file)

    @staticmethod
    def compile_class(tokens, output_file, lvl=0):
        kls = next(tokens)
        print(kls.to_xml(lvl + 1), file=output_file)
        class_name = next(tokens)
        print(class_name.to_xml(lvl + 1), file=output_file)
        left = next(tokens)
        CompilationEngine.compile_class_var_dec(tokens, output_file)
        CompilationEngine.compile_subroutine_dec(tokens, output_file)
        right = next(tokens)

    @staticmethod
    def parse(tokens, output_file):
        CompilationEngine.compile_class(tokens, output_file)
