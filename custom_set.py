
class CustomSet:

    #~~~~INITIALIZATION~~~~#

    def __init__(self, head=None):
        self.size = 0
        self.head = None

        if head and isinstance(head, list):
            for datum in head:
                self.add(datum)

    #~~~~COMPARISON~~~~#

    def is_subset(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        if self.is_empty():
            return True

        return all([ datum in other.to_list()
                 for datum in self.to_list() ])

    def is_disjoint(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        if self.is_empty():
            return True

        return all([ datum not in other.to_list()
                 for datum in self.to_list() ])

    def is_same(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        if len(self.to_list()) != len(other.to_list()):
            return False

        return all([ datum in other.to_list()
                 for datum in self.to_list() ])

    def __eq__(self, other):
        return self.is_same(other)

    #~~~~MERGING~~~~#

    def intersection(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        combined = self.to_list() + other.to_list()

        return self.__class__([ datum for datum in combined
                             if (datum in self.to_list()
                             and datum in other.to_list()) ])

    def difference(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return self.__class__([ datum for datum in self.to_list()
                             if datum not in other.to_list() ])

    def union(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return self.__class__(self.to_list() + other.to_list())

    #~~~~GETTER METHODS~~~~#

    @property
    def head(self):
        return self._head

    @property
    def size(self):
        return self._size

    #~~~~SETTER METHODS~~~~#

    @head.setter
    def head(self, head):
        self._head = head

    @size.setter
    def size(self, size):
        self._size = size

    def is_empty(self):
        return self.size == 0

    #~~~~CHAIN MANAGEMENT~~~~#

    def in_chain(self, datum):
        return not self.is_empty() and self.head.in_chain(datum)

    def contains(self, datum):
        return self.in_chain(datum)

    def to_list(self):
        list_ = []

        if self.is_empty():
            return list_

        current = self.head

        while current is not None:
            list_.append(current.datum)
            current = current.ref

        return list_

    def add(self, datum):
        if self.in_chain(datum):
            return

        old = self.head
        self.head = Element(datum, old)
        self.size += 1

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#//////////////////////////////////////////////////////////////////////////////

class Element:

    #~~~~INITIALIZATION~~~~#

    def __init__(self, datum, ref=None):
        self.datum = datum
        self.ref = ref

    #~~~~GETTER METHODS~~~~#

    @property
    def datum(self):
        return self._datum

    @property
    def ref(self):
        return self._ref

    #~~~~SETTER METHODS~~~~#

    @datum.setter
    def datum(self, datum):
        self._datum = datum

    @ref.setter
    def ref(self, ref):
        self._ref = ref

    #~~~~CHAIN MANAGEMENT~~~~#

    def in_chain(self, datum):
        if self.is_tail():
            return self.datum == datum

        return self.datum == datum or self.ref.in_chain(datum)

    def is_tail(self):
        return self.ref is None

    @property
    def tail(self):
        if self.is_tail():
            return self.datum

        return self.ref.tail
