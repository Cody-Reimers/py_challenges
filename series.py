
class Series:

    #~~~~INITIALIZATION~~~~#

    def __init__(self, string):
        self.string = string

    #~~~~GETTER METHODS~~~~#

    @property
    def string(self):
        return self._string

    #~~~~SETTER METHODS~~~~#

    @string.setter
    def string(self, string):
        self._string = string

    #~~~~SERIES SLICING~~~~#

    def _generate_attempt(self):
        for start in range(len(self.string)):
            for stop in range(1, len(self.string) + 1):
                yield self.string[start:stop]

    def slices(self, length):
        if length > len(self.string):
            raise ValueError("Slice too long!")

        return [ [ int(digit) for digit in attempt ]
               for attempt in self._generate_attempt()
               if len(attempt) == length ]
