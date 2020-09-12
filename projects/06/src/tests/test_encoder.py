import unittest
from lib.encoder import Encoder
from lib.instruction import Instruction, AInstruction, CInstruction


class TestEncoder(unittest.TestCase):
    def setUp(self):
        self.encoder = Encoder()

    def test_encode_instruction(self):
        insts = [
            AInstruction(value="123"),
            CInstruction(dest="D", comp="M", jump="JGT"),
            AInstruction(value="0"),
            CInstruction(dest="D", comp="M", jump=None),
            AInstruction(value="1"),
            CInstruction(dest="D", comp="D-M", jump=None),
            AInstruction(value="10"),
            CInstruction(dest=None, comp="D", jump="JGT"),
            AInstruction(value="1"),
            CInstruction(dest="D", comp="M", jump=None),
            AInstruction(value="12"),
            CInstruction(dest=None, comp="0", jump="JMP"),
            AInstruction(value="0"),
            CInstruction(dest="D", comp="M", jump=None),
            AInstruction(value="2"),
            CInstruction(dest="M", comp="D", jump=None),
            AInstruction(value="14"),
            CInstruction(dest=None, comp="0", jump="JMP"),
        ]
        expected_machine_codes = [
            "0000000001111011",
            "1111110000010001",
            "0000000000000000",
            "1111110000010000",
            "0000000000000001",
            "1111010011010000",
            "0000000000001010",
            "1110001100000001",
            "0000000000000001",
            "1111110000010000",
            "0000000000001100",
            "1110101010000111",
            "0000000000000000",
            "1111110000010000",
            "0000000000000010",
            "1110001100001000",
            "0000000000001110",
            "1110101010000111",
        ]
        machine_codes = [self.encoder.encode_instruction(i) for i in insts]

        self.assertEqual(expected_machine_codes, machine_codes)
