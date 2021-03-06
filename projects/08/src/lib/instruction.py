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
        elif line.startswith("eq"):
            return InstEq()
        elif line.startswith("lt"):
            return InstLt()
        elif line.startswith("gt"):
            return InstGt()
        elif line.startswith("neg"):
            return InstNeg()
        elif line.startswith("and"):
            return InstAnd()
        elif line.startswith("or"):
            return InstOr()
        elif line.startswith("not"):
            return InstNot()
        elif line.startswith("label"):
            _, label_name = line.split()
            return InstLabel(label_name)
        elif line.startswith("if-goto"):
            _, label_name = line.split()
            return InstIfGoto(label_name)
        elif line.startswith("goto"):
            _, label_name = line.split()
            return InstGoto(label_name)
        elif line.startswith("function"):
            _, function_name, n_local = line.split()
            return InstFunction(function_name, n_local)
        elif line.startswith("return"):
            return InstReturn()
        elif line.startswith("call"):
            _, function_name, n_args = line.split()
            return InstCall(function_name, int(n_args))
        else:
            raise ValueError("cannot parse line:", line)


class InstCall(Instruction):
    def __init__(self, function_name, n_args: int):
        self.name = "call"
        self.function_name = function_name
        self.n_args = n_args

    def __eq__(self, other) -> bool:
        return (
            self.name == other.name
            and self.function_name == other.function_name
            and self.n_args == other.n_args
        )

    def __repr__(self) -> str:
        return " ".join([self.name, self.function_name, str(self.n_args)])


class InstReturn(Instruction):
    def __init__(self):
        self.name = "return"

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __repr__(self) -> str:
        return "return"


class InstFunction(Instruction):
    def __init__(self, function_name, n_local):
        self.name = "function"
        self.function_name = function_name
        self.n_local = n_local

    def __eq__(self, other) -> bool:
        return (
            self.name == other.name
            and self.function_name == other.function_name
            and self.n_local == other.n_local
        )

    def __repr__(self) -> str:
        return " ".join([self.name, self.function_name, self.n_local])


class InstGoto(Instruction):
    def __init__(self, value: str, name: str = "goto"):
        self.name = name
        self.value = value

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.value == other.value

    def __repr__(self) -> str:
        return " ".join([self.name, self.value])


class InstIfGoto(Instruction):
    def __init__(self, value: str, name: str = "if-goto"):
        self.name = name
        self.value = value

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.value == other.value

    def __repr__(self) -> str:
        return " ".join([self.name, self.value])


class InstLabel(Instruction):
    def __init__(self, value: str, name: str = "label"):
        self.name = name
        self.value = value

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.value == other.value

    def __repr__(self) -> str:
        return " ".join([self.name, self.value])


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


class InstEq(Instruction):
    def __init__(self, name: str = "eq"):
        self.name = name

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __repr__(self) -> str:
        return self.name


class InstLt(Instruction):
    def __init__(self, name: str = "lt"):
        self.name = name

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __repr__(self) -> str:
        return self.name


class InstGt(Instruction):
    def __init__(self, name: str = "gt"):
        self.name = name

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __repr__(self) -> str:
        return self.name


class InstOr(Instruction):
    def __init__(self, name: str = "or"):
        self.name = name

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __repr__(self) -> str:
        return self.name


class InstNot(Instruction):
    def __init__(self, name: str = "not"):
        self.name = name

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __repr__(self) -> str:
        return self.name


class InstNeg(Instruction):
    def __init__(self, name: str = "neg"):
        self.name = name

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __repr__(self) -> str:
        return self.name


class InstAnd(Instruction):
    def __init__(self, name: str = "and"):
        self.name = name

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __repr__(self) -> str:
        return self.name
