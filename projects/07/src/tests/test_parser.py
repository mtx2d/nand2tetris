import mock
import unittest
from lib.parser import Parser
from lib.instructions import InstPush, InstPop, InstAdd, InstNeg


class TestParser(unittest.TestCase):
    def test_strip_comments(self):
        lines = [
            Parser.strip_comments("push constant 10            // first comment"),
            Parser.strip_comments("pop constant 22        // another comment"),
            Parser.strip_comments(" add              // add something"),
        ]
        expected_lines = ["push constant 10", "pop constant 22", "add"]

        for pair in zip(expected_lines, lines):
            self.assertEqual(pair[0], pair[1])

    def test_parse(self):
        read_data = [
            "push constant 10",
            "pop local 0",
            "pop argument 1",
            "push argument 1",
            "pop this 6",
            "add",
            "sub",
        ]
        mock_open = mock.mock_open(read_data=read_data)

        insts = [*Parser("some_file_path").parser()]

        exp_insts = [
            InstPush("constant", 10),
            InstPop("local", 0),
            InstPop("argument", 1),
            InstPush("argument", 1),
            InstPop("this", 6),
            InstAdd(),
            InstSub(),
        ]

        self.assertEqual()
