import mock
import unittest

from simple_mocking.currency_converter import currency_converter, RATES


class Test(unittest.TestCase):
    def test_convert_currency(self):
        with mock.patch(
                'simple_mocking.currency_converter.get_conversion_rate')\
                as get_conversion_rate_mock:

            get_conversion_rate_mock.return_value = 1.22
            result = currency_converter(100, 'EUR', 'USD')
            self.assertEqual(result, 100 * 1.22)

    def test_with_unsupported_currencies(self):
        with mock.patch.dict(RATES, {}, clear=True):
            with self.assertRaises(KeyError):
                result = currency_converter(100, 'EUR', 'USD')
                self.assertEqual(result, 100 * 1.11)
