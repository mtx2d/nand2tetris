class Instruction:
    pass


class AInstruction(Instruction):
    def __init__(self, value):
        self.value = value


class CInstruction(Instruction):
    def __init__(self, dest, comp, jump):
        self.dest = dest
        self.comp = comp
        self.jump = jump


class Label(Instruction):
    def __init__(self, name):
        self.name = name
