class Instrucion:
    pass


class AInstruction(Instruction):
    pass


class CInstruction(Instruction):
    pass


class Encoder:
    def __init__(self):
        pass

    def encode_instruction(self, instruction: str) -> Instruction:
        "should this return inst binary string or Class Inst?"
        pass
