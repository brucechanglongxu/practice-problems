import unittest
from red_black_cards import expected_value


class test_game(unittest.TestCase):
    def test_game1(self):
        value = expected_value(1, 1)
        self.assertEqual(value, 0.5)

    def test_game2(self):
        value = expected_value(0, 5)
        self.assertEqual(value, 5)

    def test_game3(self):
        value = expected_value(5, 0)
        self.assertEqual(value, 0)

    def test_game4(self):
        value = expected_value(2, 2)
        self.assertEqual(value, 2/3)

    def test_game5(self):
        value = expected_value(3, 3)
        self.assertEqual(value, 0.85)

    def test_game6(self):
        value = expected_value(-1, 5)
        self.assertEqual(value, -1)

    def test_game7(self):
        value = expected_value(5, -2)
        self.assertEqual(value, -1)

    def test_game8(self):
        value = expected_value(Hello, 0)
        self.assertEqual(value, -1)

if __name__ == "__main__":
    unittest.main()
