import unittest
import tempfile
import filecmp
import os
import random
import main

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

TEST_ASM_FILES = [
    "../rect/Rect.asm",
    "../rect/RectL.asm",
    "../add/Add.asm",
    "../pong/Pong.asm",
    "../pong/PongL.asm",
    "../max/Max.asm",
    "../max/MaxL.asm",
]

TEST_EXP_HACK_FILES = [
    "../rect/Rect.hack",
    "../rect/Rect.hack",
    "../add/Add.hack",
    "../pong/Pong.hack",
    "../pong/Pong.hack",
    "../max/Max.hack",
    "../max/Max.hack",
]


class TestAssembler(unittest.TestCase):
    def test_parse_args(self):
        args = main.parse_args("main.py in.asm out.hack".split())
        self.assertEqual(args.input, "in.asm")
        self.assertEqual(args.output, "out.hack")

    def test_main(self):
        with tempfile.TemporaryDirectory() as tempdir:
            for (input_asm_file, exp_hack_file) in zip(
                TEST_ASM_FILES, TEST_EXP_HACK_FILES
            ):
                input_file = os.path.join(THIS_DIR, input_asm_file)
                output_file = os.path.join(
                    tempdir, "output{}.hack".format(random.randint(0, 999))
                )
                expected_output_file = os.path.join(THIS_DIR, exp_hack_file)

                main.main("main.py {} {}".format(input_file, output_file).split())

                self.assertTrue(
                    filecmp.cmp(output_file, expected_output_file, shallow=False),
                    "{} is differnt from {}".format(output_file, expected_output_file),
                )
