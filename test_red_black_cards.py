import unittest
from red_black_cards import expected_value

class testGame(unittest.TestCase):
    def test_game1(self):
        value = expected_value(1, 1)
        self.assertEqual(value, 0.5)
    def test_game2(self):
        value = expected_value(0, 5)
        self.assertEqual(value, 5)
    def test_game3(self):
        value = expected_value(5, 0)
        self.assertEqual(value, 0)

if __name__ == '__main__':
    unittest.main()
