from datetime import datetime

import pytz


ULS_TIMEZONE = pytz.timezone('America/New_York')
UTC_TIMEZONE = pytz.timezone('UTC')


def get_now_uls() -> datetime:
    return datetime.now(ULS_TIMEZONE)


def get_now_utc() -> datetime:
    return datetime.now(UTC_TIMEZONE)


def get_today_uls() -> datetime:
    now = get_now_uls()
    return ULS_TIMEZONE.localize(datetime(year=now.year, month=now.month, day=now.day))
