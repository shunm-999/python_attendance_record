import unittest
from datetime import datetime

from util.date_util import DateUtil


class TestDateUtil(unittest.TestCase):

    def test_create_date_range_for_day(self):
        date_range = DateUtil.create_date_range_for_day(start_date=datetime(year=2018, month=2, day=2),
                                                        end_date=datetime(year=2018, month=2, day=4))
        for date in date_range:
            pass

    def test_create_date_range_for_day_wrong_date(self):
        date_range = DateUtil.create_date_range_for_day(start_date=datetime(year=2018, month=2, day=4),
                                                        end_date=datetime(year=2018, month=2, day=2))
        for date in date_range:
            pass

    def test_create_date_range_for_month(self):
        date_range = DateUtil.create_date_range_for_month(start_date=datetime(year=2018, month=2, day=2),
                                                          end_date=datetime(year=2019, month=2, day=2))

        for date in date_range:
            pass

    def test_create_date_range_for_month_wrong_date(self):
        date_range = DateUtil.create_date_range_for_month(start_date=datetime(year=2019, month=2, day=2),
                                                          end_date=datetime(year=2018, month=2, day=2))

        for date in date_range:
            pass
