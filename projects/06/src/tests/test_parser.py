import unittest
from lib.parser import Parser
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = Parser(os.path.join(THIS_DIR, "./test_parser_file.asm"))

    def test_get_instruction(self):
        insts = [inst for inst in self.parser.get_instruction()]

        expected_insts = [
            *zip(
                range(1, 8),
                ["@R0", "D=M", "@R1", "D=D-M", "@OUTPUT_FIRST", "D;JGT", "@R1", "D=M"],
            )
        ]
        self.assertEqual(insts, expected_insts)

    def test_strip_comments(self):
        line_with_comments = "D=D-M            // D = first number - second number"
        line = self.parser.strip_comments(line_with_comments)
        expected_line = "D=D-M"
        self.assertEqual(line, expected_line)
