
import os

class Parser:
    """
    Parse the Xxx.asm into stream of instructions.
    """
    def __init__(self, path: str):
        self._path = path
        self._count = 0

    def get_instruction(self):
        with open(self._path, 'r') as f:
            count = self._count
            line = f.readline().strip()
            while line.isspace() or not line:
                print('isspace')
                line = f.readline().strip()
            self._count += 1
            yield count, line
