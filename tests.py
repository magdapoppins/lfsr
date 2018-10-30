import unittest
from integer_addition import add_bin
from operations import bitwise_xor, bitwise_and, add


class TestAddition(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add("1", "0"), "1")
        self.assertEqual(add("1", "1"), "10")
        self.assertEqual(add("1", "1", out='int'), 2)
        self.assertEqual(add("1", "1", out='int[]'), [1, 0])

    def test_bitwise_xor(self):
        self.assertEqual(bitwise_xor("10", "01"), "11")
        self.assertEqual(bitwise_xor("10", "01", out='str'), "11")
        self.assertEqual(bitwise_xor("10", "01", out='int'), 3)
        self.assertEqual(bitwise_xor("10", "01", out='int[]'), [1, 1])
        self.assertEqual(bitwise_xor("11", "11", out='int[]', pad=False), [0])
        self.assertEqual(bitwise_xor("11", "10"), "01")
        self.assertEqual(bitwise_xor("11", "10", pad=False), "1")

    def test_bitwise_and(self):
        self.assertEqual(bitwise_and("10", "01"), "00")
        self.assertEqual(bitwise_and("10", "01", out='int'), 0)
        self.assertEqual(bitwise_and("10", "01", out='int[]'), [0, 0])
        self.assertEqual(bitwise_and("10", "01", out='int[]', pad=False), [0])

    def test_exception(self):
        with self.assertRaises(ValueError):
            add("1", "1", out='int[')


if __name__ == '__main__':
    unittest.main()