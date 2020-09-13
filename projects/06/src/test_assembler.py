import unittest
import assembler
import tempfile
import filecmp
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

TEST_ASM_FILES = [
    "../add/Add.asm",
    "../max/Max.asm",
    "../max/MaxL.asm",
    "../pong/Pong.asm",
    "../pong/PongL.asm",
    "../rect/Rect.asm",
    "../rect/RectL.asm",
]

TEST_EXP_HACK_FILES = ["../add/Expected_Add.hack"]


class TestAssembler(unittest.TestCase):
    def test_parse_args(self):
        args = assembler.parse_args("assembler.py in.asm out.hack".split())
        self.assertEqual(args.input, "in.asm")
        self.assertEqual(args.output, "out.hack")

    def test_assembling(self):
        for (input_asm_file, exp_hack_file) in zip(TEST_ASM_FILES, TEST_EXP_HACK_FILES):
            with tempfile.TemporaryDirectory() as tempdir:
                input_file = os.path.join(THIS_DIR, input_asm_file)
                output_file = os.path.join(tempdir, "output.hack")
                expected_output_file = os.path.join(THIS_DIR, exp_hack_file)

                assembler.main(
                    "assember.py {} {}".format(input_file, output_file).split()
                )

                self.assertTrue(
                    filecmp.cmp(output_file, expected_output_file),
                    "{} is differnt from {}".format(output_file, expected_output_file),
                )
