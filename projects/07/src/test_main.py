import unittest
import main


class TestMain(unittest.TestCase):
    def test_argument(self):
        args = main.parse_args("main.py input.vm output.asm".split())

        self.assertEqual("input.vm", args.input)
        self.assertEqual("output.asm", args.output)
