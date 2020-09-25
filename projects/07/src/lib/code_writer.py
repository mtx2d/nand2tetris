from .instruction import Instruction

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
        return "\n".join([
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
         SP--; addr = segment + value; *addr = *SP;
        """
        return "\n".join([
            "// " + inst.__repr__(),
            "@SP",
            "M=M-1", # SP-- 

            #---------------------------
            f"@{inst.value}"
            "D=A",
            f"@{inst.segment.upper()}",
            "A=D+A",
            "D=M", # D = *addr

            "@SP"
            "A=M"
            "M=M+D" # *SP = *SP + *addr
            #---------------------------
            "@SP",
            "A=M",
            "D=M", # D = *SP

            f"@{inst.value}"
            "D=A", 
            f"@{inst.segment.upper()}",
            "A=D+A",
            "M=D-M" # *addr = *SP - *addr
            #-------------------------- 
            f"@{inst.value}"
            "D=A",
            f"@{inst.segment.upper()}",
            "A=D+A",
            "D=M", # D = *addr

            "@SP",
            "A=M",
            "M=M-D", # *SP = *SP - *addr 
        ])
    
    @staticmethod
    def write_add(inst: AddInstruction) -> str:
        return "\n".join([
            "@SP",
            "M=M-1" # SP--

            "@SP",
            "A=M",
            "D=M", # D = op1

            "@SP",
            "M=M-1" # SP--

            "@SP",
            "A=M",
            "M=M+D" # add op2 op1

            "@SP",
            "M=M+1", # SP++
        ])
    
    @staticmethod
    def write_sub(inst: SubInstruction) -> str:
        return "\n".join([
            "@SP",
            "M=M-1", # SP--
            
            "@SP",
            "A=M", 
            "M=-M", # -y
            "D=M",

            "@SP",
            "M=M-1", # SP--

            "@SP",
            "A=M", 
            "M=D+M" # x - y

            "@SP",
            "M=M+1", # SP++
        ])
    
    @staticmethod
    def write_sub(inst: SubInstruction) -> str:
        return "\n".join([
            ""
        ])

    def write(self, inst: Instruction) -> str:
        return INST_ASM_MAP[inst.name](inst)
