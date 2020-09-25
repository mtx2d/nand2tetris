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
        self.table: dict(str, int) = {k: v for k, v in table.items()}
        self.cnt_free_ram_addr = iter(range(16, PREDEFINED_SYMBOLS["SCREEN"]))

    def add_entry(self, symbol: str, addr: int) -> None:
        # Add program lable, the address here is ROM addr.
        if not self.contains(symbol):
            self.table[symbol] = addr

    def get_address(self, symbol: str) -> int:
        # Compute the adderss to be associated with the given symbol
        if not self.contains(symbol):
            self.table[symbol] = next(self.cnt_free_ram_addr)
        return self.table[symbol]

    def contains(self, symbol) -> bool:
        return symbol in self.table
