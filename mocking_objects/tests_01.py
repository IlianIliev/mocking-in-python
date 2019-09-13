import unittest

from mocking_objects import User


class Test(unittest.TestCase):
    def test_profile(self):

        user = User('Test User', 'test@example.org')
        print(user.profile)
