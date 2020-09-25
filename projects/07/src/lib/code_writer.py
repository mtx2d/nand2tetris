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
            "D=M", # D = *addr

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
            "M=D+M",  # update @SEGMENT to point to LCL + val

            "@SP",
            "M=M-1", # SP-- 

            "@SP",  
            "A=M", 
            "D=M", # D=*SP

            f"@{inst.segment.upper()}",
            "A=M",
            "M=D", # *addr = *SP
        
            #need to set back to LCL
            f"@{inst.value}"
            "D=A", # D = value
            f"@{inst.segment.upper()}",
            "M=M-D"
        ])

    def write(self, inst: Instruction) -> str:
        return INST_ASM_MAP[inst.name](inst)
