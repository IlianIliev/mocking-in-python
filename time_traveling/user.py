import time
from datetime import datetime


class User:
    def __init__(self, email):
        self.email = email
        self.created = datetime.now()

    def save(self):
        time.sleep(1)
        return
