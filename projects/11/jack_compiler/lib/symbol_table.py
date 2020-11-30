from typing import DefaultDict, Dict


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
        self.var_count: Dict[Kind, int] = DefaultDict{}

    def start_subroutine(self):
        pass

    def define(self, name: str, type: str, kind: Kind):
        if not isinstance(kind, Kind):
            raise ValueError(f"invalid identifier kind: {kind}")
        new_entry = SymbolTable.Entry(name, type, kind, self.var_count(kind) + 1)
        self.global_table[name] =  new_entry
        self.var_count[kind] += 1

    def var_count(self, kind: Kind) -> int:
        pass

    def kind_of(self, name: str) -> Kind:
        pass

    def type_of(self, name: str) -> str:
        pass

    def index_of(self, name: str) -> int:
        pass
