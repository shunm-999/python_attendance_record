from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta


class DateUtil:

    @staticmethod
    def create_date_range_for_day(start_date: datetime, end_date: datetime):
        if start_date > end_date:
            return []
        for n in range((end_date - start_date).days + 1):
            yield start_date + timedelta(n)

    @staticmethod
    def create_date_range_for_month(start_date: datetime, end_date: datetime):
        if start_date > end_date:
            return []

        start_date = start_date.replace(day=1)
        end_date = end_date.replace(day=1)

        yield start_date

        while (start_date.year != end_date.year) or (start_date.month != end_date.month):
            start_date = start_date + relativedelta(months=1)
            yield start_date
