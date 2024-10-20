
import data_processing as process

###############################################################################

class Triangle:

    #~~~~INITIALIZATION~~~~#

    def __init__(self, side1, side2, side3):
        self._set_side1(side1, side2, side3)
        self._set_side2(side2, side1, side3)
        self._set_side3(side3, side1, side2)

    #~~~~REPRESENTATIONS~~~~#

    KINDS_OF_TRIANGLE = {
        "sides": {
            3: "equilateral",
            2: "isosceles",
            0: "scalene",
        },
    }

    @property
    def kind(self):
        if len(set(self.sides)) == 1:
            return self.__class__.KINDS_OF_TRIANGLE["sides"][3]
        if len(set(self.sides)) == 2:
            return self.__class__.KINDS_OF_TRIANGLE["sides"][2]

        return self.__class__.KINDS_OF_TRIANGLE["sides"][0]

    #~~~~GETTER METHODS~~~~#

    @property
    def side1(self):
        return self._side1

    @property
    def side2(self):
        return self._side2

    @property
    def side3(self):
        return self._side3

    @property
    def sides(self):
        return (self.side1, self.side2, self.side3)

    #~~~~SETTER METHODS~~~~#

    @side1.setter
    def side1(self, side1):
        self._set_side1(side1, self.side2, self.side3)

    def _set_side1(self, side1, side2, side3):
        ref = "Triangle Side 1 Length"

        process.error_not_int_or_float(side1, ref)
        if side1 <= 0:
            raise ValueError(f"{repr(ref)} must be greater than 0!")
        if side2 + side3 <= side1:
            raise ValueError(f"{repr(ref)} must be less than the length "
                              "of both other sides combined.")

        self._side1 = side1

    @side2.setter
    def side2(self, side2):
        self._set_side1(side2, self.side1, self.side3)

    def _set_side2(self, side2, side1, side3):
        ref = "Triangle Side 2 Length"

        process.error_not_int_or_float(side2, ref)
        if side2 <= 0:
            raise ValueError(f"{repr(ref)} must be greater than 0!")
        if side1 + side3 <= side2:
            raise ValueError(f"{repr(ref)} must be less than the length "
                              "of both other sides combined.")

        self._side2 = side2

    @side3.setter
    def side3(self, side3):
        self._set_side3(side3, self.side1, self.side2)

    def _set_side3(self, side3, side1, side2):
        ref = "Triangle Side 3 Length"

        process.error_not_int_or_float(side3, ref)
        if side3 <= 0:
            raise ValueError(f"{repr(ref)} must be greater than 0!")
        if side1 + side2 <= side3:
            raise ValueError(f"{repr(ref)} must be less than the length "
                              "of both other sides combined.")

        self._side3 = side3

###############################################################################
