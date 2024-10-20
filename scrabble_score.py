
class Scrabble:

    LETTER_VALUES = {
        "aeioulrnst": 1,
        "dg": 2,
        "bcmp": 3,
        "fhvwy": 4,
        "k": 5,
        "jx": 8,
        "qz": 10,
    }

    #~~~~INITIALIZATION~~~~#

    def __init__(self, word):
        self.word = word

    #~~~~GETTER METHODS~~~~#

    @property
    def word(self):
        return self._word

    #~~~~SETTER METHODS~~~~#

    @word.setter
    def word(self, word):
        self._word = word if isinstance(word, str) else ""

    #~~~~SCRABBLE SCORE~~~~#

    @classmethod
    def calculate_score(cls, word):
        return sum([ score for bracket, score
                  in cls.LETTER_VALUES.items()
                 for letter in word
                  if letter.casefold() in bracket ])

    def score(self):
        return self.__class__.calculate_score(self.word)
