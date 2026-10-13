import unittest

from main import add, greet


class TestMain(unittest.TestCase):
    def test_greet_ohne_name(self):
        self.assertEqual(greet(), "Hello")

    def test_greet_mit_name(self):
        self.assertEqual(greet("Kai"), "Hello Kai")

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negativ(self):
        self.assertEqual(add(-1, 1), 0)


if __name__ == "__main__":
    unittest.main()
