import datetime
import freezegun


with freezegun.freeze_time('2019-12-30'):
    now = datetime.datetime.now()
    print(now)

    in_six_days = now + datetime.timedelta(days=6)
    print(in_six_days)
