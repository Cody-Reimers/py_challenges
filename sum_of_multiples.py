
class SumOfMultiples:

    #~~~~INITIALIZATION~~~~#

    def __init__(self, *bases):
        self.bases = bases

    #~~~~SUM CALCULATION~~~~#

    @staticmethod
    def sum_up_to(target, bases=(3, 5)):
        return sum({ list_ for base in bases
                 for list_ in range(base, target, base) })

    def to(self, target):
        return self.__class__.sum_up_to(target, self.bases)
