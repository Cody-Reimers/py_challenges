
import data_processing as process

###############################################################################

class RomanNumeral:

    #~~~~INITIALIZATION~~~~#

    def __init__(self, number):
        self.number = number

    #~~~~REPRESENTATIONS~~~~#

    NUMERALS = {
        1_000: "M",
        500: "D",
        100: "C",
        50: "L",
        10: "X",
        5: "V",
        1: "I",
    }

    def _get_1000s(self, current):
        result = self.__class__.NUMERALS[1000] * (current[0] // 1000)
        current[0] %= 1000

        return result

    def _get_100s(self, current):
        result = self.__class__.NUMERALS[100] * (current[0] // 100)
        current[0] %= 100

        if len(result) == 9:
            result = (self.__class__.NUMERALS[100]
                    + self.__class__.NUMERALS[1000])
        elif len(result) > 4:
            result = (self.__class__.NUMERALS[500]
                   + self.__class__.NUMERALS[100] * (len(result) % 5))
        elif len(result) == 4:
            result = (self.__class__.NUMERALS[100]
                    + self.__class__.NUMERALS[500])

        return result

    def _get_10s(self, current):
        result = self.__class__.NUMERALS[10] * (current[0] // 10)
        current[0] %= 10

        if len(result) == 9:
            result = (self.__class__.NUMERALS[10]
                    + self.__class__.NUMERALS[100])
        elif len(result) > 4:
            result = (self.__class__.NUMERALS[50]
                   + self.__class__.NUMERALS[10] * (len(result) % 5))
        elif len(result) == 4:
            result = (self.__class__.NUMERALS[10]
                    + self.__class__.NUMERALS[50])

        return result

    def _get_1s(self, current):
        result = self.__class__.NUMERALS[1] * current[0]

        if len(result) == 9:
            result = (self.__class__.NUMERALS[1]
                    + self.__class__.NUMERALS[10])
        elif len(result) > 4:
            result = (self.__class__.NUMERALS[5]
                   + self.__class__.NUMERALS[1] * (len(result) % 5))
        elif len(result) == 4:
            result = (self.__class__.NUMERALS[1]
                    + self.__class__.NUMERALS[5])

        return result

    def to_roman(self):
        current, result = [self.number], ""

        result += self._get_1000s(current)
        result += self._get_100s(current)
        result += self._get_10s(current)
        result += self._get_1s(current)

        return result

    #~~~~GETTER METHODS~~~~#

    @property
    def number(self):
        return self._number

    #~~~~SETTER METHODS~~~~#

    @number.setter
    def number(self, number):
        ref = "Roman Numeral Number Value"

        process.error_not_int(number, ref)
        if number <= 0:
            raise ValueError(f"{repr(ref)} must be greater than 0!")

        self._number = number
