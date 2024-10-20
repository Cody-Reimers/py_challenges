
class Clock:

    MINUTES_IN_AN_HOUR = 60
    HOURS_IN_A_DAY = 24

    #~~~~INITIALIZATION~~~~#

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    @classmethod
    def at(cls, hours, minutes=0):
        return cls(hours, minutes)

    #~~~~REPRESENTATIONS~~~~#

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

    #~~~~MATH~~~~#

    def __add__(self, other):
        if not isinstance(other, int):
            return NotImplemented

        return self.__class__(self.hours, self.minutes + other)

    def __sub__(self, other):
        if not isinstance(other ,int):
            return NotImplemented

        return self.__class__(self.hours, self.minutes - other)

    #~~~~RICH COMPARISONS~~~~#

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return str(self) == str(other)

    #~~~~GETTER METHODS~~~~#

    @property
    def hours(self):
        return self._hours

    @property
    def minutes(self):
        return self._minutes

    #~~~~SETTER METHODS~~~~#

    @hours.setter
    def hours(self, hours):
        self._hours = hours % self.__class__.HOURS_IN_A_DAY

    @minutes.setter
    def minutes(self, minutes):
        self._minutes = minutes % self.__class__.MINUTES_IN_AN_HOUR

        if not 0 <= minutes < self.__class__.MINUTES_IN_AN_HOUR:
            self.hours += minutes // self.__class__.MINUTES_IN_AN_HOUR
