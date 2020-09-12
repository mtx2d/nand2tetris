import unittest
from lib.instruction import CInstruction


class TestCInstruction(unittest.TestCase):
    def test_from_line(self):
        lines = ["D=M; JMP", "M; JMP", "M=D", "M"]
        insts = [CInstruction.from_line(line) for line in lines]

        expected_insts = [
            CInstruction(None, "D=M", "JMP"),
            CInstruction(None, "M", "JMP"),
            CInstruction(None, "M=D", None),
            CInstruction(None, "M", None),
        ]

        for pair in zip(insts, expected_insts):
            self.assertEqual(pair[0].to_string(), pair[1].to_string())

    def test_from_line_raise_for_invalid_lines(self):
        lines_malformated = ["M=D;;J", "A==D"]
        for line in lines_malformated:
            self.assertRaises(ValueError, CInstruction.from_line, line)
