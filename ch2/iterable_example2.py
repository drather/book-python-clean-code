from datetime import timedelta
from datetime import date


class DateRangeIterable:
    """
    자체 이터러블 메서드 가진 이터러블 객체
    """
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self):
        current_day = self.start_date
        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)


if __name__ == '__main__':
    for day in DateRangeIterable(date(2019, 1, 1), date(2019, 1, 10)):
        print(day)

