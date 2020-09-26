import os

from .instruction import (
    Instruction,
    InstPush,
    InstPop,
    InstAdd,
    InstSub,
)

HACK_MEM_SYMBOL_MAP = {
    "local": "LCL",
    "argument": "ARG",
    "this": "THIS",
    "that": "THAT",
}


class CodeWriter:
    def __init__(self, input_file):
        self.filename = os.path.basename(input_file)
        self.inst_asm_map = {
            "push": self.write_push,
            "pop": self.write_pop,
            "add": CodeWriter.write_add,
            "sub": CodeWriter.write_sub,
        }

    def write_push(self, inst: InstPush) -> str:
        """
        addr = segment + value; *SP=*addr; SP++;
        """
        if inst.segment in HACK_MEM_SYMBOL_MAP.keys():
            return "\n".join(
                [
                    "// " + inst.__repr__(),
                    f"@{inst.value}",
                    "D=A",  # D = value
                    f"@{HACK_MEM_SYMBOL_MAP[inst.segment]}",  # @SEGMENT
                    "A=D+M",  # A = value + SEGMENT -> element addr
                    "D=M",  # D = *addr
                    "@SP",
                    "A=M",
                    "M=D",  # *SP = *addr
                    "@SP",
                    "M=M+1",  # SP++
                ]
            )
        elif inst.segment == "constant":
            return "\n".join(
                [
                    "// " + inst.__repr__(),
                    f"@{str(inst.value)}",
                    "D=A",
                    "@SP",
                    "A=M",
                    "M=D",
                    "@SP",
                    "M=M+1",
                ]
            )
        elif inst.segment == "static":
            return "\n".join(
                [
                    "// " + inst.__repr__(),
                    f"@{self.filename}.{str(inst.value)}",
                    "D=M",
                    "@SP",
                    "A=M",
                    "M=D",
                    "@SP",
                    "M=M+1",
                ]
            )
        elif inst.segment == "temp":
            return "\n".join([
                "// " + inst.__repr__(),
                f"@R{5 + inst.value}",
                "D=M",
                "@SP",
                "A=M",
                "M=D",
                "@SP",
                "M=M+1",
            ])
        elif inst.segment == "pointer":
            return "\n".join([

            ])
        else:
            raise ValueError("Could not gen code for:", inst)

    def write_pop(self, inst: InstPop) -> str:
        """
        SP--; addr = segment + value; *addr = *SP;
        """
        if inst.segment in HACK_MEM_SYMBOL_MAP.keys():
            return "\n".join(
                [
                    "// " + inst.__repr__(),
                    "@SP",
                    "M=M-1",  # SP--
                    # ---------------------------
                    f"@{inst.value}",
                    "D=A",
                    f"@{HACK_MEM_SYMBOL_MAP[inst.segment]}",
                    "A=D+A",
                    "D=M",  # D = *addr
                    "@SP",
                    "A=M",
                    "M=M+D",  # *SP = *SP + *addr
                    # ---------------------------
                    "@SP",
                    "A=M",
                    "D=M",  # D = *SP
                    f"@{inst.value}",
                    "D=A",
                    f"@{HACK_MEM_SYMBOL_MAP[inst.segment]}",
                    "A=D+A",
                    "M=D-M",  # *addr = *SP - *addr
                    # --------------------------
                    f"@{inst.value}",
                    "D=A",
                    f"@{HACK_MEM_SYMBOL_MAP[inst.segment]}",
                    "A=D+A",
                    "D=M",  # D = *addr
                    "@SP",
                    "A=M",
                    "M=M-D",  # *SP = *SP - *addr
                ]
            )
        elif inst.segment == "static":
            return "\n".join(
                [
                    "// " + inst.__repr__(),
                    "@SP",
                    "A=M",
                    "D=M",
                    "@SP",
                    "M=M-1",
                    f"@{self.filename}.{inst.value}",
                    "M=D",
                ]
            )
        elif inst.segment == "temp":
            return "\n".join([
                "// " + inst.__repr__(),
                "@SP",
                "M=M-1",
                "A=M",
                "D=M",
                f"R@{5 + inst.value}",
                "M=D",
            ])
        elif inst.segment == "pointer":
            return "\n".join([])
        else:
            raise ValueError("Could not gen code for:", inst)


    @staticmethod
    def write_add(inst: InstAdd) -> str:
        return "\n".join(
            [
                "// " + inst.__repr__(),
                "@SP",
                "M=M-1",
                "@SP",  # SP--
                "A=M",
                "D=M",  # D = op1
                "@SP",
                "M=M-1",
                "@SP",  # SP--
                "A=M",
                "M=M+D",
                "@SP",  # add op2 op1
                "M=M+1",  # SP++
            ]
        )

    @staticmethod
    def write_sub(inst: InstSub) -> str:
        return "\n".join(
            [
                "// " + inst.__repr__(),
                "@SP",
                "M=M-1",  # SP--
                "@SP",
                "A=M",
                "M=-M",  # -y
                "D=M",
                "@SP",
                "M=M-1",  # SP--
                "@SP",
                "A=M",
                "M=D+M",
                "@SP",  # x - y
                "M=M+1",  # SP++
            ]
        )

    def write(self, inst: Instruction) -> str:
        return self.inst_asm_map[inst.name](inst)


