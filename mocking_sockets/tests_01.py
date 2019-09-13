import unittest

from urllib.request import urlopen
from urllib.error import HTTPError

from mocket import mocketize
from mocket.mockhttp import Entry


RATES_API_URL = 'https://api.exchangeratesapi.io/latest'


class Test(unittest.TestCase):

    @mocketize
    def test_200(self):
        Entry.single_register(
            Entry.GET,
            RATES_API_URL,
            body='mocked_body',
            status=200
        )
        response = urlopen(RATES_API_URL)
        body = response.read()

        self.assertEqual(body, b'mocked_body')

    @mocketize
    def test_404(self):
        Entry.single_register(Entry.GET, RATES_API_URL, status=404)
        with self.assertRaises(HTTPError):
            urlopen(RATES_API_URL)
