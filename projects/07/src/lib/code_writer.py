import os
import itertools
from pathlib import Path

from .instruction import (
    Instruction,
    InstPush,
    InstPop,
    InstAdd,
    InstSub,
    InstEq,
    InstLt,
    InstGt,
    InstNeg,
    InstOr,
    InstNot,
)

HACK_MEM_SYMBOL_MAP = {
    "local": "LCL",
    "argument": "ARG",
    "this": "THIS",
    "that": "THAT",
}


class CodeWriter:
    label_id = itertools.count()

    @staticmethod
    def get_next_label_id():
        return next(CodeWriter.label_id)

    def __init__(self, input_file):
        self.filename = Path(input_file).stem
        self.inst_asm_map = {
            "push": self.write_push,
            "pop": self.write_pop,
            "add": CodeWriter.write_add,
            "sub": CodeWriter.write_sub,
            "eq": CodeWriter.write_eq,
            "lt": CodeWriter.write_lt,
            "gt": CodeWriter.write_gt,
            "neg": CodeWriter.write_neg,
            "or": CodeWriter.write_or,
            "and": CodeWriter.write_and,
            "not": CodeWriter.write_not,
        }
    
    @staticmethod
    def write_neg(inst: InstNeg) -> str:
        return "\n".join([ 
            "// " + inst.__repr__(),
            "@SP",
            "A=M-1",
            "M=-M",
        ])

    @staticmethod
    def write_not(inst: InstNot) -> str:
        return "\n".join([ 
            "// " + inst.__repr__(),
            "@SP",
            "A=M-1",
            "M=!M",
        ])
    
    @staticmethod
    def write_or(inst: InstOr) -> str:
        return "\n".join([
            "// " + inst.__repr__(),
            "@SP",
            "A=M-1",
            "D=M",

            "@SP",
            "M=M-1",
            "A=M-1",
            "M=D|M"
        ])

    
    @staticmethod
    def write_and(inst: InstAnd) -> str:
        return "\n".join([
            "// " + inst.__repr__(),
            "@SP",
            "A=M-1",
            "D=M",

            "@SP",
            "M=M-1",
            "A=M-1",
            "M=D&M"
        ])

    @staticmethod
    def write_lt(inst: InstLt) -> str:
        block_id = CodeWriter.get_next_label_id()
        IF = f"IF_{block_id}"
        END = f"END_{block_id}"
        return "\n".join(
            [
                "// " + inst.__repr__(),
                "@SP",
                "M=M-1",
                "A=M",
                "D=M",
                "@SP",
                "A=M-1",
                "D=M-D",
                f"@{IF}",
                "D;JLT",
                "@SP",  # ELSE_BRANCH
                "A=M-1",
                "M=0",  # set to false
                f"@{END}",
                "0;JMP",
                f"({IF})",
                "@SP",
                "A=M-1",
                "M=-1",  # set to true
                f"({END})",
            ]
        )

    @staticmethod
    def write_gt(inst: InstGt) -> str:
        block_id = CodeWriter.get_next_label_id()
        IF = f"IF_{block_id}"
        END = f"END_{block_id}"
        return "\n".join(
            [
                "// " + inst.__repr__(),
                "@SP",
                "M=M-1",
                "A=M",
                "D=M",
                "@SP",
                "A=M-1",
                "D=M-D",
                f"@{IF}",
                "D;JGT",
                "@SP",  # ELSE_BRANCH
                "A=M-1",
                "M=0",  # set to false
                f"@{END}",
                "0;JMP",
                f"({IF})",
                "@SP",
                "A=M-1",
                "M=-1",  # set to true
                f"({END})",
            ]
        )

    @staticmethod
    def write_eq(inst: InstEq) -> str:
        block_id = CodeWriter.get_next_label_id()
        IF = f"IF_{block_id}"
        END = f"END_{block_id}"
        return "\n".join(
            [
                "// " + inst.__repr__(),
                "@SP",
                "M=M-1",
                "A=M",
                "D=M",
                "@SP",
                "A=M-1",
                "D=D-M",
                f"@{IF}",
                "D;JEQ",
                "@SP",
                "A=M-1",
                "M=0",  # set to false
                f"@{END}",
                "0;JMP",
                f"({IF})",
                "@SP",
                "A=M-1",
                "M=-1",  # set to true
                f"({END})",
            ]
        )

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
            return "\n".join(
                [
                    "// " + inst.__repr__(),
                    f"@R{5 + inst.value}",
                    "D=M",
                    "@SP",
                    "A=M",
                    "M=D",
                    "@SP",
                    "M=M+1",
                ]
            )
        elif inst.segment == "pointer":
            # *SP=THIS/THAT, SP++
            POINTER = "THIS" if inst.value == 0 else "THAT"
            return "\n".join(
                [
                    "// " + inst.__repr__(),
                    f"@{POINTER}",
                    "A=M",
                    "D=M",
                    "@SP",
                    "A=M",
                    "M=D",
                ]
            )
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
                    "A=M",
                    "D=D+A",  # D = addr
                    "@SP",
                    "A=M",
                    "D=D+M",  # D = addr + stack_top_val
                    "A=D-M",
                    "D=D-A",
                    "M=D",
                ]
            )
        elif inst.segment == "static":
            return "\n".join(
                [
                    "// " + inst.__repr__(),
                    "@SP",
                    "M=M-1",
                    "@SP",
                    "A=M",
                    "D=M",
                    f"@{self.filename}.{inst.value}",
                    "M=D",
                ]
            )
        elif inst.segment == "temp":
            return "\n".join(
                [
                    "// " + inst.__repr__(),
                    "@SP",
                    "M=M-1",
                    "A=M",
                    "D=M",
                    f"@R{5 + inst.value}",
                    "M=D",
                ]
            )
        elif inst.segment == "pointer":
            # SP--, THIS/THAT = *SP
            POINTER = "THIS" if inst.value == 0 else "THAT"
            return "\n".join(
                [
                    "// " + inst.__repr__(),
                    "@SP",
                    "A=M-1",
                    "D=M",
                    f"@{POINTER}",
                    "M=D",
                ]
            )
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
