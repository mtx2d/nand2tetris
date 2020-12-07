from collections import defaultdict
from typing import DefaultDict, Dict


class SymbolTable:
    class Entry:
        def __init__(self, name, type, kind, index):
            self.name: str = name
            self.type: str = type
            self.kind: str = kind
            self.index: int = index

    def __init__(self):
        self.global_table: Dict[str, SymbolTable.Entry] = {}
        self.global_table["this"] = SymbolTable.Entry(
            "this", "TYPE_OF_THE_CLASS", "argument", 0
        )
        self.subroutine_table: Dict[str, SymbolTable.Entry] = {}
        self.var_count: Dict[str, int] = defaultdict(int)

    def start_subroutine(self):
        for k, v in self.subroutine_table.items():
            self.var_count[v.kind] -= 1
        self.subroutine_table.clear()

    def define(self, name: str, type: str, kind: str):
        if name in self.global_table:
            raise ValueError(f"{name} already defined")

        if name in self.subroutine_table:
            raise ValueError(f"{name} already defined")

        new_entry = SymbolTable.Entry(name, type, kind, self.var_count[kind])
        if kind in ["static", "field"]:
            self.global_table[name] = new_entry
        elif kind in ["argument", "var"]:
            self.subroutine_table[name] = new_entry
        else:
            raise ValueError(f"Unknown kind: {kind}")

        self.var_count[kind] += 1

    def var_count(self, kind: str) -> int:
        if kind not in self.var_count:
            raise ValueError(f"invalid kind: {kind}")
        return self.var_count[kind]

    def kind_of(self, name: str) -> str:
        if name in self.subroutine_table:
            return self.subroutine_table[name].kind

        if name in self.global_table:
            return self.global_table[name].kind

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
