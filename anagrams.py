
import data_processing as process

###############################################################################

class Anagram:

    #~~~~INITIALIZATION~~~~#

    def __init__(self, word):
        self.word = word

    #~~~~COMPARISONS~~~~#

    def is_same_word(self, other):
        return self.word.casefold() == other.casefold()

    def match(self, candidate_list):
        self_letters = Anagram.word_letters(self.word)

        return [ candidate for candidate in candidate_list
              if (not self.is_same_word(candidate)
                  and self_letters == Anagram.word_letters(candidate)) ]

    #~~~~GETTER METHODS~~~~#

    @property
    def word(self):
        return self._word

    #~~~~SETTER METHODS~~~~#

    @word.setter
    def word(self, word):
        ref = "Anagram Word"

        process.error_not_string(word, ref)
        if not word.isalpha():
            raise ValueError(f"{ref} must be an alphabetical string.")

        self._word = word

    #~~~~LETTER COUNTING~~~~#

    @staticmethod
    def word_letters(word):
        letter_count = {}
        word = word.casefold()

        for letter in word:
            letter_count.setdefault(letter, 0)
            letter_count[letter] += 1

        return letter_count

###############################################################################
