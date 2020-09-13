PREDEFINED_SYMBOLS = {
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
    "SCREEN": 16384,
    "KBD": 24576,
}


class SymbolTable:
    def __init__(self, table=PREDEFINED_SYMBOLS):
        self.table: dict(str, int) = table
        self.cnt_free_ram_addr = 16

    def add_label(self, name: str, addr: int) -> None:
        # Add program lable, the address here is ROM addr.
        if not self.has_symbol(name):
            self.table[name] = addr

    def get_or_add(self, name: str) -> int:
        # if not exist, add and then return
        # if exists, directly return
        if not self.has_symbol(name):
            self.table[name] = self.cnt_free_ram_addr
            self.cnt_free_ram_addr += 1
        return self.table[name]

    def has_symbol(self, name) -> bool:
        return name in self.table

    def get(self, name) -> int:
        if not self.has_symbol(name):
            raise ValueError("Does not have such a symbol: ", name)

        return self.table[name]
