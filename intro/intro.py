import unittest


def square_it(x):
    return x * x


class SimpleTest(unittest.TestCase):
    def test_square_it(self):
        self.assertEqual(square_it(2), 4)
