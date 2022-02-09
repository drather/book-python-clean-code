from datetime import timedelta
from datetime import date


class DateRangeIterable:
    """
    자체 이터러블 메서드 가진 이터러블 객체
    """
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_date = start_date

    def __iter__(self):
        return self

    def __next__(self):
        if self._present_date >= self.end_date:
            raise StopIteration
        today = self._present_date
        self._present_date += timedelta(days=1)

        return today


if __name__ == '__main__':
    for day in DateRangeIterable(date(2019, 1, 1), date(2019, 1, 10)):
        print(day)

