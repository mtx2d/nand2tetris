import os
import unittest

from lib.parser import Parser
from lib.instruction import Instruction, AInstruction, CInstruction

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

        for pair in zip(expected_lines, lines):
            self.assertEqual(pair[0], pair[1])

    def test_get_instruction(self):
        num_inst_pairs = [(num, inst) for (num, inst) in self.parser.get_instruction()]

        expected_insts = [
            AInstruction(value="R0"),
            CInstruction(dest="D", comp="M", jump=None),
            AInstruction(value="R1"),
            CInstruction(dest="D", comp="D-M", jump=None),
            CInstruction(dest=None, comp="D", jump="JGT"),
            AInstruction(value="R1"),
            CInstruction(dest="D", comp="M", jump=None),
        ]
        expected_num_inst_pairs = [
            *zip(
                range(1, len(expected_insts)),
                expected_insts,
            )
        ]

        for (exp_num_inst, test_num_inst) in zip(
            expected_num_inst_pairs, num_inst_pairs
        ):
            self.assertEqual(
                exp_num_inst[0], test_num_inst[0]
            )  # check line number match
            self.assertEqual(
                exp_num_inst[1].to_string(),
                test_num_inst[1].to_string(),
            )  # chectk instruction match
