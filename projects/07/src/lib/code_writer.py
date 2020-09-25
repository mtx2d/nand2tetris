from .instruction import (
    Instruction,
    InstPush,
    InstPop,
    InstAdd,
    InstSub,
)


class CodeWriter:
    @staticmethod
    def write_push(inst: InstPush) -> str:
        """
        addr = segment + value; *SP=*addr; SP++;
        """
        return "\n".join(
            [
                "// " + inst.__repr__(),
                f"@{inst.value}",
                "D=A",  # D = value
                f"@{inst.segment.upper()}",  # @SEGMENT
                "A=D+M",  # A = value + SEGMENT -> element addr
                "D=M",  # D = *addr
                "@SP",
                "A=M",
                "M=D",  # *SP = *addr
                "@SP",
                "M=M+1",  # SP++
            ]
        )

    @staticmethod
    def write_pop(inst: InstPop) -> str:
        """
        SP--; addr = segment + value; *addr = *SP;
        """
        return "\n".join(
            [
                "// " + inst.__repr__(),
                "@SP",
                "M=M-1",  # SP--
                # ---------------------------
                f"@{inst.value}",
                "D=A",
                f"@{inst.segment.upper()}",
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
                f"@{inst.segment.upper()}",
                "A=D+A",
                "M=D-M"  # *addr = *SP - *addr
                # --------------------------
                f"@{inst.value}",
                "D=A",
                f"@{inst.segment.upper()}",
                "A=D+A",
                "D=M",  # D = *addr
                "@SP",
                "A=M",
                "M=M-D",  # *SP = *SP - *addr
            ]
        )

    @staticmethod
    def write_add(inst: InstAdd) -> str:
        return "\n".join(
            [
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
        return INST_ASM_MAP[inst.name](inst)


INST_ASM_MAP = {
    "push": CodeWriter.write_push,
    "pop": CodeWriter.write_pop,
    "add": CodeWriter.write_add,
    "sub": CodeWriter.write_sub,
}
