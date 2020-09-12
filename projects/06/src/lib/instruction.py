from typing import Optional


class Instruction:
    pass


class AInstruction(Instruction):
    def __init__(self, value):
        self.value = value

    def to_string(self):
        return "@" + self.value

    def __repr__(self):
        return self.to_string()


class CInstruction(Instruction):
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

    def __repr__(self):
        return self.to_string()
