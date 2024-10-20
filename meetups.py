
from datetime import date

###############################################################################

class Meetup:

    DAYS_IN_EACH_MONTH = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    WEEKS_OF_THE_MONTH = {
        "first": 0,
        "second": 1,
        "third": 2,
        "fourth": 3,
        "fifth": 4,
        "teenth": 5,
        "last": 6,
    }
    TEENTH_WEEK_START, TEENTH_WEEK_END = 13, 20
    DAYS_OF_THE_WEEK = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6,
    }

    #~~~~INITIALIZATION~~~~#

    def __init__(self, year, month):
        self.year = year
        self.month = month

    #~~~~REPRESENTATIONS~~~~#

    def _find_last_day(self):
        if (self.month == 2
        and (self.year % 4 == 0
         and (not self.year % 100 == 0
           or self.year % 400 == 0))):
            leap_year_mod = 1
        else:
            leap_year_mod = 0

        return self.__class__.DAYS_IN_EACH_MONTH[self.month] + leap_year_mod

    def _find_weekdays(self, week):
        week = self.__class__.WEEKS_OF_THE_MONTH[week]
        last_day = self._find_last_day()

        if week == 5:
            return list(range(self.__class__.TEENTH_WEEK_START,
                              self.__class__.TEENTH_WEEK_END))
        if week == 6:
            return list(range(last_day - 6, last_day + 1))
        else:
            return [ num for num
                  in range(7 * week + 1, 7 * (week + 1) + 1)
                  if num <= last_day ]

    def day(self, day, week):
        day, week = day.casefold(), week.casefold()
        weekdays = self._find_weekdays(week)
        dates = [ date(self.year, self.month, day_num)
              for day_num in weekdays ]

        try:
            return [ date for date in dates
                 if date.weekday() == self.__class__.DAYS_OF_THE_WEEK[day] ][0]
        except IndexError:
            return None

    #~~~~GETTER METHODS~~~~#

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    #~~~~SETTER METHODS~~~~#

    @year.setter
    def year(self, year):
        self._year = year

    @month.setter
    def month(self, month):
        self._month = month
