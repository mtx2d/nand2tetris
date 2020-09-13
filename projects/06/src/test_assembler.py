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

    def test_assembling_add(self):
        with tempfile.TemporaryDirectory() as tempdir:
            input_file = os.path.join(THIS_DIR, TEST_ASM_FILES[0])
            output_file = os.path.join(tempdir, "output.hack")
            expected_output_file = os.path.join(THIS_DIR, TEST_EXP_HACK_FILES[0])

            assembler.main(
                "assember.py {} {}".format(input_file, output_file).split()
            )

            with open(output_file) as f:
                print(f.read())
            

            with open(expected_output_file) as f:
                print(f.read())

            self.assertTrue(
                filecmp.cmp(output_file, expected_output_file),
                "File differ: {} differnt from ground truth {}".format(
                    output_file, expected_output_file
                ),
            )
