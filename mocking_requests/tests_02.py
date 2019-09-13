import unittest
import responses

from mocking_requests.rates import get_rate, RATES_API_URL


class Test(unittest.TestCase):

    @responses.activate
    def test(self):
        mock_response = {
            'rates': {
                'USD': 1.0963
            }
        }
        responses.add(
            responses.GET, RATES_API_URL, json=mock_response, status=200)
        self.assertEqual(get_rate('EUR', 'USD'), 1.0963)

    @responses.activate
    def test_failed_call(self):

        responses.add(responses.GET, RATES_API_URL, status=503)
        self.assertIsNone(get_rate('EUR', 'USD'))
