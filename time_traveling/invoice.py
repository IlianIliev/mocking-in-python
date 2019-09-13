from datetime import datetime, timedelta


class Invoice:
    STATUS_DUE = 'due'
    STATUS_FIRST_REMINDER = 'first_reminder'
    STATUS_SECOND_REMINDER = 'second_reminder'

    def __init__(self):
        self.due_date = datetime.now()

    @property
    def status(self):
        now = datetime.now()

        if self.due_date >= now - timedelta(days=5):
            return self.STATUS_DUE
        elif self.due_date >= now - timedelta(days=10):
            return self.STATUS_FIRST_REMINDER
        else:
            return self.STATUS_SECOND_REMINDER
