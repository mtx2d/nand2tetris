class Instruction:
    @staticmethod
    def from_line(line) -> "Instruction":
        if line.startswith("push"):
            name, segment, value = line.split(" ")
            return InstPush(segment, int(value))
        elif line.startswith("pop"):
            name, segment, value = line.split(" ")
            return InstPop(segment, int(value))
        elif line.startswith("add"):
            return InstAdd()
        elif line.startswith("sub"):
            return InstSub()
        else:
            raise ValueError("cannot parse line:", line)


class InstPush(Instruction):
    def __init__(self, segment: str, value: int, name: str = "push"):
        self.name = name
        self.segment = segment
        self.value = value

    def __eq__(self, other) -> bool:
        return (
            self.name == other.name
            and self.segment == other.segment
            and self.value == other.value
        )

    def __repr__(self) -> str:
        return " ".join([self.name, self.segment, str(self.value)])


class InstPop(Instruction):
    def __init__(self, segment: str, value: int, name: str = "pop"):
        self.name = name
        self.segment = segment
        self.value = value

    def __eq__(self, other) -> bool:
        return (
            self.name == other.name
            and self.segment == other.segment
            and self.value == other.value
        )

    def __repr__(self) -> str:
        return " ".join([self.name, self.segment, str(self.value)])


class InstAdd(Instruction):
    def __init__(self, name: str = "add"):
        self.name = name

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __repr__(self) -> str:
        return self.name


class InstSub(Instruction):
    def __init__(self, name: str = "sub"):
        self.name = name

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __repr__(self) -> str:
        return self.name
