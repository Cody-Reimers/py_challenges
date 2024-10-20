
import data_processing as process

###############################################################################

class DNA:

    #~~~~INITIALIZATION~~~~#

    def __init__(self, strand):
        self.strand = strand

    #~~~~REPRESENTATIONS~~~~#

    def __str__(self):
        return self.strand

    #~~~~HAMMING DISTANCE~~~~#

    def hamming_distance(self, other):
        if isinstance(other, self.__class__):
            other = str(other)

        self._validate(other)

        index, count = 0, 0
        for char in self.strand:
            try:
                if other[index] != char:
                    count += 1
            except IndexError:
                break

            index += 1

        return count

    #~~~~GETTER METHODS~~~~#

    @property
    def strand(self):
        return self._strand

    #~~~~SETTER METHODS~~~~#

    VALID_BASES = "ACGT"

    def _validate(self, strand):
        ref = "DNA Strand"

        process.error_not_string(strand, ref)
        for char in strand:
            if char not in self.__class__.VALID_BASES:
                raise ValueError("Each DNA base must be one of the valid "
                                 " bases: 'A', 'C', 'G', or 'T'.")

    @strand.setter
    def strand(self, strand):
        self._validate(strand)

        self._strand = strand
