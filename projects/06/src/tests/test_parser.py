import os
import unittest

from lib.parser import Parser
from lib.instruction import Instruction, AInstruction, CInstruction, LInstruction

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
        insts = [inst for inst in self.parser.get_instruction()]

        expected_insts = [
            AInstruction(value="R0"),
            CInstruction(dest="D", comp="M", jump=None),
            AInstruction(value="R1"),
            CInstruction(dest="D", comp="D-M", jump=None),
            CInstruction(dest=None, comp="D", jump="JGT"),
            AInstruction(value="R1"),
            CInstruction(dest="D", comp="M", jump=None),
            LInstruction(name="INFINITE_LOOP"),
            AInstruction(value="INFINITE_LOOP"),
            CInstruction(dest=None, comp="0", jump="JMP"),
            LInstruction(name="END EQ"),
            AInstruction(value="END EQ"),
            CInstruction(dest=None, comp="D", jump="JNE"),
        ]

        # TODO implement __eq__ for all these instructions
        for (exp_inst, inst) in zip(expected_insts, insts):
            if isinstance(exp_inst, AInstruction):
                self.assertEqual(exp_inst.value, inst.value)
            elif isinstance(exp_inst, LInstruction):
                self.assertEqual(exp_inst.name, inst.name)
            else:
                self.assertEqual(
                    exp_inst.dest,
                    inst.dest,
                )
                self.assertEqual(
                    exp_inst.comp,
                    inst.comp,
                )
                self.assertEqual(
                    exp_inst.jump,
                    inst.jump,
                )

    def test__parse_c_instruction(self):
        # normal line cases
        lines = ["D=M; JMP", "M; JMP", "M=D", "M", "AM=M-1"]
        insts = [self.parser._parse_c_instruction(line) for line in lines]

        expected_insts = [
            CInstruction("D", "M", "JMP"),
            CInstruction(None, "M", "JMP"),
            CInstruction("M", "D", None),
            CInstruction(None, "M", None),
            CInstruction("AM", "M-1", None),
        ]

        for pair in zip(insts, expected_insts):
            self.assertEqual(pair[0].to_string(), pair[1].to_string())

        # bad line cases
        lines_malformated = ["M=D;;J", "A==D"]
        for line in lines_malformated:
            self.assertRaises(ValueError, self.parser._parse_c_instruction, line)
