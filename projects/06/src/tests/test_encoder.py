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
            CInstruction(dest="D", comp="D-M", jump=None),
        ]
        expected_machine_codes = [
            "0000000001111011", 
            "1111110000010001",
            "0000000000000000",
            "1111110000010000",
            "1111010011010000",
        ]
        machine_codes = [self.encoder.encode_instruction(i) for i in insts]

        self.assertEqual(expected_machine_codes, machine_codes)
