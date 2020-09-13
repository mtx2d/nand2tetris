import unittest
from lib.symbol_table import SymbolTable


class TestSymbolTable(unittest.TestCase):
    def test_add_label(self):
        st = SymbolTable()
        st.add_label("LOOP", 3)
        st.add_label("END EQ", 5)

        self.assertTrue(st.has_symbol("R0"))
        self.assertTrue(st.has_symbol("R1"))
        self.assertTrue(st.has_symbol("R2"))
        self.assertEqual(3, st.table["LOOP"])
        self.assertEqual(5, st.table["END EQ"])

    def test_has_symbol(self):
        st = SymbolTable({"LOOP": 123, "SUM": 23})

        self.assertTrue(st.has_symbol("LOOP"))
        self.assertTrue(st.has_symbol("SUM"))
        self.assertFalse(st.has_symbol("SYMBOL_DOES_NOT_EXIST"))

    def test_get(self):
        st = SymbolTable({"LOOP": 222, "SUM": 32})

        self.assertEqual(st.get("LOOP"), 222)
        self.assertEqual(st.get("SUM"), 32)
        self.assertRaises(ValueError, st.get, "WRONG_KEY")

    def test_get_or_add(self):
        st = SymbolTable()
        st.get_or_add("SUM")  # SUM, 16
        st.get_or_add("i")  # i, 17

        self.assertEqual(16, st.get("SUM"))
        self.assertEqual(17, st.get("i"))
