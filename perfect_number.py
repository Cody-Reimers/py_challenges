
class PerfectNumber:

    #~~~~ALIQUOT SUM~~~~#

    @staticmethod
    def aliquot(base):
        small_divisors = [ num for num  # 0.5 power == square root
                        in range(1, int(base**0.5) + 1)
                        if base % num == 0 ]

        large_divisors = [ base // num for num in small_divisors ]

        return sum(sorted(small_divisors + large_divisors)[:-1])

    @classmethod
    def classify(cls, number):
        if not isinstance(number, int):
            raise TypeError("Input must be a positive integer")
        if not number > 0:
            raise ValueError("Input must be a positive integer")

        a_sum = cls.aliquot(number)

        return ("abundant" if a_sum > number
                else "perfect" if a_sum == number
                else "deficient")
