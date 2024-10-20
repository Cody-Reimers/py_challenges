
class Octal:

    #~~~~INITIALIZATION~~~~#

    def __init__(self, octal_string):
        self.octal_string = octal_string

    #~~~~REPRESENTATIONS~~~~#

    def to_decimal(self):
        # Treat invalid octal_string as 0 
        if not self.octal_string.isnumeric():
            return 0
        if any([ digit in ("8", "9") for digit in self.octal_string ]):
            return 0

        places = dict(zip(range(len(self.octal_string)),
                          self.octal_string[::-1]))

        return sum([ int(digit) * 8**place
                 for place, digit in places.items() ])

    #~~~~GETTER METHODS~~~~#

    @property
    def octal_string(self):
        return self._octal_string

    #~~~~SETTER METHODS~~~~#

    @octal_string.setter
    def octal_string(self, octal_string):
        self._octal_string = (octal_string if isinstance(octal_string, str)
                                         else "0")
