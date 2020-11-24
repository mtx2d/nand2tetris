from typing import Dict


class Type:
    pass


class Kind:
    pass


class SymbolTable:
    class Entry:
        def __init__(self, name, type, kind, index):
            self.name: str = name
            self.type: Type = type
            self.kind: Kind = kind
            self.index: int = index

    def __init__(self):
        self.global_table: Dict[str, SymbolTable.Entry] = {}
        self.subroutine_table: Dict[str, SymbolTable.Entry] = {}

    def start_subroutine(self):
        pass

    def define(self):
        pass

    def var_count(self) -> int:
        pass

    def kind_of(self, name: str) -> Kind:
        pass

    def type_of(self, name: str) -> Type:
        pass

    def index_of(self, name: str) -> int:
        pass
