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
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "M": "1110000",
    "!D": "0001101",
    "!A": "0110001",
    "!M": "1110001",
    "-D": "0001111",
    "-A": "0110011",
    "-M": "1110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "M+1": "1110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "M-1": "1110010",
    "D+A": "0000010",
    "D+M": "1000010",
    "D-A": "0010011",
    "D-M": "1010011",
    "A-D": "0000111",
    "M-D": "1000111",
    "D&A": "0000000",
    "D&M": "1000000",
    "D|A": "0010101",
    "D|M": "1010101",
}


class Encoder:

    def _encode_A_instruction(
        self, inst: AInstruction, st_get_or_add: Callable[[str], int]
    ) -> str:
        if all([v.isdigit() for v in inst.value]):
            return "{0:0>16b}".format(int(inst.value))
        else:
            # symbol lable case
            addr = st_get_or_add(inst.value)
            return "{0:0>16b}".format(addr)

    def _encode_C_instruction(self, inst: CInstruction) -> str:
        dest_code = dest_map[inst.dest]
        comp_code = comp_map[inst.comp]
        jump_code = jump_map[inst.jump]
        return "111{}{}{}".format(comp_code, dest_code, jump_code)

    def encode(self, inst: Instruction, st_get_or_add: Callable[[str], int]) -> str:
        if isinstance(inst, AInstruction):
            return self._encode_A_instruction(inst, st_get_or_add)
        elif isinstance(inst, CInstruction):
            return self._encode_C_instruction(inst)
        else:
            raise ValueError("Do not have encoder for instruction: ", inst)
