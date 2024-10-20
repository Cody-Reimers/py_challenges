
class Diamond:

    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #~~~~FORMING A DIAMOND~~~~#

    @staticmethod
    def _generate_line(letter, index, pad_width):
        yield (f"{' ' * (pad_width - index)}" +
               f"{letter}" +
               f"{' ' * (index * 2 - 1)}" +
               f"{letter if index != 0 else ''}" +
               f"{' ' * (pad_width - index)}")

    @classmethod
    def make_diamond(cls, terminal_letter):
        letters = cls.ALPHABET[:cls.ALPHABET.index(terminal_letter) + 1]
        indices = list(range(len(letters)))
        pad_width = len(letters) - 1

        diamond_top = [ line for index in indices for line
                     in cls._generate_line(letters[index], index, pad_width) ]

        return "\n".join(diamond_top + diamond_top[:-1][::-1]) + "\n"
