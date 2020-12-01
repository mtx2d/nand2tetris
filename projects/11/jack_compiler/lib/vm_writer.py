from enum import Enum


class Segment(Enum):
    CONST = 0
    ARG = 1
    LOCAL = 2
    STATIC = 3
    THIS = 4
    THAT = 5
    POINTER = 6
    TEMP = 7


class Command(Enum):
    ADD = 0
    SUB = 1
    NEG = 2
    EQ = 3
    GT = 4
    LT = 5
    AND = 6
    OR = 7
    NOT = 8


class VMWriter:
    def __init__(self):
        pass

    def write_push(segment: Segment):
        pass

    def write_pop(segment: Segment):
        pass

    def write_arithmetic(command: Command):
        pass

    def write_label(label: str):
        pass

    def write_goto(label: str):
        pass

    def write_if(label: str):
        pass

    def write_call(name: str, n_args: int):
        pass

    def write_function(name: str, n_locals: int):
        pass

    def write_return():
        pass
