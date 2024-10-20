
class BeerSong:

    #~~~~INITIALIZATION~~~~#

    def __init__(self):
        pass

    #~~~~VERSE GENERATION~~~~#

    @staticmethod
    def standard_verse(number):
        return (f"{number} bottles of beer on the wall, "
                f"{number} bottles of beer.\n"
                "Take one down and pass it around, "
                f"{number - 1} bottles of beer on the wall.\n")

    @staticmethod
    def two_bottles_verse():
        return ("2 bottles of beer on the wall, "
                "2 bottles of beer.\n"
                "Take one down and pass it around, "
                "1 bottle of beer on the wall.\n")

    @staticmethod
    def one_bottle_verse():
        return ("1 bottle of beer on the wall, "
                "1 bottle of beer.\n"
                "Take it down and pass it around, "
                "no more bottles of beer on the wall.\n")

    @staticmethod
    def zero_bottles_verse():
        return ("No more bottles of beer on the wall, "
                "no more bottles of beer.\n"
                "Go to the store and buy some more, "
                "99 bottles of beer on the wall.\n")

    @classmethod
    def verse(cls, number):
        if number > 2:
            return cls.standard_verse(number)
        if number == 2:
            return cls.two_bottles_verse()
        if number == 1:
            return cls.one_bottle_verse()

        return cls.zero_bottles_verse()

    @classmethod
    def verses(cls, first, last):
        return "\n".join([ cls.verse(number) for number
                        in range(first, last - 1, -1) ])

    @classmethod
    def lyrics(cls):
        return cls.verses(99, 0)
