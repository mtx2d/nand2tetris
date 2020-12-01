from collections import defaultdict
from enum import Enum
from typing import DefaultDict, Dict


class SymbolTable:
    class Entry:
        def __init__(self, name, type, kind, index):
            self.name: str = name
            self.type: str = type
            self.kind: str = kind
            self.index: int = index

    class Kind(Enum):
        STATIC = 1
        FIELD = 2
        VAR = 3
        ARG = 4

    def __init__(self):
        self.global_table: Dict[str, SymbolTable.Entry] = {}
        self.subroutine_table: Dict[str, SymbolTable.Entry] = {}
        self.var_count: Dict[str, int] = defaultdict(int)

    def start_subroutine(self):
        self.subroutine_table.clear()

    def define(self, name: str, type: str, kind: str):
        new_entry = SymbolTable.Entry(name, type, kind, self.var_count(kind) + 1)
        # symbol exist, new definition overrides old definition
        if kind in ["static", "field"]:
            self.global_table[name] = new_entry
        elif kind in ["arg", "var"]:
            self.subroutine_table[name] = new_entry
        else:
            raise ValueError(f"Unknown kind: {kind}")

        if name in self.global_table:
            return
        if name in self.subroutine_table:
            return
        # symbol does not exist before add count
        self.var_count[kind] += 1

    def var_count(self, kind: str) -> int:
        if kind not in self.var_count:
            raise ValueError(f"invalid kind: {kind}")
        return self.var_count[kind]

    def kind_of(self, name: str) -> str:
        if name in self.subroutine_table:
            return self.subroutine_table[name]

        if name in self.global_table:
            return self.global_table[name]

        raise ValueError(f"name not found: {name}")

    def type_of(self, name: str) -> str:
        if name in self.subroutine_table:
            return self.subroutine_table[name]

        if name in self.global_table:
            return self.global_table[name]

        raise ValueError(f"name not found: {name}")

    def index_of(self, name: str) -> int:
        if name in self.subroutine_table:
            return self.subroutine_table[name].index

        if name in self.global_table:
            return self.global_table[name].index

        raise ValueError(f"name not found: {name}")
