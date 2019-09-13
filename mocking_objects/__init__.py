import hashlib


class AvatarService:
    def get_avatar(self, key):
        raise NotImplementedError


class User:
    def __init__(self, name, email):
        self.salt = 'Really bad salt'
        self.name = name
        self.email = email

    def get_avatar(self):
        hash_string = '{self.salt}-{self.email}'.format(self=self)
        hash = hashlib.sha1(hash_string.encode('utf-8')).hexdigest()
        return AvatarService().get_avatar(hash)

    @property
    def profile(self):
        return {
            'name': self.name,
            'email': self.email,
            'avatar': self.get_avatar()
        }
