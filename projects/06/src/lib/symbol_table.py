class SymbolTable:
    def __init__(self, table={}):
        self.table: dict(str, int) = table

    def add(self, name, addr) -> None:
        if not self.has_symbol(name):
            self.table[name] = addr

    def has_symbol(self, name) -> bool:
        return name in self.table

    def get_address(self, name) -> int:
        if not self.has_symbol(name):
            raise ValueError("Does not have such a symbol: ", name)

        return self.table[name]
