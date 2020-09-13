import unittest
import assembler
import tempfile
import filecmp
import os

TEST_ASM_FILES = [
    "../add/Add.asm",
    "../max/Max.asm",
    "../max/MaxL.asm",
    "../pong/Pong.asm",
    "../pong/PongL.asm",
    "../rect/Rect.asm",
    "../rect/RectL.asm",
]

TEST_EXP_HACK_FILES = ["../add/Add/Expected_Add.hack"]


class TestAssembler(unittest.TestCase):
    def test_main(self):
        with self.assertRaises(SystemExit):
            assembler.main(["assembler.py"])

    def test_parse_args(self):
        args = assembler.parse_args("assembler.py in.asm out.hack".split())
        self.assertEqual(args.input, "in.asm")
        self.assertEqual(args.output, "out.hack")

    def test_assembling_add(self):
        with tempfile.TemporaryDirectory() as tempdir:
            output = os.path.join(tempdir, "output.hack")
            assembler.main(
                "assember.py {} {}".format(TEST_ASM_FILES[0], output).split()
            )

            self.assertTrue(
                filecmp.cmp(output, TEST_EXP_HACK_FILES[0], shallow=False),
                "File differ: {} differnt from ground truth {}".format(
                    output, TEST_EXP_HACK_FILES[0]
                ),
            )
