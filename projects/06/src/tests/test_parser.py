import unittest
from lib.parser import Parser
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = Parser(os.path.join(THIS_DIR, "./test_parser_file.asm"))

    def test_strip_comments(self):
        lines = [
            self.parser.strip_comments(
                "D=D-M            // D = first number - second number"
            ),
            self.parser.strip_comments("D=M              // D = first number"),
            self.parser.strip_comments(
                "D;JGT              // if D>0 (first is greater) goto output_first"
            ),
        ]
        expected_lines = ["D=D-M", "D=M", "D;JGT"]

        for pair in zip(lines, expected_lines):
            self.assertEqual(pair[0], pair[1])

    def test_get_instruction(self):
        with open(os.path.join(THIS_DIR, "./test_parser_file.asm")) as fp:
            insts = [inst for inst in self.parser.get_instruction(fp)]

        expected_insts = [
            *zip(
                range(1, 8),
                ["@R0", "D=M", "@R1", "D=D-M", "@OUTPUT_FIRST", "D;JGT", "@R1", "D=M"],
            )
        ]
        self.assertEqual(insts, expected_insts)
