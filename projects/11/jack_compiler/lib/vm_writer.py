class Segment:
    pass


class Command:
    pass


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
