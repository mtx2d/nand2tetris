import unittest
from lib.symbol_table import SymbolTable


class TestSymbolTable(unittest.TestCase):
    def test_add(self):
        st = SymbolTable()
        st.add("LOOP", 5)
        st.add("i", 17)

        self.assertEqual(5, st.table["LOOP"])
        self.assertEqual(17, st.table["i"])

    def test_has_symbol(self):
        st = SymbolTable({"LOOP": 123, "SUM": 15})

        self.assertTrue(st.has_symbol("LOOP"))
        self.assertTrue(st.has_symbol("SUM"))
        self.assertFalse(st.has_symbol("SYMBOL_DOES_NOT_EXIST"))

    def test_get_address(self):
        st = SymbolTable({"LOOP": 222, "SUM": 32})

        self.assertEqual(st.get_address("LOOP"), 222)
        self.assertEqual(st.get_address("SUM"), 32)
        self.assertRaises(ValueError, st.get_address, "WRONG_KEY")
