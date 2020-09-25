from parser import Parser


class Translator:
    def __init__(self, input_file: str):
        self.parser = Parser(input_file)

    def translate(self):
        for line in parser.parse():
            pass
