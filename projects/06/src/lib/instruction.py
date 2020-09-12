from typing import Optional


class Instruction:
    pass


class AInstruction(Instruction):
    def __init__(self, value):
        self.value = value

    def to_string(self):
        return "@" + self.value


class CInstruction(Instruction):
    @classmethod
    def from_line(cls, line: str):
        if line.count(";") > 1:
            raise ValueError('line format error, should not have more than one ";" ')

        if line.count("=") > 1:
            raise ValueError('line format error, should not have more than one "="')

        if "=" in line and ";" in line:
            # D=M; JMP
            dest, tail = line.split("=")
            comp, jump = tail.split(";")
            return cls(dest=dest.strip(), comp=comp.strip(), jump=jump.strip())
        elif ";" in line:
            # M; JMP
            comp, jump = line.split(";")
            return cls(dest=None, comp=comp.strip(), jump=jump.strip())
        elif "=" in line:
            # M=D
            return cls(dest=None, comp=line.strip(), jump=None)
        else:
            # D
            return cls(dest=None, comp=line.strip(), jump=None)

        raise ValueError("line format invalid: ", line)

    def __init__(self, dest: Optional[str], comp: str, jump: Optional[str]):
        self.dest: Optional[str] = dest
        self.comp: str = comp
        self.jump: Optional[str] = jump

    def to_string(self):
        processed_cmd = self.comp
        if self.dest:
            processed_cmd = self.dest + "=" + processed_cmd
        if self.jump:
            processed_cmd = processed_cmd + ";" + self.jump
        return processed_cmd
