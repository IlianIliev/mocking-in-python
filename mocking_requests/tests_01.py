import unittest

from mocking_requests.rates import get_rate


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_rate('EUR', 'USD'), 1.0963)
