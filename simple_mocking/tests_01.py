import unittest

from simple_mocking.currency_converter import currency_converter


class Test(unittest.TestCase):
    def test_convert_currency(self):
        result = currency_converter(100, 'EUR', 'USD')
        self.assertEqual(result, 100 * 1.11)

    def test_with_unsupported_currencies(self):

        with self.assertRaises(KeyError):
            result = currency_converter(100, 'SEK', 'JPY')
            self.assertEqual(result, 100 * 1.11)
