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
        ]
        machine_codes = [self.encoder.encode_instruction(i) for i in insts]

        expected_machine_codes = ["0000000001111011", "1111110000010001"]

        self.assertEqual(machine_codes, expected_machine_codes)
