class Instruction:
    pass


class AInstruction(Instruction):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "@" + self.value


class CInstruction(Instruction):

    @classmethod
    def from_line(cls, line: str):
        dest, line = line.split("=")
        comp, jump = line.split(";")
        return cls(dest=dest.strip(), comp=comp.strip(), jump=jump.strip())

    def __init__(self, dest: str, comp: str, jump: str):
        self.dest: str = dest
        self.comp: str = comp
        self.jump: str = jump

    def __repr__(self):
        processed_cmd = self.comp
        if self.dest:
            processed_cmd = self.dest + "=" + processed_cmd
        if self.jump:
            processed_cmd = processed_cmd + ";" + self.jump
        return processed_cmd

