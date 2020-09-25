from instruction import Instruction

INST_ASM_MAP = {
    "push": CodeWriter.write_push,
    "pop": CodeWriter.write_pop,
    "add": CodeWriter.write_add,
    "sub": CodeWriter.write_sub,
}


class CodeWriter:
    @staticmethod
    def write_push(inst: PushInstruction) -> str:
        """
        addr = segment + value; *SP=*addr; SP++;
        """
        "\n".join([
            "// " + inst.__repr__(),
            f"@{inst.value}",
            "D=A", # D = value
            f"@{inst.segment.upper()}", # @SEGMENT
            "A=D+A", # A = SEGMENT + value -> element addr
            "D=M", # D = *addr

            "@SP",
            "A=M"
            "M=D", # *SP = *addr
            
            "@SP",
            "M=M+1" # SP++
        ])

    def write(self, inst: Instruction) -> str:
        return INST_ASM_MAP[inst.name](inst)
