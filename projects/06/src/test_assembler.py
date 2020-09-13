import unittest
import assembler

TEST_ASM_FILES = [
    "../add/Add.asm",
    "../max/Max.asm",
    "../max/MaxL.asm",
    "../pong/Pong.asm",
    "../pong/PongL.asm",
    "../rect/Rect.asm",
    "../rect/RectL.asm",
]


class TestAssembler(unittest.TestCase):
    def test_main(self):
        with self.assertRaises(SystemExit):
            assembler.main(["assembler.py"])

    def test_parse_args(self):
        args = assembler.parse_args("assembler.py in.asm out.hack".split())
        self.assertEqual(args.input, "in.asm")
        self.assertEqual(args.output, "out.hack")
