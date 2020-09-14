import unittest
from lib.symbol_table import SymbolTable


class TestSymbolTable(unittest.TestCase):
    def test_add_entry(self):
        st = SymbolTable()
        st.add_entry("LOOP", 3)
        st.add_entry("END EQ", 5)

        self.assertTrue(st.contains("R0"))
        self.assertTrue(st.contains("R1"))
        self.assertTrue(st.contains("R2"))
        self.assertEqual(3, st.table["LOOP"])
        self.assertEqual(5, st.table["END EQ"])

    def test_contains(self):
        st = SymbolTable({"LOOP": 123, "SUM": 23})

        self.assertTrue(st.contains("LOOP"))
        self.assertTrue(st.contains("SUM"))
        self.assertFalse(st.contains("SYMBOL_DOES_NOT_EXIST"))

    def test_get_address(self):
        st = SymbolTable({"LOOP": 222, "SUM": 32})

        self.assertEqual(st.get_address("LOOP"), 222)
        self.assertEqual(st.get_address("SUM"), 32)

        self.assertFalse(st.contains("NEW_KEY"))
        st.get_address("NEW_KEY")
        self.assertTrue(st.contains("NEW_KEY"))

    def test_get_address(self):
        st = SymbolTable()
        st.get_address("SUM")  # SUM, 16
        st.get_address("i")  # i, 17

        self.assertEqual(16, st.get_address("SUM"))
        self.assertEqual(17, st.get_address("i"))
