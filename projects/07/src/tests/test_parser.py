import unittest
from unittest import mock
from lib.parser import Parser
from lib.instruction import InstPush, InstPop, InstAdd, InstSub


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
        read_data = "\n".join([
            "push constant 10",
            "pop local 0",
            "pop argument 1",
            "push argument 1",
            "pop this 6",
            "add",
            "sub",
        ])
        mock_open = mock.mock_open(read_data=read_data)
        with mock.patch('builtins.open', mock_open):
            insts = [*Parser("some_file_path").parse()]

        exp_insts = [
            InstPush("constant", 10),
            InstPop("local", 0),
            InstPop("argument", 1),
            InstPush("argument", 1),
            InstPop("this", 6),
            InstAdd(),
            InstSub(),
        ]

        self.assertEqual(exp_insts, insts)
