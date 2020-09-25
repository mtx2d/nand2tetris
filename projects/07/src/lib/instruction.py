class Instruction:
    pass


class InstPush(Instruction):
    def __init__(self, segment: str, value: int, name: str = "push"):
        self.name = name
        self.segment = segment
        self.value = value


class InstPop(Instruction):
    def __init__(self, segment: str, value: int, name: str = "pop"):
        self.name = name
        self.segment = segment
        self.value = value


class InstAdd(Instruction):
    def __init__(self, name: str = "add"):
        self.name = name


class InstNeg(Instruction):
    def __init__(self, name: str = "neg"):
        self.name = name
