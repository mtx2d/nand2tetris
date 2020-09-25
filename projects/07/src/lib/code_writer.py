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
            "A=D+M", # A = value + SEGMENT -> element addr
            "A=M", # D = *addr

            "@SP",
            "A=M"
            "M=D", # *SP = *addr

            "@SP",
            "M=M+1" # SP++
        ])
    
    @staticmethod
    def write_pop(inst: PopInstruction) -> str:
        """
        addr = segment + value;  SP--; *addr = *SP;
        """
        "\n".join([
            "// " + inst.__repr__(),

            f"@{inst.value}"
            "D=A", # D = value
            f"@{inst.segment.upper()}", # @SEGMENT
            "A=D+A",  # A = value + SEGMENT -> element addr -> point to the element in memory
            "D=A" # D = addr

            "@SP",
            "M=M-1", # SP-- 


        ])

    def write(self, inst: Instruction) -> str:
        return INST_ASM_MAP[inst.name](inst)
