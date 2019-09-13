import unittest
import freezegun

from time_traveling.invoice import Invoice


class Test(unittest.TestCase):

    def test_invoice_get_status(self):
        with freezegun.freeze_time('2019-01-01'):
            invoice = Invoice()
            self.assertEqual(invoice.status, Invoice.STATUS_DUE)

        with freezegun.freeze_time('2019-01-06'):
            self.assertEqual(invoice.status, Invoice.STATUS_FIRST_REMINDER)

        with freezegun.freeze_time('2019-01-17'):
            self.assertEqual(invoice.status, Invoice.STATUS_SECOND_REMINDER)
