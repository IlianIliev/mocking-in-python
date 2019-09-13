import freezegun
import unittest
from datetime import datetime

from time_traveling.user import User


class Test(unittest.TestCase):

    def test(self):
        with freezegun.freeze_time():
            user = User(email='info@example.org')
            user.save()

            self.assertEqual(user.created, datetime.now())
