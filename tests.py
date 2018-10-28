import unittest
from integer_addition import integer_add
from bitwise_addition import bitwise_add

class TestAddition(unittest.TestCase):
    def test_integer_addition(self):
        self.assertEqual(integer_add("101", "000"), [1,0,1])
        self.assertEqual(integer_add("011", "010"), [1,0,1])
    
    def test_bitwise_add(self):
        self.assertEqual(bitwise_add("1011", "0110"), [1,1,0,1])
        self.assertEqual(bitwise_add("1001", "0000"), [1,0,0,1])
    

if __name__ == '__main__':
    unittest.main()