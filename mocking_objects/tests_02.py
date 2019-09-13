import mock
import unittest

from mocking_objects import User


class Test(unittest.TestCase):
    def test_profile(self):
        name = 'Test User'
        email = 'test@example.org'
        avatar = '/avatars/001.png'
        user = User(name, email)

        with mock.patch.object(user, 'get_avatar', return_value=avatar):
            expected_profile = {
                'name': name,
                'email': email,
                'avatar': avatar
            }
            self.assertEqual(user.profile, expected_profile)
