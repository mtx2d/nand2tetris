from typing import Callable

from lib.instruction import Instruction, AInstruction, CInstruction
from lib.symbol_table import SymbolTable

dest_map = {
    None: "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111",
}

jump_map = {
    None: "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111",
}

comp_map = {
    "0": "101010",
    "1": "111111",
    "-1": "111010",
    "D": "001100",
    "A": "110000",
    "M": "110000",
    "!D": "001101",
    "!A": "110001",
    "!M": "110001",
    "-D": "001111",
    "-A": "110011",
    "-M": "110011",
    "D+1": "011111",
    "A+1": "110111",
    "M+1": "110111",
    "D-1": "001110",
    "A-1": "110010",
    "M-1": "110010",
    "D+A": "000010",
    "D+M": "000010",
    "D-A": "010011",
    "D-M": "010011",
    "A-D": "000111",
    "M-D": "000111",
    "D&A": "000000",
    "D&M": "000000",
    "D|A": "010101",
    "D|M": "010101",
}


class Encoder:
    def __init__(self):
        self._encoders = {
            type(AInstruction): self._encode_A_instruction,
            type(CInstruction): self._encode_C_instruction,
        }

    def _encode_A_instruction(
        self, inst: AInstruction, st_get_or_add: Callable[[str], int]
    ) -> str:
        if all([v.isdigit() for v in inst.value]):
            return "{0:016b}".format(int(inst.value))[-16:]
        else:
            # symbol lable case
            addr = st_get_or_add(inst.value)
            if inst.value == "math.1":
                print("inst: ", inst.to_string())
                print("addr: ", addr)
            return "{0:016b}".format(addr)[-16:]

    def _encode_C_instruction(self, inst: CInstruction) -> str:
        dest_code = dest_map[inst.dest]
        comp_code = comp_map[inst.comp]
        jump_code = jump_map[inst.jump]
        if "M" in inst.comp:
            return "1111" + comp_code + dest_code + jump_code
        return "1110" + comp_code + dest_code + jump_code

    def encode(self, inst: Instruction, st_get_or_add: Callable[[str], int]) -> str:
        if isinstance(inst, AInstruction):
            return self._encode_A_instruction(inst, st_get_or_add)
        elif isinstance(inst, CInstruction):
            return self._encode_C_instruction(inst)
        else:
            raise ValueError("Do not have encoder for instruction: ", inst)
