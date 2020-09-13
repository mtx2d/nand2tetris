import unittest
from assembler import main

TEST_ASM_FILES=[
    '../add/Add.asm',
    '../max/Max.asm',
    '../max/MaxL.asm',
    '../pong/Pong.asm',
    '../pong/PongL.asm',
    '../rect/Rect.asm',
    '../rect/RectL.asm'
]

class TestAssembler(unittest.TestCase):
    def test_assembler(self):
        pass