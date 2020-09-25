class Instruction:
    pass


class InstPush(Instruction):
    def __init__(self, segment: str, value: int, name: str = "push"):
        self.name = name
        self.segment = segment
        self.value = value

    def __eq__(self, other):
        self.name = other.name
        self.segment = other.segment
        self.value = other.value


class InstPop(Instruction):
    def __init__(self, segment: str, value: int, name: str = "pop"):
        self.name = name
        self.segment = segment
        self.value = value

    def __eq__(self, other):
        self.name = other.name
        self.segment = other.segment
        self.value = other.value


class InstAdd(Instruction):
    def __init__(self, name: str = "add"):
        self.name = name

    def __eq__(self, other):
        self.name = other.name


class InstSub(Instruction):
    def __init__(self, name: str = "sub"):
        self.name = name

    def __eq__(self, other):
        self.name = other.name
