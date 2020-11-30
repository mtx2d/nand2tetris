from typing import Dict


class Kind:
    pass


class Static(Kind):
    pass


class Field(Kind):
    pass


class Arg(Kind):
    pass


class Var(Kind):
    pass


class SymbolTable:
    class Entry:
        def __init__(self, name, type, kind, index):
            self.name: str = name
            self.type: str = type
            self.kind: Kind = kind
            self.index: int = index

    def __init__(self):
        self.global_table: Dict[str, SymbolTable.Entry] = {}
        self.subroutine_table: Dict[str, SymbolTable.Entry] = {}

    def start_subroutine(self):
        pass

    def define(self, name, type: str, kind: Kind):
        pass

    def var_count(self) -> int:
        pass

    def kind_of(self, name: str) -> Kind:
        pass

    def type_of(self, name: str) -> str:
        pass

    def index_of(self, name: str) -> int:
        pass
