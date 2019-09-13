import unittest
from datetime import datetime

from time_traveling.user import User


class TestCreateUser(unittest.TestCase):
    def test_create(self):
        user = User(email='info@example.org')
        user.save()
        self.assertEqual(datetime.now(), user.created)
