from lib.instruction import Instruction, AInstruction, CInstruction

dest_map = {}
jump_map = {}
comp_map = {
    "M": "1232",
}


class Encoder:
    def __init__(self):
        pass

    def encode_instruction(self, instruction: Instruction) -> str:
        pass
