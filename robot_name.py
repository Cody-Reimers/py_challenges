
import random as r

class Robot:

    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUMBERS = "0123456789"
    USED_NAMES = set()

    #~~~~INITIALIZATION~~~~#

    def __init__(self):
        self._name = None
        self.reset()

    #~~~~GETTER METHODS~~~~#

    @property
    def name(self):
        return self._name

    #~~~~ROBOT RESETTING~~~~#

    def reset(self):
        self.__class__.USED_NAMES.discard(self.name)

        try:
            attempt = "".join(r.choices(self.__class__.ALPHABET, k=2) +
                              r.choices(self.__class__.NUMBERS, k=3))

            if attempt in self.__class__.USED_NAMES:
                raise ValueError
        except ValueError:
            self.reset()
        else:
            self._name = attempt
            self.__class__.USED_NAMES.add(attempt)
