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
    def compile_parameter_list(tokens, output_file, lvl = 0):
       CompilationEngine.compile_type(tokens, output_file, lvl + 1) 
       CompilationEngine.compile_var_name(tokens, output_file, lvl + 1)

    @staticmethod
    def compile_subroutine_body(tokens, output_file, lvl = 0):
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
        CompilationEngine.compile_parameter_list(tokens, output_file, lvl+ 1)
        right_bracket = next(tokens)
        output_file.write(right_bracket.to_xml(lvl + 1))
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
