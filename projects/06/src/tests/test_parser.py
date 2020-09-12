import unittest
from lib.parser import Parser
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class TestParser(unittest.TestCase):
    def test_get_instruction(self):
        parser = Parser(os.path.join(THIS_DIR, "./test_parser_file.asm"))
        insts = [inst for inst in parser.get_instruction()]

        expected_insts = [
            *zip(
                range(7),
                ["R0", "D=M", "@R1", "D=D-M", "@OUTPUT_FIRST", "D;JGT", "@R1", "D=M"],
            )
        ]
        self.assertEqual(insts, expected_insts)
